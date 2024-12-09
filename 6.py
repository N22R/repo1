import numpy as np

class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
        self.n = self.data.shape[0]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def calculate_fi(self):
        fi = []
        for i in range(self.n):
            sum_elements = 0
            count = 0
            for j in range(self.n):
                if i + j < self.n - 1:
                    sum_elements += self.data[j][i]
                    count += 1
            fi.append(float(sum_elements / count) if count > 0 else 0.0)
        return fi

    def calculate_F(self, fi):
        result = 1
        for val in fi:
            result *= val
        return result

    def insertion_sort_desc(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key > arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def sort_rows(self):
        self.data = np.array([self.insertion_sort_desc(row) for row in self.data])
        return self.data


matrix = Matrix([
    [12, 46, -23, 72, -5],
    [59, 7, -8, 0, 67],
    [7, -8, -4, -97, -55],
    [77, -1, -5, 34, -8],
    [0, 22, 27, 24, 24]
])


print("Початкова матриця:")
print(matrix)


matrix.sort_rows()


fi_values = matrix.calculate_fi()
F_value = matrix.calculate_F(fi_values)

print("\nВідсортована матриця:")
print(matrix)

print("\nЗначення fi(aij) для кожного рядка:")
print(fi_values)

print("\nЗначення F(fi(aij)):")
print(F_value)
