"""Modelos compartilhados pelas solucoes."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ExecutionStats:
    """Metricas coletadas durante uma busca por backtracking."""

    iterations: int = 0
    instructions: int = 0
    elapsed_seconds: float = 0.0
    stopped_by_limit: bool = False


@dataclass
class NQueensResult:
    n: int
    solutions: list[tuple[int, ...]]
    stats: ExecutionStats


@dataclass
class SubsetSumResult:
    values: tuple[int, ...]
    subsets: list[tuple[int, ...]]
    stats: ExecutionStats
