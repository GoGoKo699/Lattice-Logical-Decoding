#!/usr/bin/env python3
"""Reproduce finite algebra and numerical identity checks using only the stdlib.

These checks catch normalization, parity, coordinate-permutation, and smoothing
formula mistakes. They do not prove asymptotic geometry, LWE hardness, or a
physical implementation theorem. Run from any directory; see README.md here.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import random


SEED = 20261023


def require(condition, message):
    """Do not use Python assert: checks must also run under python -O."""
    if not condition:
        raise AssertionError(message)


def transpose(a):
    return [list(row) for row in zip(*a)]


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    columns = transpose(b)
    return [[sum(x * y for x, y in zip(row, column)) for column in columns]
            for row in a]


def matvec(a, v):
    return [sum(x * y for x, y in zip(row, v)) for row in a]


def modulo(a, q):
    return [[x % q for x in row] for row in a]


def block_diagonal(a, b):
    return ([row + [0] * len(b[0]) for row in a]
            + [[0] * len(a[0]) + row for row in b])


def rref_mod(a, q):
    """Reduced row echelon form over the prime field F_q."""
    out = modulo(a, q)
    row = 0
    pivots = []
    for column in range(len(out[0])):
        pivot = next((i for i in range(row, len(out)) if out[i][column]), None)
        if pivot is None:
            continue
        out[row], out[pivot] = out[pivot], out[row]
        inverse = pow(out[row][column], -1, q)
        out[row] = [(x * inverse) % q for x in out[row]]
        for i in range(len(out)):
            if i != row and out[i][column]:
                scale = out[i][column]
                out[i] = [(x - scale * y) % q
                          for x, y in zip(out[i], out[row])]
        pivots.append(column)
        row += 1
        if row == len(out):
            break
    return out, pivots


def inverse_mod(a, q):
    n = len(a)
    reduced, pivots = rref_mod([row + unit for row, unit in zip(a, identity(n))], q)
    require(pivots[:n] == list(range(n)), "singular modular matrix")
    return [row[n:] for row in reduced]


def inverse_rational(a):
    n = len(a)
    rows = [[Fraction(x) for x in row + unit]
            for row, unit in zip(a, identity(n))]
    for column in range(n):
        pivot = next(i for i in range(column, n) if rows[i][column])
        rows[column], rows[pivot] = rows[pivot], rows[column]
        scale = rows[column][column]
        rows[column] = [x / scale for x in rows[column]]
        for i in range(n):
            if i != column and rows[i][column]:
                scale = rows[i][column]
                rows[i] = [x - scale * y for x, y in zip(rows[i], rows[column])]
    return [row[n:] for row in rows]


def determinant(a):
    """Exact elimination; matrices are small, so Fraction is sufficient."""
    rows = [[Fraction(x) for x in row] for row in a]
    value = Fraction(1)
    for column in range(len(rows)):
        pivot = next((i for i in range(column, len(rows)) if rows[i][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            value = -value
        diagonal = rows[column][column]
        value *= diagonal
        for i in range(column + 1, len(rows)):
            scale = rows[i][column] / diagonal
            rows[i] = [x - scale * y for x, y in zip(rows[i], rows[column])]
    return value


def kernel_basis(a, q):
    """Return a column basis of the nullspace of a over F_q."""
    reduced, pivots = rref_mod(a, q)
    free = [j for j in range(len(a[0])) if j not in pivots]
    columns = []
    for j in free:
        v = [0] * len(a[0])
        v[j] = 1
        for row, pivot in enumerate(pivots):
            v[pivot] = -reduced[row][j] % q
        columns.append(v)
    return transpose(columns)


def random_full_rank(rng, rows, columns, q, zero_first_row=False):
    while True:
        a = [[rng.randrange(q) for _ in range(columns)] for _ in range(rows)]
        if zero_first_row:
            a[0] = [0] * columns
        if len(rref_mod(a, q)[1]) == columns:
            return a


def integral_basis(a, q):
    """Build H in ORIGINAL coordinates after selecting independent pivot rows.

    With P taking pivot rows first, H = P^T [[I,0],[B,qI]].  Returning
    only the systematic-coordinate matrix would silently break the reduction.
    """
    m, n = len(a), len(a[0])
    require(m == 2 * n, "this suite uses the balanced ensemble m=2n")
    pivots = rref_mod(transpose(a), q)[1]
    order = pivots + [i for i in range(m) if i not in pivots]
    change = inverse_mod([a[i] for i in pivots], q)
    systematic = modulo(matmul([a[i] for i in order], change), q)
    require(systematic[:n] == identity(n), "systematic top block is not I")
    h_systematic = ([row + [0] * n for row in identity(n)]
                    + [row + [q * x for x in unit]
                       for row, unit in zip(systematic[n:], identity(n))])
    h = [None] * m
    for systematic_row, original_row in enumerate(order):
        h[original_row] = h_systematic[systematic_row]
    return h, order


def in_column_space(a, vector, q):
    pivots = rref_mod(transpose(a), q)[1]
    coefficients = matvec(inverse_mod([a[i] for i in pivots], q),
                          [vector[i] for i in pivots])
    return all((x - y) % q == 0 for x, y in zip(matvec(a, coefficients), vector))


def label_and_syndrome(coordinates, bits):
    integers = [math.floor(x) for x in coordinates]
    label = [z % 2 for z in integers]
    syndrome = [math.floor((1 << bits) * (x - z))
                for x, z in zip(coordinates, integers)]
    return label, syndrome


def check_masking():
    cases = 0
    for q in (3, 5, 7):
        for a in itertools.product(range(q), repeat=2):
            if a == (0, 0):
                continue
            for secret in range(q):
                for error in itertools.product(range(-2, 3), repeat=2):
                    b = [(a[j] * secret + error[j]) % q for j in range(2)]
                    for mask in itertools.product((0, 1), repeat=2):
                        y = [(2 * b[j] + mask[j]) % q for j in range(2)]
                        v = [y[j] - 2 * error[j] - mask[j] for j in range(2)]
                        require(all((v[j] - 2 * a[j] * secret) % q == 0
                                    for j in range(2)), "masked target left the code")
                        require(tuple((y[j] - v[j]) % 2 for j in range(2)) == mask,
                                "logical parity did not recover the mask")
                        cases += 1

    signed_masks = list(itertools.product((0, 1), repeat=2)) + [(-9, 14), (11, -12), (2, 3)]
    permutations = 0
    for q in (3, 5, 7):
        for mask in signed_masks:
            images = {tuple((2 * b[j] + mask[j]) % q for j in range(2))
                      for b in itertools.product(range(q), repeat=2)}
            require(len(images) == q * q, "uniform challenge map is not a permutation")
            permutations += 1

    # At n=1 enumerate the complete matched-ensemble duality, including all
    # generator-basis randomizations. This is not a proof for general n.
    dual_ensemble_pairs = 0
    for q in (3, 5, 7):
        counts = Counter()
        for a0 in itertools.product(range(q), repeat=2):
            if a0 == (0, 0):
                continue
            kernel = kernel_basis([list(a0)], q)
            for change in range(1, q):
                public_a = tuple(row[0] * change % q for row in kernel)
                require(sum(x * y for x, y in zip(public_a, a0)) % q == 0,
                        "dual generator is not orthogonal")
                counts[public_a] += 1
                dual_ensemble_pairs += 1
        require(len(counts) == q * q - 1 and set(counts.values()) == {q - 1},
                "dual generator distribution is not exactly uniform")

    return {"status": "PASS", "exact_masked_cases": cases,
            "uniform_branch_permutations": permutations,
            "enumerated_dual_ensemble_pairs": dual_ensemble_pairs}


def check_bases_and_frames():
    rng = random.Random(SEED)
    bases = nontrivial_permutations = parity_vectors = frame_cases = 0
    quantization_coordinates = safe_quantizations = exact_boundaries = 0
    for n in (1, 2, 3, 5):
        m = 2 * n
        for q in (5, 11, 31):
            for trial in range(10):
                # Half the cases force a leading dependent row so that row
                # permutation cannot be accidentally omitted. These deliberately
                # targeted cases are algebra tests, not samples for hardness.
                original_a = random_full_rank(rng, m, n, q, zero_first_row=(trial % 2 == 0))
                a0 = modulo(matmul(kernel_basis(transpose(original_a), q),
                                   random_full_rank(rng, n, n, q)), q)
                public_a = modulo(matmul(kernel_basis(transpose(a0), q),
                                         random_full_rank(rng, n, n, q)), q)
                require(modulo(matmul(transpose(a0), public_a), q)
                        == [[0] * n for _ in range(n)], "ensemble duality failed")

                h, order = integral_basis(public_a, q)
                h_inverse = inverse_rational(h)
                g_fractional = [[q * x for x in row] for row in transpose(h_inverse)]
                require(all(x.denominator == 1 for row in g_fractional for x in row),
                        "dual q-ary basis is not integral")
                g = [[int(x) for x in row] for row in g_fractional]
                g_inverse = [[Fraction(x, q) for x in row] for row in transpose(h)]
                require(matmul(h, h_inverse) == identity(m), "H inverse failed")
                require(matmul(g, g_inverse) == identity(m), "G inverse failed")
                require(matmul(transpose(h), g) == [[q * x for x in row] for row in identity(m)],
                        "H^T G != qI")
                require(abs(determinant(h)) == q ** n and abs(determinant(g)) == q ** n,
                        "primal or dual covolume mismatch")
                require(all(in_column_space(public_a, column, q) for column in transpose(h)),
                        "H is not in the public q-ary lattice")
                require(all(in_column_space(a0, column, q) for column in transpose(g)),
                        "G is not in the LWE-challenge q-ary lattice")

                t_basis = block_diagonal(h, g)
                zero = [[0] * m for _ in range(m)]
                symplectic = ([z + unit for z, unit in zip(zero, identity(m))]
                              + [[-x for x in unit] + z for unit, z in zip(identity(m), zero)])
                pairing = matmul(matmul(transpose(t_basis), symplectic), t_basis)
                require(pairing == [[q * x for x in row] for row in symplectic],
                        "exact symplectic normalization failed")
                # T^T J T=qJ implies K^T J K=J/2 and Gamma^T J Gamma=2J.
                # det(T)=q^m then gives det(S)=1 and det(Gamma)=2^m exactly.
                require(determinant(h) * determinant(g) == q ** m,
                        "phase-space orientation/covolume mismatch")

                for basis in (h, g):
                    parity_inverse = inverse_mod(basis, 2)
                    require(modulo(matmul(basis, parity_inverse), 2) == identity(m),
                            "ambient parity is not a quotient isomorphism")
                    for _ in range(5):
                        coefficient = [rng.randrange(-20, 21) for _ in range(m)]
                        lattice_point = matvec(basis, coefficient)
                        recovered = [x % 2 for x in matvec(parity_inverse, lattice_point)]
                        require(recovered == [x % 2 for x in coefficient],
                                "basis parity extraction failed")
                        parity_vectors += 1

                t_inverse = block_diagonal(h_inverse, g_inverse)
                for sector, challenge, basis in ((0, public_a, h), (1, a0, g)):
                    secret = [rng.randrange(q) for _ in range(n)]
                    error = [rng.randrange(-5, 6) for _ in range(m)]
                    mask = [rng.randrange(-20, 21) for _ in range(m)]
                    b = [(x + e) % q for x, e in zip(matvec(challenge, secret), error)]
                    y = [(2 * x + u) % q for x, u in zip(b, mask)]
                    v = [x - 2 * e - u for x, e, u in zip(y, error, mask)]
                    dither = [Fraction(rng.randrange(-100, 101), 4096) for _ in range(m)]
                    independent = [Fraction(rng.randrange(-100, 101), 4096) for _ in range(m)]
                    masked_noise = [2 * e + u + d for e, u, d in zip(error, mask, dither)]
                    masked_target = [x + d for x, d in zip(y, dither)]
                    if sector == 0:
                        noise, target, vector = masked_noise + independent, masked_target + independent, v + [0] * m
                    else:
                        noise, target, vector = independent + masked_noise, independent + masked_target, [0] * m + v
                    noise_coordinates = matvec(t_inverse, noise)
                    target_coordinates = matvec(t_inverse, target)
                    shift = matvec(t_inverse, vector)
                    require(all(x.denominator == 1 for x in shift),
                            "challenge displacement is not a K vector")
                    require(target_coordinates == [x + k for x, k in zip(noise_coordinates, shift)],
                            "unwrapped coordinate translation failed")

                    true_label, syndrome = label_and_syndrome(noise_coordinates, 8)
                    target_label, target_syndrome = label_and_syndrome(target_coordinates, 8)
                    require(syndrome == target_syndrome, "integer translation changed quantized syndrome")
                    require(target_label == [(ell + int(k)) % 2 for ell, k in zip(true_label, shift)],
                            "integer translation changed frame incorrectly")
                    start = sector * m
                    parity_shift = matvec(inverse_mod(basis, 2), [x + u for x, u in zip(y, mask)])
                    computed_label = [(target_label[start + i] + parity_shift[i]) % 2 for i in range(m)]
                    require(computed_label == true_label[start:start + m],
                            "full-frame parity formula failed in original coordinates")
                    frame_cases += 1

                    # Finite arithmetic regression, not a probabilistic boundary
                    # lemma: exact rationals let us identify every boundary.
                    bits, precision = 8, 48
                    for coordinate in noise_coordinates + target_coordinates:
                        quantization_coordinates += 1
                        grid_coordinate = coordinate * (1 << bits)
                        fraction = grid_coordinate - math.floor(grid_coordinate)
                        distance = min(fraction, 1 - fraction) / (1 << bits)
                        rounded = Fraction(math.floor(coordinate * (1 << precision)), 1 << precision)
                        if distance == 0:
                            exact_boundaries += 1
                        elif distance > Fraction(1, 1 << precision):
                            require(label_and_syndrome([coordinate], bits)
                                    == label_and_syndrome([rounded], bits),
                                    "safe finite-precision rounding changed syndrome/frame")
                            safe_quantizations += 1
                bases += 1
                nontrivial_permutations += int(order != list(range(m)))

    require(nontrivial_permutations >= 60, "permutation-sensitive cases were not exercised")
    # Deliberately straddle a grid boundary and an integer boundary. This prevents
    # the regression from assuming that every real input tolerates rounding.
    epsilon = Fraction(1, 1 << 40)
    for center in (Fraction(7, 256), Fraction(1)):
        left = label_and_syndrome([center - epsilon], 8)
        right = label_and_syndrome([center + epsilon], 8)
        require(left[1] != right[1], "grid-crossing adversarial case was not detected")
        if center == 1:
            require(left[0] != right[0], "integer-crossing frame change was not detected")

    return {"status": "PASS", "exact_basis_instances": bases,
            "nontrivial_original_coordinate_permutations": nontrivial_permutations,
            "exact_primal_and_dual_parity_vectors": parity_vectors,
            "exact_position_and_momentum_frame_cases": frame_cases,
            "quantization_coordinates": quantization_coordinates,
            "safe_finite_precision_roundings": safe_quantizations,
            "exact_boundary_coordinates_reported_not_assumed_safe": exact_boundaries,
            "adversarial_boundary_crossings": 2,
            "symplectic_normalization": "Exact: T^T J T=qJ; K^T J K=J/2; Gamma^T J Gamma=2J",
            "phase_space_covolumes": "Exact: det(S)=1; det(Gamma)=2^m"}


def normalizer(width):
    limit = math.ceil(12 * width)
    return math.fsum(math.exp(-k * k / (2 * width * width)) for k in range(-limit, limit + 1))


def theta_direct(width, center):
    lower, upper = math.floor(center - 12 * width), math.ceil(center + 12 * width)
    return math.fsum(math.exp(-(k - center) ** 2 / (2 * width * width))
                     for k in range(lower, upper + 1))


def theta_poisson(width, center):
    return math.sqrt(2 * math.pi) * width * (1 + 2 * math.fsum(
        math.exp(-2 * math.pi ** 2 * width ** 2 * k * k) * math.cos(2 * math.pi * k * center)
        for k in range(1, 30)))


def theta_error(width):
    return 2 * math.fsum(math.exp(-2 * math.pi ** 2 * width ** 2 * k * k)
                         for k in range(1, 30))


def density(distribution, width, x):
    denominator = math.sqrt(2 * math.pi) * width
    return math.fsum(probability * math.exp(-(x - z) ** 2 / (2 * width * width))
                     for z, probability in distribution) / denominator


def integrate_tv(distribution, dither_width, total_variance, intervals=16000):
    radius = 9 * math.sqrt(total_variance)
    step = 2 * radius / intervals
    values = []
    gaussian_denominator = math.sqrt(2 * math.pi * total_variance)
    for i in range(intervals + 1):
        x = -radius + i * step
        normal = math.exp(-x * x / (2 * total_variance)) / gaussian_denominator
        values.append(abs(density(distribution, dither_width, x) - normal))
    fine = step * (math.fsum(values) - (values[0] + values[-1]) / 2) / 2
    coarse = 2 * step * (math.fsum(values[::2]) - (values[0] + values[-1]) / 2) / 2
    return fine, abs(fine - coarse)


def check_smoothing():
    max_theta_relative_error = 0.0
    for width in (0.45, 0.8, 1.5, 3.0):
        for center in (-2.75, -0.5, 0.0, 0.125, 0.9, 3.25):
            direct, fourier = theta_direct(width, center), theta_poisson(width, center)
            relative_error = abs(direct - fourier) / direct
            require(relative_error < 2e-13, "Poisson theta identity failed numerically")
            max_theta_relative_error = max(max_theta_relative_error, relative_error)

    records = []
    for r, mask_width, dither_width in ((4.0, 1.0, 1.0), (4.0, 2.0, 2.0),
                                        (8.0, 2.0, 2.0), (8.0, 3.0, 3.0)):
        variance = 4 * r * r + mask_width * mask_width
        s = math.sqrt(variance)
        theta_width = r * mask_width / s
        error_limit = math.ceil(12 * r)
        error_weights = [(e, math.exp(-e * e / (2 * r * r)))
                         for e in range(-error_limit, error_limit + 1)]
        normalization = normalizer(r) * normalizer(mask_width)
        z_limit = math.ceil(9 * s)
        distribution = [(z, math.fsum(weight * math.exp(-(z - 2 * e) ** 2 / (2 * mask_width ** 2))
                                      for e, weight in error_weights) / normalization)
                        for z in range(-z_limit, z_limit + 1)]
        discrete_normal = [(z, math.exp(-z * z / (2 * variance)) / normalizer(s))
                           for z in range(-z_limit, z_limit + 1)]
        discrete_tv = math.fsum(abs(p - target)
                                for (_, p), (_, target) in zip(distribution, discrete_normal)) / 2
        delta = theta_error(theta_width)
        discrete_bound = 2 * delta / (1 - delta)
        require(discrete_tv <= discrete_bound + 3e-14, "discrete smoothing exceeded theta bound")
        require(abs(math.fsum(p for _, p in distribution) - 1) < 3e-14,
                "truncated convolution lost material probability")

        max_discrete_identity_error = 0.0
        for z, probability in distribution:
            center = 2 * r * r * z / variance
            completed_square = math.exp(-z * z / (2 * variance)) * theta_direct(theta_width, center) / normalization
            relative_error = abs(probability - completed_square) / probability
            max_discrete_identity_error = max(max_discrete_identity_error, relative_error)
        require(max_discrete_identity_error < 3e-12, "first completed-square identity failed")

        total_variance = variance + dither_width * dither_width
        second_width = s * dither_width / math.sqrt(total_variance)
        delta_second = theta_error(second_width)
        continuous_bound = discrete_bound + 2 * delta_second / (1 - delta_second)
        continuous_tv, quadrature_change = integrate_tv(distribution, dither_width, total_variance)
        require(continuous_tv <= continuous_bound + 3e-13, "continuous smoothing exceeded theta bound")
        require(quadrature_change < 2e-7, "quadrature refinement did not stabilize")

        max_continuous_identity_error = 0.0
        for multiple in (-3.0, -1.0, -0.125, 0.0, 0.375, 1.0, 3.0):
            x = multiple * math.sqrt(total_variance)
            mixed = density(discrete_normal, dither_width, x)
            gaussian = math.exp(-x * x / (2 * total_variance)) / math.sqrt(2 * math.pi * total_variance)
            predicted_ratio = (theta_poisson(second_width, variance * x / total_variance)
                               / (math.sqrt(2 * math.pi) * second_width))
            predicted_ratio /= normalizer(s) / (math.sqrt(2 * math.pi) * s)
            relative_error = abs(mixed / gaussian - predicted_ratio)
            max_continuous_identity_error = max(max_continuous_identity_error, relative_error)
        require(max_continuous_identity_error < 3e-12, "second completed-square identity failed")

        limit = math.ceil(12 * mask_width)
        parity_bias = math.fsum((1 if k % 2 == 0 else -1) * math.exp(-k * k / (2 * mask_width ** 2))
                                for k in range(-limit, limit + 1)) / normalizer(mask_width)
        poisson_bias = (math.sqrt(2 * math.pi) * mask_width / normalizer(mask_width)) * math.fsum(
            math.exp(-2 * math.pi ** 2 * mask_width ** 2 * (k + 0.5) ** 2) for k in range(-30, 30))
        require(abs(parity_bias - poisson_bias) < 2e-14, "mask-parity Poisson formula failed")

        records.append({"r": r, "R": mask_width, "R2": dither_width,
                        "discrete_tv_finite_sum": discrete_tv,
                        "discrete_theta_bound": discrete_bound,
                        "continuous_tv_quadrature": continuous_tv,
                        "continuous_theta_bound": continuous_bound,
                        "quadrature_refinement_change": quadrature_change,
                        "max_discrete_identity_relative_error": max_discrete_identity_error,
                        "max_continuous_identity_absolute_error": max_continuous_identity_error,
                        "mask_parity_bias_direct": parity_bias,
                        "mask_parity_bias_poisson": poisson_bias})
    return {"status": "PASS", "theta_identity_cases": 24,
            "max_theta_relative_error": max_theta_relative_error,
            "arithmetic": "IEEE-754 Python floats; Gaussian sums truncated at 9 or 12 widths",
            "interpretation": "Finite numerical consistency checks; TV quadrature is not a certified integral",
            "parameter_cases": records}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="also write the JSON report to this path")
    args = parser.parse_args()
    report = {"schema_version": 1, "status": "PASS", "seed": SEED,
              "scope": "Finite exact algebra and floating-point identity checks, not evidence of asymptotic hardness.",
              "masking": check_masking(),
              "bases_frames_and_precision": check_bases_and_frames(),
              "smoothing": check_smoothing()}
    payload = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if args.output is not None:
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")


if __name__ == "__main__":
    main()
