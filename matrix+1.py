x = [[3, 2, 5, 6], [1, 2, 3, 4], [7, 6, 5, 4]]
y = [[1, 1, 1, 2], [2, 2, 2, 2], [1, 2, 3, 1]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))


matrix_1 = Matrix(x)
matrix_2 = Matrix(y)
print(f"Matrix_1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix_2\n{matrix_2}\n{'-' * 20}")
print(f"matrix_1 + matrix_2\n{matrix_1 + matrix_2}")