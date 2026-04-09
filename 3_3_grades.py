student = [
    {"name": "Arrie", "score": 85},
    {"name": "Bobby", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 88},
    {"name": "Ethan", "score": 95},
    {"name": "Fiona", "score": 80},
    {"name": "George", "score": 62},
    {"name": "Hannah", "score": 90},
    {"name": "Ian", "score": 87},
    {"name": "Jane", "score": 59}
    
] 
average_score = sum(s["score"] for s in student) / len(student)
highest_score = max(s["score"] for s in student)
lowest_score = min(s["score"] for s in student)

for s in student:
    score = s["score"]
    status = "Pass" if score >= 60 else "Fail"
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{s['name']}: Score: {score}, Grade: {grade}, Status: {status}")


print(f"\nClass Average Score: {average_score:.2f}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")   
