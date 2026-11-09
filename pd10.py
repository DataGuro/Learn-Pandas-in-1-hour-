# ============================================================
# DataScienceLab - Parts C to VIII (Troubleshooting)
# ============================================================

# ------------------------------------------------------------
# Part C: Loading a Dataset
# ------------------------------------------------------------
import pandas as pd
import os

print("=" * 60)
print("PART C: LOADING A DATASET")
print("=" * 60)

# Check current working directory
print("\nCurrent Working Directory:")
print(os.getcwd())

# Load the dataset using relative path
df = pd.read_csv("mindanao_agriculture.csv")

# Display the entire DataFrame
print("\nFull Dataset:")
print(df)

# ------------------------------------------------------------
# Part D: Viewing Dataset Information
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("PART D: VIEWING DATASET INFORMATION")
print("=" * 60)

print("\n1. First 5 records (df.head()):")
print(df.head())

print("\n2. Last 5 records (df.tail()):")
print(df.tail())

print("\n3. Dataset Information (df.info()):")
df.info()

print("\n4. Summary Statistics (df.describe()):")
print(df.describe())

# Answers to Part D Questions
print("\n--- Answers to Part D Questions ---")
print(f"1. How many rows?        → {df.shape[0]} rows")
print(f"2. How many columns?     → {df.shape[1]} columns")
print(f"3. Which columns are numeric? → {list(df.select_dtypes(include='number').columns)}")
print(f"4. Which are text?       → {list(df.select_dtypes(include='object').columns)}")

# ------------------------------------------------------------
# Part E: File Path Investigation
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("PART E: FILE PATH INVESTIGATION")
print("=" * 60)

# Method 1: Relative Path (Recommended)
print("\nMethod 1: Relative Path")
df_relative = pd.read_csv("../datasets/mindanao_agriculture.csv")
print("Relative path loaded successfully!")
print(df_relative.head(2))

# Method 2: Absolute Path (Example - change according to your computer)
print("\nMethod 2: Absolute Path (Example)")
# Uncomment and edit the path below according to your computer:
# df_absolute = pd.read_csv("C:/Users/Student/DataScienceLab/datasets/mindanao_agriculture.csv")
# print("Absolute path loaded successfully!")

print("\nDiscussion:")
print("Which is more portable? → Relative paths work better when sharing projects.")
print("Reason: Absolute paths break when the project is moved to another computer or folder.")

# ------------------------------------------------------------
# Part F: Confirming Compatibility on Different Computers
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("PART F: COMPATIBILITY ON DIFFERENT COMPUTERS")
print("=" * 60)

print("""
Guide Questions:

1. Did it work immediately? Why?
   → Yes (if you copied the entire DataScienceLab folder).
     Relative paths depend on the folder structure, not the computer location.

2. Would the absolute path still work? Explain.
   → No. Absolute paths contain the specific username and drive letter
     (e.g., C:/Users/Student/...). These change on other computers.
""")

# ------------------------------------------------------------
# VIII. Troubleshooting Activity
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("VIII. TROUBLESHOOTING ACTIVITY")
print("=" * 60)

# Scenario 1: Wrong filename
print("\n--- Scenario 1: Wrong Filename ---")
print("Code that causes error:")
print('df = pd.read_csv("../datasets/agriculture.csv")')
print("Error: FileNotFoundError")
print("Solution: Check spelling, folder location, and file extension.")
print("Correct code:")
print('df = pd.read_csv("mindanao_agriculture.csv")')

# Scenario 2: Wrong folder
print("\n--- Scenario 2: Wrong Folder ---")
print("If you move the CSV file to another location → FileNotFoundError")
print("Fix: Return the CSV to the correct folder (datasets/)")

# Scenario 3: Wrong delimiter
print("\n--- Scenario 3: Wrong Delimiter ---")
print("If the CSV uses semicolon (;) instead of comma (,):")
print("Wrong:  df = pd.read_csv('dataset.csv')          → One giant column")
print("Correct: df = pd.read_csv('dataset.csv', sep=';')")

# Scenario 4: Encoding Problem
print("\n--- Scenario 4: Encoding Problem ---")
print("Error: UnicodeDecodeError")
print("Fix options:")
print('df = pd.read_csv("dataset.csv", encoding="latin1")')
print('df = pd.read_csv("dataset.csv", encoding="cp1252")')
print('df = pd.read_csv("dataset.csv", encoding="utf-8")')

# Scenario 5: Missing File Extension
print("\n--- Scenario 5: Missing File Extension ---")
print("Wrong:   pd.read_csv('mindanao_agriculture')")
print("Correct: pd.read_csv('mindanao_agriculture.csv')")

print("\n" + "=" * 60)
print("END OF LABORATORY CODE")
print("=" * 60)