from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
import os

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Create a boxplot for median income
plt.figure(figsize=(8, 5))
plt.boxplot(df["MedInc"])
plt.title("California Housing - Median Income Boxplot")
plt.ylabel("Median Income")

# Make sure the figs folder exists
os.makedirs("figs", exist_ok=True)

# Save the figure
plt.savefig("figs/boxplot.png", bbox_inches="tight")

# Show the plot
plt.show()