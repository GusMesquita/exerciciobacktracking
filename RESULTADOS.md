# Resolucao da atividade de Backtracking
# Aluno: Gustavo Caldeira de Mesquita

## Resumo

- As duas atividades foram resolvidas com backtracking.
- As tabelas mostram chamadas recursivas, instrucoes estimadas e tempo de execucao.

## Problema das n-rainhas

A solucao coloca uma rainha por linha e usa conjuntos para controlar colunas e diagonais ocupadas.

### Primeira solucao para n = 7

```text
Q . . . . . .
. . Q . . . .
. . . . Q . .
. . . . . . Q
. Q . . . . .
. . . Q . . .
. . . . . Q .
```

### Complexidade

- Primeira solucao: O(n!) no pior caso; espaco O(n).
- Todas as solucoes: O(n! + S*n), onde S e o total de solucoes; espaco O(n + S*n).

### Resultados: n-rainhas, primeira solucao

| n | solucoes retornadas | iteracoes | instrucoes | tempo |
| --- | --- | --- | --- | --- |
| 4 | 1 | 9 | 266 | 0.017 ms |
| 5 | 1 | 6 | 142 | 0.006 ms |
| 6 | 1 | 32 | 1513 | 0.044 ms |
| 7 | 1 | 10 | 358 | 0.012 ms |
| 8 | 1 | 114 | 7123 | 0.212 ms |
| 9 | 1 | 42 | 2634 | 0.077 ms |
| 10 | 1 | 103 | 7516 | 0.212 ms |

### Resultados: n-rainhas, todas as solucoes

| n | total de solucoes | iteracoes | instrucoes | tempo |
| --- | --- | --- | --- | --- |
| 4 | 2 | 17 | 642 | 0.022 ms |
| 5 | 10 | 54 | 2273 | 0.072 ms |
| 6 | 4 | 153 | 7974 | 0.235 ms |
| 7 | 40 | 552 | 31153 | 1.384 ms |
| 8 | 92 | 2057 | 130010 | 3.953 ms |
| 9 | 352 | 8394 | 580119 | 17.574 ms |
| 10 | 724 | 35539 | 2700288 | 81.118 ms |

## Problema da soma dos subconjuntos

A busca decide para cada elemento se ele entra ou nao no subconjunto.

### Complexidade

- Primeira solucao: O(2^n) no pior caso; espaco O(n).
- Todas as solucoes: O(2^n + K*n), onde K e o total de subconjuntos retornados; espaco O(n + K*n).

### Resultados: exemplos da atividade

| conjunto | primeira solucao | qtd todas | todas as solucoes | iter. primeira | iter. todas | tempo primeira | tempo todas |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [-7, -3, -2, 5, 8] | [-3, -2, 5] | 1 | [-3, -2, 5] | 36 | 63 | 0.018 ms | 0.023 ms |
| [1, 2, 3, 4, 5, 10] | - | 0 | - | 127 | 127 | 0.040 ms | 0.066 ms |
| [-5, 2, 3, -1, 1] | [-5, 2, 3] | 3 | [-5, 2, 3, -1, 1]; [-5, 2, 3]; [-1, 1] | 4 | 63 | 0.002 ms | 0.037 ms |

### Resultados: conjuntos grandes gerados

| tamanho | primeira solucao | iter. primeira | tempo primeira | iter. todas limit. | solucoes parciais | parou no limite | tempo todas limit. |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 50 | [441, -441] | 3 | 0.002 ms | 200001 | 15 | sim | 65.883 ms |
| 100 | [699, -699] | 3 | 0.002 ms | 200001 | 0 | sim | 65.545 ms |
| 500 | [464, -464] | 3 | 0.002 ms | 200001 | 0 | sim | 66.999 ms |
| 1000 | [613, -613] | 3 | 0.002 ms | 200001 | 0 | sim | 67.312 ms |

### Nota

Nos conjuntos grandes, a busca por todas as solucoes foi limitada a 200000 chamadas para evitar execucoes muito longas.
