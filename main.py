import pandas as pd

# Read the CSV file
df = pd.read_csv('cars.csv')

# Print the original DataFrame
print("Original DataFrame:")
print(df.to_string())

# Check if 'Mileage' column exists in the DataFrame
if 'Mileage' in df.columns:
    # Drop rows with missing values
    df.dropna(subset=['Mileage'], inplace=True)

    # Convert the 'Mileage' column to numeric
    df['Mileage'] = pd.to_numeric(df['Mileage'], errors='coerce')

    # Print the DataFrame after dropping missing values and converting 'Mileage' to numeric
    print("DataFrame after dropping missing values and converting 'Mileage' to numeric:")
    print(df.to_string())
else:
    print("The 'Mileage' column does not exist in the DataFrame.")
