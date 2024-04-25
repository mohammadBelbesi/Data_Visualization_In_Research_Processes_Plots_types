import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def denisty():

    # Generate synthetic data for two groups
    np.random.seed(42)
    # Generate data for group 1
    group1 = np.random.normal(loc=0, scale=1, size=1000)
    # Generate data for group 2
    group2 = np.random.normal(loc=2, scale=1.5, size=1000)

    # Set the background style
    sns.set_style("white")  # Change background style to white with grid lines
    # darkgrid, whitegrid, dark, white, ticks

    # Create a density plot
    plt.figure(figsize=(10, 6))  # Set the figure size
    # Plot density for group 1
    sns.kdeplot(group1, fill=True, color='blue', label='Group 1')
    # Plot density for group 2
    sns.kdeplot(group2, fill=True, color='orange', label='Group 2')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Density', rotation=0, labelpad=20)
    plt.title('Density Plot Example')

    # Customize legend
    plt.legend(title='Groups', loc='upper right',
               fontsize='large', frameon=False)

    # Customize tick marks and labels
    plt.xticks([], fontsize=12)  # Set font size of x-axis tick labels
    plt.yticks(fontsize=12)  # Set font size of y-axis tick labels

    # Remove right and top spines
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    # Save as PNG image with high resolution (300 dpi)
    plt.savefig('density_plot.png', dpi=300, bbox_inches='tight')
    # Show plot
    plt.show()


denisty()
