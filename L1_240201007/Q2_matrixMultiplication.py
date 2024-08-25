from typing import Any, Tuple


# This is static function, which takes rows and columns from user and returns a tuple(rows, cols).
def get_matrix_dimensions(matrix_name: str) -> tuple[int, int]:
    while True:
        try:
            print(f"{'---'*20}")
            row = int(input(f"Enter the number of rows for the {matrix_name} matrix: "))
            column = int(input(f"Enter the number of columns for the {matrix_name} matrix: "))
            if row > 0 and column > 0:
                return row, column
            else:
                print("Rows and columns must be positive integers. Please try again.")
        except ValueError:
            print("Invalid input. Please enter valid integers for rows and columns.")


class Matrix:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.data = list()

    def input_matrix(self) -> None:
        print(f"Taking input for {self.rows}x{self.cols} matrix:")
        for i in range(self.rows):
            while True:
                try:
                    row = list(map(float, input(f"Enter row {i + 1} elements separated by space: ").split()))
                    if len(row) == self.cols:
                        self.data.append(row)
                        break
                    else:
                        print(f"Error: You need to enter exactly {self.cols} elements for each row.")
                except ValueError:
                    print("Invalid Input! \nPlease enter NUMERIC data")

    # Over-loading __mul__ method to change the behaviour of multiplication operator ('*').
    def __mul__(self, other) -> Any:
        if self.cols != other.rows:
            print("Error: Number of columns in the first matrix must equal the number of rows in the second matrix.")
            return None

        # Giving dimensions to resultant matrix (rows of matrix_A x columns of matrix_B)
        resultant_matrix = Matrix(self.rows, other.cols)
        # Initializing the resultant matrix with zeros
        resultant_matrix.data = [[0 for _ in range(other.cols)] for _ in range(self.rows)]

        # Performing matrix multiplication
        for i in range(self.rows):
            for j in range(other.cols):
                resultant_matrix.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))

        return resultant_matrix

    #  over-loading __str__ method to print matrix in readable format.
    def __str__(self):
        matrix_str = "\n".join([" ".join(map(str, row)) for row in self.data])
        return matrix_str


if __name__ == "__main__":
    # Get dimensions for the first matrix
    rows_A, cols_A = get_matrix_dimensions("first")
    
    # Creating object of Matrix class
    matrix_A = Matrix(rows_A, cols_A)

    # Taking input (matrix elements) from user  
    matrix_A.input_matrix()

    # Get dimensions for the second matrix
    rows_B, cols_B = get_matrix_dimensions("second")
    matrix_B = Matrix(rows_B, cols_B)
    
    # Taking matrix elements from user
    matrix_B.input_matrix()

    # Multiply matrices
    try:
        result = matrix_A * matrix_B
        print("\nResult of matrix multiplication:")
        print(result)
    except ValueError as e:
        print(e)
