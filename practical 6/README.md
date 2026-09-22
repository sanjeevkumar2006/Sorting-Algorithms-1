# Matrix Chain Multiplication

This is a simple Python program that finds the **best (cheapest) order** to multiply a chain of matrices together.

When you multiply many matrices together, the *order* you multiply them in changes how many total calculations (multiplications) it takes — even though the final answer is the same.

This program figures out the order that needs the **fewest multiplications**.

1. Asks you how many matrices you have.
2. Asks you for the dimensions of each matrix.
3. Calculates:
   - The minimum number of multiplications needed
   - The best order to multiply the matrices (called the "optimal parenthesization")
   - A table showing the cost for every possible combination
4. Shows how long the calculation took (execution time) and how the algorithm scales (time complexity).

For a small number of matrices, the order doesn't matter much. But for large chains, choosing the wrong order can be thousands of times slower. This program automatically finds the fastest order for you.
