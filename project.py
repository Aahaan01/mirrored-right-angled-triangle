print("Mirrored Triangle of Stars (*):")
n = int(input("Enter the number of rows: "))

print("\nMirrored Right-Angled Triangle:")
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
