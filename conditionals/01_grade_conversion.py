# Assignment
# Convert a numeric grade on a scale from 1 to 10 into a letter grade. Use these
# bands: A for 8.5–10, B for 7.5–less than 8.5, C for 6.5–less than 7.5, D for
# 5.5–less than 6.5, and F for 1–less than 5.5. Reject grades outside the scale
# and display the resulting letter.
#
# Solution

# Define a function so we can convert a grade whenever we call convert_grade(...).
# grade receives the value from that call. The hints float and -> str describe
# the expected input and returned result; they do not check values at runtime.
def convert_grade(grade: float) -> str:
    """Map a 1-to-10 grade to a letter using the stated thresholds."""
    # The chained comparison 1 <= grade <= 10 is True when both limits hold.
    # not reverses that Boolean result, so this block runs for an invalid grade.
    # Raise an error before choosing a letter: values outside the scale have no band.
    if not 1 <= grade <= 10:
        raise ValueError("Grade must be between 1 and 10.")

    # Check the highest band first. Each comparison produces True or False;
    # an if block runs only when its condition is True. Include 8.5 in band A.
    # return sends the letter back to the caller and immediately ends this call,
    # so a grade in this band never reaches the lower thresholds.
    if grade >= 8.5:
        return "A"

    # Reaching this line means grade < 8.5. Checking only the lower limit is
    # enough: together, the two facts identify 7.5 <= grade < 8.5 as band B.
    if grade >= 7.5:
        return "B"

    # Continue down the thresholds. Earlier returns have excluded A and B,
    # so a successful check here selects exactly 6.5 <= grade < 7.5.
    if grade >= 6.5:
        return "C"

    # A grade reaching this check is below 6.5; include 5.5 in band D.
    if grade >= 5.5:
        return "D"

    # All higher bands have been excluded. The initial check also guarantees
    # grade >= 1, so every remaining grade belongs to F without another if.
    return "F"


# input() returns text. Convert it to float so decimal grades such as 8.5
# can be compared with the numeric thresholds in the function.
grade = float(input("Enter your grade (1 to 10): "))

# Call the function with the entered grade. Its returned letter replaces the
# expression in braces, and the label tells the reader what that letter means.
print(f"Letter grade: {convert_grade(grade)}")
