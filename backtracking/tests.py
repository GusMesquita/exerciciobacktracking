"""Testes simples de corretude da atividade."""

from __future__ import annotations

import tempfile
from pathlib import Path

from backtracking.n_queens import (
    is_valid_n_queens_solution,
    solve_n_queens_all,
    solve_n_queens_first,
)
from backtracking.report import write_report
from backtracking.subset_sum import (
    generate_large_set,
    solve_subset_sum_all,
    solve_subset_sum_first,
)


def run_tests() -> None:
    n4_first = solve_n_queens_first(4)
    assert len(n4_first.solutions) == 1
    assert is_valid_n_queens_solution(n4_first.solutions[0])

    n4_all = solve_n_queens_all(4)
    assert len(n4_all.solutions) == 2
    assert all(is_valid_n_queens_solution(solution) for solution in n4_all.solutions)

    assert solve_n_queens_all(2).solutions == []
    assert solve_n_queens_all(3).solutions == []

    try:
        solve_n_queens_first(1)
    except ValueError:
        pass
    else:
        raise AssertionError("n < 2 deve ser rejeitado")

    subset = solve_subset_sum_first([-7, -3, -2, 5, 8])
    assert len(subset.subsets) == 1
    assert sum(subset.subsets[0]) == 0
    assert subset.subsets[0]

    all_subsets = solve_subset_sum_all([-5, 2, 3, -1, 1])
    expected = {(-5, 2, 3), (-5, 2, 3, -1, 1), (-1, 1)}
    assert set(all_subsets.subsets) == expected

    assert solve_subset_sum_all([1, 2, 3, 4, 5, 10]).subsets == []

    large = generate_large_set(50, seed=42)
    assert len(large) == 50
    assert large[0] + large[1] == 0

    with tempfile.TemporaryDirectory() as directory:
        output_path = write_report(Path(directory) / "RESULTADOS.md")
        content = output_path.read_text(encoding="utf-8")
        assert output_path.exists()
        assert "# Resolucao completa" in content
        assert "Problema das n-rainhas" in content
        assert "Problema da soma dos subconjuntos" in content
