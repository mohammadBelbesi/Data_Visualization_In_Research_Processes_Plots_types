import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D', 'others']
sizes = [10, 20, 30, 10, sum([10, 5, 5, 3, 3, 4])]


def pie_plot(labels, sizes):

    # Create a pie plot
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
            colors=['red', 'green', 'blue', 'yellow', 'grey'])

    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')

    plt.title('Pie Plot', y=1, x=0.5, color='red')

    plt.savefig('pie_plot.png', dpi=300, bbox_inches='tight')

    plt.show()


pie_plot(labels, sizes)
