# Importing pandas
import pandas as pd

# Step 1: Load the Data
# Create a simple dictionary of student names and their grades
data = {
    "Student Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Grade": [85, 92, 88, 79, 94]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Step 2: Analyze the Data
# Calculate the average grade
average_grade = df["Grade"].mean()
print(f"Average Grade: {average_grade}")

# Find the highest and lowest grades
highest_grade = df["Grade"].max()
lowest_grade = df["Grade"].min()

print(f"Highest Grade: {highest_grade}")
print(f"Lowest Grade: {lowest_grade}")

# Step 3: Filter the Data
# Filter students who have grades above 85
above_85 = df[df["Grade"] > 85]
print("\nStudents with grades above 85:")
print(above_85)

# Step 4: Add a New Column (Pass/Fail)
# Add a new column based on whether the grade is above 80
df["Pass/Fail"] = df["Grade"].apply(lambda x: "Pass" if x >= 80 else "Fail")

# Step 5: Display the Modified Data
print("\nModified Data with Pass/Fail column:")
print(df)

# Step 6: Save the Data to a CSV File
df.to_csv("student_grades.csv", index=False)
print("\nData saved to 'student_grades.csv'.")
