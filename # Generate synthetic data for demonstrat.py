# Generate synthetic data for demonstration purposes, since original data is unavailable
np.random.seed(42)  # For reproducibility
differences = np.random.normal(loc=0, scale=20000, size=200)
differences = np.clip(differences, -50000, 300000)  # To simulate the range seen in the original

# Create a DataFrame to simulate the data
data = pd.DataFrame({"Perbedaan": differences})

# Create a barplot version of the distribution
plt.figure(figsize=(12, 6))
sns.histplot(data=data, x="Perbedaan", bins=30, kde=True, color="skyblue", edgecolor="black")
plt.axvline(x=0, color="red", linestyle="--", linewidth=2, label="Mean Difference (2020-2023)")
plt.title("Distribusi Perbedaan Nilai Ekspor 2020 - 2023 (Barplot)", fontsize=16, weight='bold')
plt.xlabel("Perbedaan (2020 - 2023)", fontsize=12)
plt.ylabel("Frekuensi", fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save and display the plot
output_path = "/mnt/data/Distribusi_Perbedaan_Ekspor_Barplot.png"
plt.savefig(output_path)
plt.show()

output_path
