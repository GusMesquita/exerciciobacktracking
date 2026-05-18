"""Backtracking para o problema das n-rainhas."""

from __future__ import annotations

from time import perf_counter

from backtracking.models import ExecutionStats, NQueensResult
from backtracking.utils import ensure_recursion_limit


def solve_n_queens_first(n: int) -> NQueensResult:
    """Retorna a primeira solucao encontrada para um tabuleiro n por n."""

    return _solve_n_queens(n, max_solutions=1)


def solve_n_queens_all(n: int) -> NQueensResult:
    """Retorna todas as solucoes para um tabuleiro n por n."""

    return _solve_n_queens(n, max_solutions=None)


def format_board(solution: tuple[int, ...]) -> str:
    """Formata uma solucao como tabuleiro textual."""

    n = len(solution)
    return "\n".join(
        " ".join("Q" if queen_col == col else "." for col in range(n))
        for queen_col in solution
    )


def is_valid_n_queens_solution(solution: tuple[int, ...]) -> bool:
    """Valida se uma solucao nao possui ataques entre rainhas."""

    n = len(solution)
    if len(set(solution)) != n:
        return False

    for row_a in range(n):
        for row_b in range(row_a + 1, n):
            same_diagonal = abs(row_a - row_b) == abs(solution[row_a] - solution[row_b])
            if same_diagonal:
                return False
    return True


def _solve_n_queens(n: int, max_solutions: int | None) -> NQueensResult:
    _validate_n(n)
    ensure_recursion_limit(n + 50)

    stats = ExecutionStats()
    solutions: list[tuple[int, ...]] = []
    placement = [-1] * n
    columns: set[int] = set()
    main_diagonals: set[int] = set()
    anti_diagonals: set[int] = set()
    start = perf_counter()

    def backtrack(row: int) -> bool:
        stats.iterations += 1
        stats.instructions += 2

        if row == n:
            stats.instructions += n
            solutions.append(tuple(placement))
            return max_solutions is not None and len(solutions) >= max_solutions

        for col in range(n):
            main_diagonal = row - col
            anti_diagonal = row + col
            stats.instructions += 5

            has_conflict = (
                col in columns
                or main_diagonal in main_diagonals
                or anti_diagonal in anti_diagonals
            )
            if has_conflict:
                stats.instructions += 1
                continue

            placement[row] = col
            columns.add(col)
            main_diagonals.add(main_diagonal)
            anti_diagonals.add(anti_diagonal)
            stats.instructions += 8

            if backtrack(row + 1):
                return True

            columns.remove(col)
            main_diagonals.remove(main_diagonal)
            anti_diagonals.remove(anti_diagonal)
            placement[row] = -1
            stats.instructions += 8

        return False

    backtrack(0)
    stats.elapsed_seconds = perf_counter() - start
    return NQueensResult(n, solutions, stats)


def _validate_n(n: int) -> None:
    if not isinstance(n, int):
        raise ValueError("n deve ser inteiro")
    if n < 2:
        raise ValueError("n deve ser maior ou igual a 2")
