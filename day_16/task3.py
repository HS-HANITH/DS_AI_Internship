import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

population = np.random.exponential(scale=50000, size=100000)

sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=30)
    sample_means.append(np.mean(sample))

sample_means = np.array(sample_means)

print("Population Mean:", round(np.mean(population), 2))
print("Mean of Sample Means:", round(np.mean(sample_means), 2))
print("Standard Deviation of Sample Means:", round(np.std(sample_means), 2))

plt.figure(figsize=(6,4))
sns.histplot(population, bins=50, kde=True)
plt.title("Original Population (Right-Skewed)")
plt.tight_layout()
plt.savefig("population_distribution.png")
plt.close()

plt.figure(figsize=(6,4))
sns.histplot(sample_means, bins=30, kde=True)
plt.title("Distribution of Sample Means (n=30)")
plt.tight_layout()
plt.savefig("sample_means_distribution.png")
plt.close()

print("Plots saved successfully.")
