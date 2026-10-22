# Assignment
# Convert a numeric grade on a scale from 1 to 10 into a letter grade. Use these
# bands: A for 8.5–10, B for 7.5–less than 8.5, C for 6.5–less than 7.5, D for
# 5.5–less than 6.5, and F for 1–less than 5.5. Reject grades outside the scale
# and display the resulting letter.
#
# Solution

# Descending thresholds assign each valid grade to exactly one band.
def convert_grade(grade: float) -> str:
    """Map a 1-to-10 grade to a letter using the stated thresholds."""
    if not 1 <= grade <= 10:
        raise ValueError("Grade must be between 1 and 10.")

    if grade >= 8.5:
        return "A"
    if grade >= 7.5:
        return "B"
    if grade >= 6.5:
        return "C"
    if grade >= 5.5:
        return "D"
    return "F"


grade = float(input("Enter your grade (1 to 10): "))
print(f"Letter grade: {convert_grade(grade)}")
