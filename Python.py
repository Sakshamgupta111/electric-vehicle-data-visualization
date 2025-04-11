import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------
# Load the dataset
# ---------------------------------------------
df = pd.read_csv("C:\\Users\\Saksham\\Downloads\\cleaned_electric_vehicle_data ###.csv")

# ---------------------------------------------
# Basic Data Inspection
# ---------------------------------------------
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe(include='all'))  # Removed datetime_is_numeric for compatibility

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# ---------------------------------------------
# Set the visual style
# ---------------------------------------------
sns.set(style="whitegrid")

# ---------------------------------------------
# Objective 1: Distribution of Electric Vehicle Types
# ---------------------------------------------
plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    y='clean_alternative_fuel_vehicle_type',
    order=df['clean_alternative_fuel_vehicle_type'].value_counts().index,
    palette='viridis'
)
plt.title('Distribution of Electric Vehicle Types')
plt.xlabel('Count')
plt.ylabel('Vehicle Type')
plt.tight_layout()
plt.show()

# Donut Chart
vehicle_type_counts = df['clean_alternative_fuel_vehicle_type'].value_counts()
plt.figure(figsize=(8, 8))
colors = sns.color_palette('viridis', len(vehicle_type_counts))
plt.pie(
    vehicle_type_counts,
    labels=vehicle_type_counts.index,
    colors=colors,
    wedgeprops=dict(width=0.4),
    startangle=140,
    autopct='%1.1f%%'
)
plt.title('EV Type Distribution (Donut Chart)')
plt.tight_layout()
plt.show()

# ---------------------------------------------
# Objective 2: Top 10 EV Makes by Count
# ---------------------------------------------
top_makes = df['make'].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_makes.values, y=top_makes.index, palette='crest')
plt.title('Top 10 EV Makes by Count')
plt.xlabel('Number of Vehicles')
plt.ylabel('EV Make')
plt.tight_layout()
plt.show()

# ---------------------------------------------
# Objective 3: Electric Range Distribution
# ---------------------------------------------
plt.figure(figsize=(10, 6))
sns.histplot(df['electric_range'], bins=50, kde=True, color='skyblue')
plt.title('Electric Range Distribution')
plt.xlabel('Electric Range (miles)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# ---------------------------------------------
# Objective 4: EV Registration Trend by Year
# ---------------------------------------------
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='model_year', palette='flare')
plt.title('EV Registration Trend by Year')
plt.xlabel('Model Year')
plt.ylabel('Number of Registrations')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------------
# Objective 5: Top Cities with the Most EV Registration
# ---------------------------------------------
top_cities = df['city'].value_counts().nlargest(10)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_cities.values, y=top_cities.index, palette='magma')
plt.title('Top Cities with the Most EV Registration')
plt.xlabel('Number of Registrations')
plt.ylabel('City')
plt.tight_layout()
plt.show()
