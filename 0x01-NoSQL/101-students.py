#!/usr/bin/env python3
"""101-students.py"""

def top_students(mongo_collection):
    """returns all students sorted by average score"""
    all_students = mongo_collection.find({})

    students_with_avg_score = []

    for student in all_students:
        scores = student.get('scores', [])
        if scores:
            total_score = sum(score['score'] for score in scores)
            average_score = total_score / len(scores)
            students_with_avg_score.append((student, average_score))

    sorted_students = sorted(students_with_avg_score, key=lambda x: x[1], reverse=True)

    return [{'student': student[0], 'averageScore': student[1]} for student in sorted_students]

if __name__ == "__main__":
    result = top_students(mongo_collection)
    for student_data in result:
        student = student_data['student']
        student_id = str(student['_id'])
        hex_student_id = student_id.encode().hex()
        print(f"[{hex_student_id}] {student['name']} - {student['scores']} => {student_data['averageScore']}")
