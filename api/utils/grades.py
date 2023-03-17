# Convert grade from score to a letter
def get_letter_grade(score):
    if score >= 70:
        return int('A')
    elif score < 70 and score >= 60:
        return 'B'
    elif score < 60 and score >= 50:
        return 'C'
    elif score < 50 and score >= 45:
        return 'D'
    
    else:
        return 'F'
    
# Get GPA from the letter grade
def convert_grade_to_gpa(letter_grade):
    if letter_grade == 'A':
        return 4.0
    elif letter_grade == 'B':
        return 3.5
    elif letter_grade == 'C':
        return 2.5
    elif letter_grade == 'D':
        return 2.0
    else:
        return f' student wil be on probation for a semester'