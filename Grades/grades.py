from decimal import Decimal, ROUND_HALF_UP


suffix_scores = [97, 93, 90, 87, 83, 80, 77, 73, 70, 67, 63, 60, 0]
suffix_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
scores = [90, 80, 70, 60, 0]
grades = ['A', 'B', 'C', 'D', 'F']
GPAS = {
    'A+': 4.33,
    'A' : 4.00,
    'A-': 3.67,
    'B+': 3.33,
    'B' : 3.00,
    'B-': 2.67,
    'C+': 2.33,
    'C' : 2.00,
    'C-': 1.67,
    'D+': 1.33,
    'D' : 1.00,
    'D-': 0.67,
    'F' : 0.00,
}


def percent_to_grade(percentage, *, suffix=False, round=False):
    if round:
        percentage = Decimal(percentage).quantize(0, ROUND_HALF_UP)

    for score, grade in zip(suffix_scores, suffix_grades) if suffix else zip(scores, grades):
        if percentage >= score:
            return grade


def calculate_gpa(grade_list):
    return sum(GPAS[g] for g in grade_list) / len(grade_list)
