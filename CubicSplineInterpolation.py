import numpy as np
import scipy.interpolate as spi
import matplotlib.pyplot as plt

def compare_cubic_splines(x, y, func):
    # Generate finer grid for plotting
    x_plot = np.linspace(min(x), max(x), 1000)
    y_true = func(x_plot)

    # Natural Cubic Spline Interpolation
    spline_natural = spi.CubicSpline(x, y, bc_type='natural')
    natural_coeffs = [(spline_natural.c[i], spline_natural.c[i+1], spline_natural.c[i+2], spline_natural.c[i+3]) for i in range(len(spline_natural.c) - 3)]

    # Clamped Cubic Spline Interpolation
    deriv_value = np.array([func(x[0], 1), func(x[-1], 1)])  # Derivative values at endpoints
    spline_clamped = spi.CubicSpline(x, y, bc_type=((1, deriv_value[0]), (1, deriv_value[1])))
    clamped_coeffs = [(spline_clamped.c[i], spline_clamped.c[i+1], spline_clamped.c[i+2], spline_clamped.c[i+3]) for i in range(len(spline_clamped.c) - 3)]

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_true, label='True Function', color='black')
    plt.plot(x_plot, spline_natural(x_plot), label='Natural Spline', linestyle='-', color='blue')
    plt.plot(x_plot, spline_clamped(x_plot), label='Clamped Spline', linestyle='-', color='red')
    plt.scatter(x, y, label='Nodes', color='green')
    plt.title('Comparison of Cubic Spline Interpolations')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    return natural_coeffs, clamped_coeffs

# Manual input of nodes (must change if you change the function)
x_nodes = np.array([0, 1, 3])
y_nodes = np.array([6, 0, -0])

# Define the function (can change the function here)
def my_function(x, order=0):
    if order == 0:
        return x**5 - 4*x**4 + 14*x**2 - 17*x + 6
    elif order == 1:
        return 5*x**4 - 16*x**3 + 28*x - 17  # Derivative of my_function

# Compare cubic spline interpolations and retrieve coefficients
natural_coeffs, clamped_coeffs = compare_cubic_splines(x_nodes, y_nodes, my_function)

# Output coefficients
print("Natural Cubic Spline Coefficients:")
for i, coef in enumerate(natural_coeffs):
    print(f"Segment {i+1}: {coef}")

print("\nClamped Cubic Spline Coefficients:")
for i, coef in enumerate(clamped_coeffs):
    print(f"Segment {i+1}: {coef}")
