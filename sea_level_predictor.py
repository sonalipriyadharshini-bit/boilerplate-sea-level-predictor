import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read the data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots()

    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # First line of best fit - all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Years through 2050
    years = pd.Series(
        range(
            df["Year"].min(),
            2051
        )
    )

    # Predicted values
    line = slope * years + intercept

    # Plot first regression line
    ax.plot(
        years,
        line
    )

    # Data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]

    # Second line of best fit
    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Years from 2000 to 2050
    years_recent = pd.Series(
        range(
            2000,
            2051
        )
    )

    # Predicted values for recent data
    line_recent = (
        slope_recent * years_recent
        + intercept_recent
    )

    # Plot second regression line
    ax.plot(
        years_recent,
        line_recent
    )

    # Labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save the figure
    fig.savefig("sea_level_plot.png")

    # IMPORTANT: return AXES, not FIGURE
    return ax