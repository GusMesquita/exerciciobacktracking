"""Funcoes auxiliares pequenas usadas pelos modulos."""

from __future__ import annotations

import sys


def ensure_recursion_limit(required_depth: int) -> None:
    if sys.getrecursionlimit() < required_depth:
        sys.setrecursionlimit(required_depth)


def format_ms(seconds: float) -> str:
    return f"{seconds * 1000:.3f} ms"


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join("---" for _ in headers) + " |"
    row_lines = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header_line, separator, *row_lines])
