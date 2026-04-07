import pandas as pd
import mysql.connector
import os

# 🔹 Step 1: File path (your correct path)
file_path = r"E:\study materials\Bluestock\india-village-project\data\final_cleaned_india_data new.csv"

# 🔹 Step 2: Check file exists
print("Checking file path...")
print(os.path.exists(file_path))  # should print True

# 🔹 Step 3: Load CSV
df = pd.read_csv(file_path)

print("✅ CSV Loaded Successfully")

# 🔹 Step 4: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Madhanmaddy_144",   # 🔴 CHANGE THIS
    database="india_data"
)

cursor = conn.cursor()

print("✅ Connected to MySQL")

# 🔹 Step 5: Insert query
query = """
INSERT INTO villages (State, District, SubDistrict, Village)
VALUES (%s, %s, %s, %s)
"""

# 🔹 Step 6: Convert dataframe to list
data = list(df.itertuples(index=False, name=None))

print("⏳ Inserting data... please wait...")

# 🔹 Step 7: Insert data
cursor.executemany(query, data)

conn.commit()

print("🔥 DONE BRO — FULL DATA INSERTED SUCCESSFULLY 🔥")

# 🔹 Step 8: Close connection
cursor.close()
conn.close()