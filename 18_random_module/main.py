import json

student = {
	"name": "Hamza",
	"roll_no": 12,
	"marks": 89
}

with open("student.json", "w") as file:
	json.dump(student, file)

print("JSON data saved to file.")
