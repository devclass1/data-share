import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 6]

# Line Plot
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st plot
plt.plot(x, y, marker='o', color='blue')
plt.title("Basic Line Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

# Bar Plot
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
bars = plt.bar(["A", "B", "C", "D", "E"], y, color=['red', 'green', 'blue', 'orange', 'purple'])
plt.title("Basic Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.tight_layout()
plt.show()
