import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("population.csv", skiprows=4)

# Take 2020 data
data = df[['Country Name', '2020']].dropna()

# Plot histogram
plt.hist(data['2020'], bins=10)

plt.title("Population Distribution (2020)")
plt.xlabel("Population")
plt.ylabel("Frequency")

plt.show()
