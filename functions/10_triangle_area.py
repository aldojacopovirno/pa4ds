# Assignment
# Write a function that receives a triangle’s base and height and returns its
# area using `base × height / 2`. Call it with a small example and display the
# result with a sentence that identifies the measurements.
#
# Solution

# Define two parameters so the same calculation can use different measurements.
# The height must be measured perpendicular to the chosen base.
def area_of_triangle(base, height):
    # A rectangle with this base and height has area base * height. The triangle
    # has half that area, so multiply by 0.5, which is the same as dividing by 2.
    area = 0.5 * base * height

    # In this implementation, the function prints the area inside the call.
    # Each f-string inserts the measurements and result into a readable sentence;
    # Python joins these adjacent strings before passing the sentence to print.
    print(
        f"The area of a triangle with a base of {base} and a height of "
        f"{height} is {area}"
    )
    # There is no return statement: reaching the end implicitly returns None.
    # Thus this implementation displays the area rather than returning its value.


# Call the function with positional arguments: 4.5 becomes base and 1.0 becomes
# height. The call calculates 2.25 and prints the sentence from inside the function.
area_of_triangle(4.5, 1.0)
