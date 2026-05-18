"""Geracao do relatorio em Markdown."""

from __future__ import annotations

from pathlib import Path

from backtracking.n_queens import format_board, solve_n_queens_all, solve_n_queens_first
from backtracking.subset_sum import (
    generate_large_set,
    solve_subset_sum_all,
    solve_subset_sum_first,
)
from backtracking.utils import format_ms, markdown_table


def build_report() -> str:
    """Monta o relatorio completo da atividade."""

    n_first_rows = []
    n_all_rows = []
    for n in range(4, 11):
        first = solve_n_queens_first(n)
        all_solutions = solve_n_queens_all(n)
        n_first_rows.append(
            [
                str(n),
                str(len(first.solutions)),
                str(first.stats.iterations),
                str(first.stats.instructions),
                format_ms(first.stats.elapsed_seconds),
            ]
        )
        n_all_rows.append(
            [
                str(n),
                str(len(all_solutions.solutions)),
                str(all_solutions.stats.iterations),
                str(all_solutions.stats.instructions),
                format_ms(all_solutions.stats.elapsed_seconds),
            ]
        )

    subset_rows = []
    for values in [
        [-7, -3, -2, 5, 8],
        [1, 2, 3, 4, 5, 10],
        [-5, 2, 3, -1, 1],
    ]:
        first = solve_subset_sum_first(values)
        all_subsets = solve_subset_sum_all(values)
        subset_rows.append(
            [
                str(values),
                _format_subsets(first.subsets),
                str(len(all_subsets.subsets)),
                _format_subsets(all_subsets.subsets),
                str(first.stats.iterations),
                str(all_subsets.stats.iterations),
                format_ms(first.stats.elapsed_seconds),
                format_ms(all_subsets.stats.elapsed_seconds),
            ]
        )

    large_rows = []
    for size in [50, 100, 500, 1000]:
        values = generate_large_set(size, seed=size)
        first = solve_subset_sum_first(values)
        limited_all = solve_subset_sum_all(values, node_limit=200_000)
        large_rows.append(
            [
                str(size),
                _format_subsets(first.subsets),
                str(first.stats.iterations),
                format_ms(first.stats.elapsed_seconds),
                str(limited_all.stats.iterations),
                str(len(limited_all.subsets)),
                "sim" if limited_all.stats.stopped_by_limit else "nao",
                format_ms(limited_all.stats.elapsed_seconds),
            ]
        )

    n7 = solve_n_queens_first(7)
    n7_board = format_board(n7.solutions[0]) if n7.solutions else "sem solucao"

    return "\n".join(
        [
            "# Resolucao completa da atividade de Backtracking",
            "",
            "## Resumo",
            "",
            "- As duas atividades foram resolvidas com backtracking.",
            "- As tabelas mostram chamadas recursivas, instrucoes estimadas e tempo de execucao.",
            "",
            "## Problema das n-rainhas",
            "",
            "A solucao coloca uma rainha por linha e usa conjuntos para controlar colunas e diagonais ocupadas.",
            "",
            "### Primeira solucao para n = 7",
            "",
            "```text",
            n7_board,
            "```",
            "",
            "### Complexidade",
            "",
            "- Primeira solucao: O(n!) no pior caso; espaco O(n).",
            "- Todas as solucoes: O(n! + S*n), onde S e o total de solucoes; espaco O(n + S*n).",
            "",
            "### Resultados: n-rainhas, primeira solucao",
            "",
            markdown_table(
                ["n", "solucoes retornadas", "iteracoes", "instrucoes", "tempo"],
                n_first_rows,
            ),
            "",
            "### Resultados: n-rainhas, todas as solucoes",
            "",
            markdown_table(
                ["n", "total de solucoes", "iteracoes", "instrucoes", "tempo"],
                n_all_rows,
            ),
            "",
            "## Problema da soma dos subconjuntos",
            "",
            "A busca decide para cada elemento se ele entra ou nao no subconjunto.",
            "",
            "### Complexidade",
            "",
            "- Primeira solucao: O(2^n) no pior caso; espaco O(n).",
            "- Todas as solucoes: O(2^n + K*n), onde K e o total de subconjuntos retornados; espaco O(n + K*n).",
            "",
            "### Resultados: exemplos da atividade",
            "",
            markdown_table(
                [
                    "conjunto",
                    "primeira solucao",
                    "qtd todas",
                    "todas as solucoes",
                    "iter. primeira",
                    "iter. todas",
                    "tempo primeira",
                    "tempo todas",
                ],
                subset_rows,
            ),
            "",
            "### Resultados: conjuntos grandes gerados",
            "",
            markdown_table(
                [
                    "tamanho",
                    "primeira solucao",
                    "iter. primeira",
                    "tempo primeira",
                    "iter. todas limit.",
                    "solucoes parciais",
                    "parou no limite",
                    "tempo todas limit.",
                ],
                large_rows,
            ),
            "",
            "### Nota",
            "",
            "Nos conjuntos grandes, a busca por todas as solucoes foi limitada a 200000 chamadas para evitar execucoes muito longas.",
            "",
        ]
    )


def write_report(path: str | Path = "RESULTADOS.md") -> Path:
    """Escreve o relatorio em um arquivo Markdown e retorna o caminho."""

    output_path = Path(path)
    output_path.write_text(build_report(), encoding="utf-8")
    return output_path


def _format_subsets(subsets: list[tuple[int, ...]]) -> str:
    if not subsets:
        return "-"
    return "; ".join(str(list(subset)) for subset in subsets[:5])
