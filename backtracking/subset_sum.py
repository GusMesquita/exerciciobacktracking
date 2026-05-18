"""Backtracking para o problema da soma dos subconjuntos."""

from __future__ import annotations

import random
from time import perf_counter

from backtracking.models import ExecutionStats, SubsetSumResult
from backtracking.utils import ensure_recursion_limit


def solve_subset_sum_first(values: list[int] | tuple[int, ...]) -> SubsetSumResult:
    """Retorna o primeiro subconjunto nao vazio com soma zero."""

    normalized = _normalize_values(values)
    ensure_recursion_limit(len(normalized) + 50)

    stats = ExecutionStats()
    subsets: list[tuple[int, ...]] = []
    chosen: list[int] = []
    start = perf_counter()

    def backtrack(index: int, current_sum: int) -> bool:
        stats.iterations += 1
        stats.instructions += 3

        if chosen and current_sum == 0:
            stats.instructions += len(chosen)
            subsets.append(tuple(chosen))
            return True

        stats.instructions += 1
        if index == len(normalized):
            return False

        value = normalized[index]
        stats.instructions += 2
        chosen.append(value)
        if backtrack(index + 1, current_sum + value):
            return True

        chosen.pop()
        stats.instructions += 2
        return backtrack(index + 1, current_sum)

    backtrack(0, 0)
    stats.elapsed_seconds = perf_counter() - start
    return SubsetSumResult(normalized, subsets, stats)


def solve_subset_sum_all(
    values: list[int] | tuple[int, ...],
    node_limit: int | None = None,
) -> SubsetSumResult:
    """Retorna todos os subconjuntos nao vazios com soma zero."""

    normalized = _normalize_values(values)
    ensure_recursion_limit(len(normalized) + 50)

    stats = ExecutionStats()
    subsets: list[tuple[int, ...]] = []
    chosen: list[int] = []
    start = perf_counter()

    def backtrack(index: int, current_sum: int) -> bool:
        stats.iterations += 1
        stats.instructions += 3

        if node_limit is not None and stats.iterations > node_limit:
            stats.stopped_by_limit = True
            return True

        stats.instructions += 1
        if index == len(normalized):
            if chosen and current_sum == 0:
                stats.instructions += len(chosen)
                subsets.append(tuple(chosen))
            return False

        value = normalized[index]
        stats.instructions += 2
        chosen.append(value)
        if backtrack(index + 1, current_sum + value):
            return True

        chosen.pop()
        stats.instructions += 2
        return backtrack(index + 1, current_sum)

    backtrack(0, 0)
    stats.elapsed_seconds = perf_counter() - start
    return SubsetSumResult(normalized, subsets, stats)


def generate_large_set(size: int, seed: int = 0) -> list[int]:
    """Gera conjunto grande com pelo menos uma solucao curta garantida."""

    if size < 50 or size > 1000:
        raise ValueError("o tamanho deve estar entre 50 e 1000")

    generator = random.Random(seed)
    values = [generator.randint(-1000, 1000) for _ in range(size)]
    value = generator.randint(1, 1000)
    values[0] = value
    values[1] = -value
    return values


def _normalize_values(values: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(values)
    if any(not isinstance(value, int) for value in normalized):
        raise ValueError("todos os valores devem ser inteiros")
    return normalized
