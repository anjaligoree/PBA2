import csv

# Open and read the CSV file
with open('attendance.csv', mode='r') as file:
    reader = csv.DictReader(file)
    
    print("Employee Attendance Summary:")
    for row in reader:
        name = row['Name']
        days = row['DaysPresent']
        print(f"{name}: {days} days")
