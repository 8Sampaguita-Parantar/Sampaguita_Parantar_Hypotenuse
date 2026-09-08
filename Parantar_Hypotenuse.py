# Title - Program for a Right Triangle's Hypotenuse

#================================================================================================
# Author - Aldrich John P. Parantar
# Date - 08/27/2026
# Purpose - To find the hypotenuse of a right triangle.
#================================================================================================

#STEP 1 - Math Library Importation. This step allows math functions such as pow, sqrt, and most importantly for this code hypot.
import math

#STEP 2 - User Input Validation. This step asks the user to enter the length of the two sides which can be of decimal value because of its value being float, side a and side b before calculating.
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))

#STEP 4 - Input Processing. This step uses the imported math library from step 1 and the inputs from step 2 to calculate the right triangle's hypotenuse with math.hypot.
hypotenuse = math.hypot(side_a, side_b)

#STEP 5 - Output Display. This step gives the output from step 4's calculation through print and 2f, making it display up to 2 decimal numbers.
print(f"The hypotenuse is: {hypotenuse:.2f}")