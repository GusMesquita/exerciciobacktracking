"""Solucoes de backtracking para a atividade."""

from backtracking.n_queens import format_board, solve_n_queens_all, solve_n_queens_first
from backtracking.report import build_report, write_report
from backtracking.subset_sum import (
    generate_large_set,
    solve_subset_sum_all,
    solve_subset_sum_first,
)

__all__ = [
    "build_report",
    "format_board",
    "generate_large_set",
    "solve_n_queens_all",
    "solve_n_queens_first",
    "solve_subset_sum_all",
    "solve_subset_sum_first",
    "write_report",
]
