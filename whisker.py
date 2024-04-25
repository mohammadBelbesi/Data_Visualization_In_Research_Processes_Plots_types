import matplotlib.pyplot as plt
import pandas as pd


def whisker_plot(start_date, end_date, data_frequency='D'):

    """
    Create a whisker plot for time-based data.

    Parameters:
        start_date (str or pandas.Timestamp): Start date of the data range.
        end_date (str or pandas.Timestamp): End date of the data range.
        data_frequency (str, optional): Frequency of the data.
        Defaults to 'D' (daily).

    Returns:
        None
    """

    # Sample time-based data with at least 10 data points
    data1 = pd.date_range(start_date, end_date, freq=data_frequency)
    # Offset the second dataset
    data2 = pd.date_range(start_date + pd.Timedelta(days=5), end_date +
                          pd.Timedelta(days=5), freq=data_frequency)

    numeric_data1 = (data1 - start_date).days
    numeric_data2 = (data2 - start_date).days

    # Create a whisker plot
    plt.figure(figsize=(10, 6))  # Increase figure size

    # First whisker plot
    plt.boxplot([numeric_data1, numeric_data2], vert=False)

    # Add labels and title
    plt.xlabel('Days from Start Date', labelpad=15)
    # Rotate y-axis label by 90 degrees, move to the left, and a little bit up
    plt.ylabel('Date', rotation=0, labelpad=10, verticalalignment='top')
    plt.gca().yaxis.set_label_coords(-0.1, 0.5)
    plt.title('Whisker Plot Example for Time-Based Data')

    # Remove right and top spines
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)

    plt.savefig('whisker_plot.png', dpi=300, bbox_inches='tight')

    plt.show()


# Example usage
whisker_plot(pd.Timestamp('2022-01-01'), pd.Timestamp('2022-01-20'), 'D')
