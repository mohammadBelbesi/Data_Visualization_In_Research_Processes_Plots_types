import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def pairPlot():

    # Generate sample data
    np.random.seed(0)
    data = pd.DataFrame(np.random.randn(100, 4), columns=['A', 'B', 'C', 'D'])

    # Add a categorical column
    data['Category'] = np.random.choice(['X'], 100)

    # Define marker styles for different categories
    markers = {'X': 'o', 'Y': 's', 'Z': 'D'}

    # Pairplot with scatter plots only
    fig, axes = plt.subplots(4, 4, figsize=(10, 12))

    for i, col1 in enumerate(data.columns[:-1]):
        for j, col2 in enumerate(data.columns[:-1]):
            if (i, j) == (0, 0) or (i, j) == (1, 1) or \
               (i, j) == (2, 2) or (i, j) == (3, 3):  # Check if diagonal
                axes[i, j].hist(data[col1], color='skyblue', alpha=0.7)
            else:
                for category, group in data.groupby('Category'):
                    axes[i, j].scatter(group[col2], group[col1],
                                       marker=markers[category],
                                       label=category, c='blue', alpha=0.3)

            # Remove right and top spines
            axes[i, j].spines['right'].set_visible(False)
            axes[i, j].spines['top'].set_visible(False)

    # Add legend to the last subplot
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper right')

    # Set titles and labels
    for i, col in enumerate(data.columns[:-1]):
        axes[-1, i].set_xlabel(col)
        # Set rotation to 0 for y-labels
        axes[i, 0].set_ylabel(col, rotation=0)

    # Set overall title
    fig.suptitle('Pairplot of Sample Data', y=1.02, fontsize=18)

    # Adjust layout
    plt.tight_layout()

    plt.savefig('pair_plot.png', dpi=300, bbox_inches='tight')

    # Show plot
    plt.show()


pairPlot()
