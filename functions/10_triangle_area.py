# Assignment
# Write a function that receives a triangle’s base and height and returns its
# area using `base × height / 2`. Call it with a small example and display the
# result with a sentence that identifies the measurements.
#
# Solution

# Half of the base-height rectangle is the triangle area.
def area_of_triangle(base, height):
    area = 0.5 * base * height
    print(
        f"The area of a triangle with a base of {base} and a height of "
        f"{height} is {area}"
    )


area_of_triangle(4.5, 1.0)
