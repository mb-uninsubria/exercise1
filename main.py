# Import seaborn
import seaborn as sns
import matplotlib.pyplot as plt
# Apply the default theme
sns.set_theme()

# Load an example dataset
penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")

plt.show()