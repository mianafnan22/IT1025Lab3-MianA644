# Start your code below with a comment that includes your name and the date
# Comment every line of code to show your understanding
# Write the code below to ask for two numbers. This will take two variables and two input() function statements.
# Check your code by printing the two numbers to the output window
# Use a decision structure to determing which number is bigger
# Output the answer using the print function that displays: "Variable x with a value of y is bigger then variable a with a value of b"
# the x and a are the variables that you created (not necessarily x and a)
# and the letters y and b should be replaced with the actual values
# use concatenation (rather than hard-coding the values) in your output. Remember concatenation is accomplished with the "+"

# Mian Afnan, June 20th 2021
print('Enter the first number:') # assign x to the first number
x = input()
#x = y
print('Enter the second number:') # assign y to the second number
a = input()
#a = b
if x > a:
  print("Variable x with a value of " + x + " is bigger then variable a with a value of " + a  )
elif x == a:
   print("First number and second number are equal")
else:
   print("The first number is greater than the second number")


