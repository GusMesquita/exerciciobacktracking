"""Ponto de entrada da resolucao da atividade de backtracking."""

import argparse

from backtracking.n_queens import format_board, solve_n_queens_first
from backtracking.report import build_report, write_report
from backtracking.subset_sum import solve_subset_sum_first
from backtracking.tests import run_tests


def main() -> None:
    parser = argparse.ArgumentParser(description="Resolucao de backtracking")
    parser.add_argument("--test", action="store_true", help="executa testes de corretude")
    parser.add_argument("--demo", action="store_true", help="mostra exemplos de execucao")
    parser.add_argument("--report", action="store_true", help="imprime o relatorio completo")
    parser.add_argument(
        "--write-report",
        nargs="?",
        const="RESULTADOS.md",
        metavar="ARQUIVO",
        help="escreve o relatorio em Markdown; padrao: RESULTADOS.md",
    )
    args = parser.parse_args()

    if args.test:
        run_tests()
        print("todos os testes passaram")
        return

    if args.write_report:
        output_path = write_report(args.write_report)
        print(f"relatorio escrito em {output_path}")
        return

    if args.report:
        print(build_report())
        return

    if args.demo:
        n_queens = solve_n_queens_first(7)
        print("Primeira solucao para 7-rainhas:")
        print(format_board(n_queens.solutions[0]))
        print()
        subset = solve_subset_sum_first([-7, -3, -2, 5, 8])
        print("Primeiro subconjunto com soma zero:")
        print(subset.subsets[0])
        return

    parser.print_help()


if __name__ == "__main__":
    main()
