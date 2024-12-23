import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data from the CSV file
df = pd.read_csv("epa-sea-level.csv")

def draw_plot():
    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Create a scatter plot of the data
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create the first line of best fit (using all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = range(1880, 2051)  # Extend the years to 2050 for prediction
    ax.plot(years_extended, [slope * year + intercept for year in years_extended], label="Best Fit Line (1880-2050)", color="red")

    # Filter data for years >= 2000 for the second line of best fit
    df_recent = df[df['Year'] >= 2000]

    # Create the second line of best fit (using data from 2000 onward)
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Restrict x-values for the second line to range from 2000 to 2050
    years_recent_extended = range(2000, 2051)  # Start from 2000 to 2050
    ax.plot(years_recent_extended, [slope_recent * year + intercept_recent for year in years_recent_extended], label="Best Fit Line (2000-2050)", color="blue")

    # Add title and labels
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")

    # Add legend
    ax.legend()

    # Save the plot
    fig.savefig("sea_level_plot.png")
    plt.show()

    return ax  # Return the axes object for testing
