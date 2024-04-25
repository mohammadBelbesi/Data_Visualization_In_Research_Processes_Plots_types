import matplotlib.pyplot as plt
import numpy as np


def points():

    # Generate sample data
    np.random.seed(42)
    num_points = 2000

    # Dataset 1
    x1 = np.random.normal(loc=0, scale=1, size=num_points)
    y1 = np.random.normal(loc=0, scale=1, size=num_points)

    # Plotting
    plt.figure(figsize=(10, 6))

    # Scatter plot for Dataset 1 with only the ring
    plt.scatter(x1, y1, facecolor='none', edgecolor='blue', label='Dataset 1')

    # Add labels and title
    plt.xlabel('X-axis', labelpad=20)
    plt.ylabel('Y-axis', rotation=0, labelpad=20)
    plt.title('Scatter Plot with Ring Points')

    # Remove right and top spines
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)

    # Add legend
    plt.legend(frameon=False)

    # Show plot
    plt.grid(False)
    plt.tight_layout()

    plt.savefig('points_plot.png', dpi=300, bbox_inches='tight')

    plt.show()


points()
