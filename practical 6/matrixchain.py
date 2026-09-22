import time


def matrix_chain_order(dims):
    n = len(dims) - 1  
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # chain_len is the length of the chain being solved
    for chain_len in range(2, n + 1):
        for i in range(1, n - chain_len + 2):
            j = i + chain_len - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = (m[i][k] + m[k + 1][j]
                        + dims[i - 1] * dims[k] * dims[j])
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def get_optimal_parenthesization(s, i, j):
    if i == j:
        return f"A{i}"
    else:
        k = s[i][j]
        left = get_optimal_parenthesization(s, i, k)
        right = get_optimal_parenthesization(s, k + 1, j)
        return f"({left} x {right})"


def get_dimensions_from_user():
    while True:
        try:
            n = int(input("Enter the number of matrices: "))
            if n < 1:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    dims = []
    print(f"\nEnter dimensions for {n} matrices.")
    print("Matrix i has dimension dims[i-1] x dims[i].")
    print(f"So you must enter {n + 1} numbers (p0, p1, p2, ..., p{n}).\n")

    for i in range(n + 1):
        while True:
            try:
                val = int(input(f"Enter p{i}: "))
                if val <= 0:
                    print("Dimension must be a positive integer.")
                    continue
                dims.append(val)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    return dims


def main():
    print("=" * 55)
    print("      MATRIX CHAIN MULTIPLICATION (DP Approach)")
    print("=" * 55)

    dims = get_dimensions_from_user()
    n = len(dims) - 1

    print("\nMatrix dimensions entered:")
    for i in range(1, n + 1):
        print(f"  A{i}: {dims[i - 1]} x {dims[i]}")

    # --- measure execution time of the core algorithm ---
    start_time = time.perf_counter()
    m, s = matrix_chain_order(dims)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    optimal_parens = get_optimal_parenthesization(s, 1, n)

    print("\n" + "-" * 55)
    print("RESULTS")
    print("-" * 55)
    print(f"Minimum number of scalar multiplications : {m[1][n]}")
    print(f"Optimal parenthesization                 : {optimal_parens}")

    print("\nDP Cost Table (m[i][j]):")
    header = "      " + "".join(f"{j:>8}" for j in range(1, n + 1))
    print(header)
    for i in range(1, n + 1):
        row = f"i={i:<3}"
        for j in range(1, n + 1):
            row += f"{m[i][j]:>8}" if j >= i else f"{'-':>8}"
        print(row)

    print("\n" + "-" * 55)
    print("PERFORMANCE")
    print("-" * 55)
    print("Time Complexity  : O(n^3)")
    print("Space Complexity : O(n^2)")
    print(f"Execution Time   : {execution_time:.8f} seconds")
    print("-" * 55)


if __name__ == "__main__":
    main()