import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Misha\Desktop\GitHub\ChattanoogaCrime\Booking Records - BookingDataAnon.csv")


data = data.sort_values(by='AGE', ascending=False)

# Bar chart showing the number of charges per age
plt.figure(figsize=(16, 6))
data['AGE'].value_counts().plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Number of Charges')
plt.title('Number of Charges per Age')
plt.show()

# Pie chart showing the distribution of primary charge types
plt.figure(figsize=(16, 16))
data['PRIMARY_CHARGE_TYPE'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel('')
plt.title('Distribution of Primary Charge Types')
plt.show()

# Bar chart showing the number of charges per agency
plt.figure(figsize=(16, 6))
data['AGENCY'].value_counts().plot(kind='bar')
plt.xlabel('Agency')
plt.ylabel('Number of Charges')
plt.title('Number of Charges per Agency')
plt.show()

# Bar chart showing the distribution of highest charge classification
plt.figure(figsize=(16, 6))
data['HIGHEST_CHARGE_CLASSIFICATION'].value_counts().plot(kind='bar')
plt.xlabel('Highest Charge Classification')
plt.ylabel('Number of Charges')
plt.title('Distribution of Highest Charge Classification')
plt.show()