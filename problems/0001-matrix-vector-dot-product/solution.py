def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if not a:
        return -1

    for row in a:
        if len(row) != len(b):
            return -1

    result = []
    for row in a:
        row_total = 0
        for i in range(len(b)):
            row_total += row[i] * b[i]
        result.append(row_total)
    return result