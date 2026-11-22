def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []

    means = []

    if mode == 'row':
        for row in matrix:
            means.append(sum(row) / len(row))
    elif mode == 'column':
        rows = len(matrix)
        cols = len(matrix[0])
        for col in range(cols):
            col_sum = 0
            for row in range(rows):
                col_sum += matrix[row][col]
            means.append(col_sum / rows)
    else:
        raise ValueError("Mode must be 'row' or 'column'")
        
    return means