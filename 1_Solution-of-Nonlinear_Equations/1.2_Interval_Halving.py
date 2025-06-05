from startup import *

def interval_halving(function, tolerance, x_1, x_2):
    """
    Takes the interval [x_1, x_2] and finds a zero of any function in between it. Needs to have an odd number of zeroes to work!
    """
    # Check that a root exists in the interval
    if function(x_1) * function(x_2) > 0:
        raise ValueError("No root found in the interval [x_1, x_2]")

    midpoints = []  # Store midpoints for plotting

    # Main Body, while loop checks how precise the interval is.
    while abs(x_2 - x_1) >= tolerance:
        # If too imprecise, halve the interval.
        x_new = 0.5 * (x_1 + x_2)
        midpoints.append(x_new)  # Track midpoint for this iteration

        # Checks which side of the interval has a sign change and resets the boundaries.
        if function(x_new) * function(x_1) > 0:
            x_1 = x_new
        else:
            x_2 = x_new
    # returns the midpoint for the interval estimate and the list of midpoints.
    return 0.5 * (x_1 + x_2), midpoints  

# Any function
def function(x):
    return x**3 + x**2 - 3*x - 3

########################################################################################

x_1, x_2 = 1, 2
root, midpoints = interval_halving(function, 1e-6, 1, 2)
print("Root:", root)
print("f(root):", function(root))

# Plot the function and the vertical dotted lines
x_vals = np.linspace(x_1, x_2, 1000)
y_vals = function(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")

for i, x_mid in enumerate(midpoints):
    plt.axvline(x_mid, color='gray', linestyle=':', alpha=0.6)
    plt.text(x_mid, 0, f"Iter {i}", rotation=90, verticalalignment='bottom', fontsize=8, color='blue')

plt.axhline(0, color='black', linewidth=0.8)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Function with Interval Halving Midpoints")
plt.legend()
plt.grid(True)
plt.show()
