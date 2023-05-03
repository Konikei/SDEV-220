import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a pandas DataFrame
df = pd.read_csv('data.csv')

# Convert the time column to a pandas datetime format
df['time'] = pd.to_datetime(df['time'])

# Set the index of the DataFrame to the time column
df.set_index('time', inplace=True)

# Resample the DataFrame to one-minute intervals
df_resampled = df.resample('1T').mean()

# Create a new column for the marker color based on the height
df_resampled['color'] = 'blue'
df_resampled.loc[df_resampled['height'] >= 100, 'color'] = 'red'

# Plot the data with colored markers
plt.scatter(df_resampled.index, df_resampled['height'], c=df_resampled['color'])

# Show the plot
plt.show()