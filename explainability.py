def explain(row):
    reasons = []

    if row['gpa'] > 3.5:
        reasons.append("High GPA increases suitability")

    if row['communication'] < 40:
        reasons.append("Weak communication decreases score")

    if row['experience'] >= 5:
        reasons.append("Strong experience improves profile")

    if row['test_score'] > 85:
        reasons.append("High test performance is positive")

    return reasons
