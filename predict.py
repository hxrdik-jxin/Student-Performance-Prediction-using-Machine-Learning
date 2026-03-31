import joblib
import numpy as np

model = joblib.load("../model/student_model.pkl")

study_hours = float(input("Study Hours: "))
attendance = float(input("Attendance (%): "))
previous_score = float(input("Previous Score: "))
assignments = int(input("Assignments Completed: "))

data = np.array([[study_hours, attendance, previous_score, assignments]])

prediction = model.predict(data)

print("Prediction:", prediction[0])
