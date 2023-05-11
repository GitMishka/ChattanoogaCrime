import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\Misha\Desktop\GitHub\ChattanoogaCrime\Booking Records - Charges.csv")

grouped_data = data.groupby("CHARGE_TYPE").size().reset_index(name="COUNT")

plt.figure(figsize=(12, 6))
bar_plot = sns.barplot(x="CHARGE_TYPE", y="COUNT", data=grouped_data)
plt.xlabel("Charge Type")
plt.ylabel("Count")
plt.title("Counts of Charges by Charge Type")
plt.xticks(rotation=45, ha='right')  
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(grouped_data["COUNT"], labels=grouped_data["CHARGE_TYPE"], autopct="%1.1f%%")
plt.title("Charge Types Distribution")
plt.show()

pivot_table = data.pivot_table(index="CHARGE_TYPE", columns="CHARGE_CLASSIFICATION", aggfunc="size", fill_value=0)

plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="YlGnBu")
plt.xlabel("Charge Classification")
plt.ylabel("Charge Type")
plt.title("Charge Classification Distribution by Charge Type")
plt.show()

pivot_table_percentage = pivot_table.div(pivot_table.sum(1), axis=0)
stacked_bar_chart = pivot_table_percentage.plot.bar(stacked=True, figsize=(12, 6))
plt.xlabel("Charge Type")
plt.ylabel("Proportion")
plt.title("Charge Classification Proportion by Charge Type")
plt.xticks(rotation=45, ha='right')  
plt.legend(title="Charge Classification")
plt.tight_layout()
plt.show()
