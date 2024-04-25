import matplotlib.pyplot as plt


def bar():
    # Sample data
    categories = [' A', ' B', ' C', ' D', ' E',
                  ' F', ' G', ' H', ' I', ' J']
    values = [25, 40, 30, 35, 20, 10, 15, 11, 14, 7]

    # Sort categories and values based on values
    sorted_data = sorted(zip(categories, values), key=lambda x: x[1],
                         reverse=True)

    # Extract top 5 categories and values
    top_categories, top_values = zip(*sorted_data[:5])

    # Sum the remaining values for "others"
    others_value = sum(value for _, value in sorted_data[5:])

    # Create new categories list including "others" 'the highest in top'
    new_categories = list(top_categories[::-1]) + ['Others']
    new_values = list(top_values[::-1]) + [others_value]

    # Create new categories list including "others" ''the highest in bottom''
    # new_categories = ['Others'] + list(top_categories)
    # new_values = [others_value] + list(top_values)

    # Create a horizontal bar chart
    plt.figure(figsize=(10, 6))  # Set the figure size
    bars = plt.barh(new_categories, new_values, color='skyblue')

    # Add data labels next to each bar
    for bar, value in zip(bars, new_values):
        plt.text(value, bar.get_y() + bar.get_height() / 2,
                 value, va='center', ha='left')

    # Add labels and title
    plt.xlabel('Values')
    plt.ylabel('Categories', rotation=0, labelpad=20)
    plt.title('Bar Chart Example')

    # Remove x-axis ticks
    plt.xticks([])

    # Customize y-axis ticks rotation
    # plt.yticks(rotation=45)

    # Remove right and top spines
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().yaxis.set_label_coords(-0.05, 1.05)

    plt.savefig('bar_plot.png', dpi=300, bbox_inches='tight')
    # Show plot
    plt.show()


bar()
