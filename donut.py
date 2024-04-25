import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D', 'others']
sizes = [10, 20, 30, 10, sum([10, 5, 5, 3, 3, 4])]


def donut_plot(labels, sizes):

    # Create a circle for the center of the plot
    plt.figure(figsize=(7, 7))
    plt.pie([100], colors='white', radius=0.5)

    # Create a donut plot
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
            colors=['red', 'green', 'blue', 'yellow', 'grey'],
            wedgeprops=dict(width=0.3, edgecolor='w'))

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')

    # Add a circle at the center to make it look like a donut
    circle = plt.Circle((0, 0), 0.35, fc='white')
    plt.gca().add_artist(circle)

    # This line adds the white circle to the current axes.
    plt.title('Donut Plot', y=1, x=0.5, color='red')

    plt.savefig('donut_plot.png', dpi=300, bbox_inches='tight')

    plt.show()


# Call the function
donut_plot(labels, sizes)
