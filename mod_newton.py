import numpy as np

x_0 = np.array([0.0, 0.0])

A_inv = np.array([[0.25, 1], [-0.25, 0]])

F_0 = np.array([4.0, 0.0])

epsilon = 1e-6

def F(x):
    x1, x2 = x
    return np.array([
        np.cos(x1) - 4 * x2 + 3,
        x1 + np.sin(x2)
    ])

x_i = x_0
F_i = F_0
iteration = 0

while True:
    x_next = x_i - A_inv @ F_i

    condition_number = np.max(np.abs(x_next - x_i))

    comparison_sign = ">=" if condition_number > epsilon else "<="

    print(f"Ітерація {iteration + 1}:")
    print(f"x_{iteration + 1} = [{x_next[0]:.8f}, {x_next[1]:.8f}]")
    print(f"||x_{iteration + 1} - x_{iteration}|| = {condition_number:.8f}")
    print(f"Перевірка: {condition_number:.8f} {comparison_sign} {epsilon:.8f}")
    print("------------------------")

    if condition_number < epsilon:
        break

    x_i = x_next
    F_i = F(x_i)
    iteration += 1

print("\nВідповідь:")
print(f"x1 = {x_next[0]:.8f}")
print(f"x2 = {x_next[1]:.8f}")
