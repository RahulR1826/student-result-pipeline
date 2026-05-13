students = {
    "Naren": 85,
    "Rahul": 82,
    "Sakas": 76,
    "Pavan": 78,
    "Pranav": 87,
    "Ragavan": 83
}

print("Student Result Processing System\n")

for name, marks in students.items():
    status = "PASS" if marks >= 50 else "FAIL"
    print(f"{name}: {marks} - {status}")
