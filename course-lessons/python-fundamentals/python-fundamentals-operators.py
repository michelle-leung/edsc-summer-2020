# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ![Colored Bar](colored-bar.png)

# <div class='notice--success' markdown="1">
#
# ## <i class="fa fa-graduation-cap" aria-hidden="true"></i> Learning Objectives
#
# At the end of this activity, you will be able to:
#
# * Explain how operators are used in **Python** to execute a specific computation or operation.
# * Write **Python** code to run different operations on data (e.g. arithmetic calculations)
#
# </div>
#
#
# ## What are Operators in Python?
#
# Operators are symbols in Python that carry out a specific computation, or operation. The value or condition that the operator operates on is called the operand. 
#
# The operand can be a variable (e.g. `jan_precip_in` which has some value, say, 0.70) or data structure like a list (e.g. `months`). The operand can also be an expression or statement (e.g. checking that list `months` contains the value `January`). 
#
# There are <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/" target="_blank">many different types of operators</a> in **Python** including: 
#
# | Operator | Usage | Example |
# |:-----------------------------------|:-----------------------------------|:-----------------------------------|
# | Arithmetic  | to complete mathematical calculations | `boulder_precip_in * 25.4` |
# | Assignment  | to assign new values (typically as a result of a arithmetic calculation) | `boulder_precip_in *= 25.4` |
# | Comparison or Relational  | to compare operands (e.g. greater than symbol `>`)  | `boulder_precip_in > phoenix_precip_in`|
# | Identity  | to check whether operands are the same | `boulder_precip_in is not phoenix_precip_in` |
# | Membership  | to check whether one operand is contained within another operand | `"January" in months` |
# | Logical  | to check whether operands are `true` | `"January" in months AND "Jan" in months` |

# ## Arithmetic Operators
#
# In **Python**, there are <a href="https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex" target="_blank">many arithmetic operations</a> that can be completed, including operators for: 
# * addition (`+`)
# * subtraction (`-`)
# * multiplication (`*`)
# * division (`/`)
# * exponents (`**`)
#
# Review the cells below and notice that the output is automatically printed without the need to tell **Python** to display the output. 

# +
a = 2
b = 3

a + b
# -

b - a

b / a

a * b

a ** b

# For scientific workflows, these arithmetic operators are very useful for converting the units of measurements, for example, from inches to millimeters (1 inch = 25.4 mm) for precipitation values.
#
# The example belows converts the average precipitation value for Boulder, CO in January from inches to millimeters.

# +
jan_precip = 0.70

jan_precip * 25.4
# -

# ### Interactive Activity
#
# In the cell below, create two variables: 
# * `march_precip_in` that is equal to `1.85`
# * `in_to_mm` that is equal to `25.4`
#
# Using only these variables and arithmetic operators, create a third variable `march_precip_mm`, which contains the average March precipitation for Boulder converted to millimeters (mm). 

# Create march_precip_mm equal to March precip in millimeters
march_precip_mm = 46.998

# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity. 
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# +
# Test to make sure that the variable was assigned correctly

import notebook_tests_fundamentals

try:
    print(notebook_tests_fundamentals.operators_test_march_precip(march_precip_mm))
except NameError:
    print("We couldn't find any variable named march_precip_mm, make sure that you correctly assigned the variable and ran the cell above.")
# -

# ## Assignment Operators
#
# While arithmetic operators are very useful for calculations, they do not change the original values. 
#
# For example, the variable `jan_precip` continues to store the value `0.7` (the measurement in inches), even after the calculations completed above. 

jan_precip

# If you want to assign a new value as a result of a calculation, you can use an assignment operator, which combines the arithmetic operator (e.g. `*`) with the `=` to set a new value. 
#
# For example, you can combine `*` and `=` to multiple a value and set the result equal to itself plus the new value. 

jan_precip *= 25.4

# Recall that on the previous page on working with lists, you also used an assignment operator to add items to the end of a list. 
#
# This is a special case of the addition assignment operator `+=` because it is not actually completing a mathematical operation on the list.  It simply adds the values as new items to the end of the list. 

# +
months = ["January", "February"]

months

# +
months += ["March", "April"]

months
# -

# However, not all assignment operators can be used on all object types. For example, the following code will result in an error because lists cannot have mathematical operations executed on them.  
#
# ```python
# boulder_precip_in = [0.70, 0.75, 1.85]
# boulder_precip_in *= 25.4
# ```
#
# You can review the <a href="https://docs.python.org/3/library/stdtypes.html#" target="_blank">Python docs on types and operations</a> to see what kinds of operations can be run on different object types. 

# ### Interactive Activity
#
# In the cell below, create two variables: 
# * `annual_avg_precip_nyc` that is equal to `42.65` (and is missing the december average precipitation)
# * `dec_avg_precip_nyc` that is equal to `3.58`
#
# Using the `+=` operator, add `december_precip_nyc` to `annual_avg_precip_nyc`, so that `annual_avg_precip_nyc` represents the complete annual average precipitation in New York City. 

# Add december_precip_nyc to annual_avg_precip_nyc using += operator


# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity. 
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# Tests to ensure the lists were added correctly
try:
    print(notebook_tests_fundamentals.operators_test_nyc_precip(annual_avg_precip_nyc))
except NameError:
    print("Could not find a variable named 'annual_avg_precip_nyc'. Check that your spelling is correct in your assignment of the variable!")

# ## Print Output
#
# Notice now that the output is not automatically printed.

# +
jan_precip = 0.70

jan_precip *= 25.4
# -

# To see the new value, you can call the variable name (e.g. `jan_precip`), or you can use the print statement (e.g. `print(jan_precip)`) to display the new value. 
#
# Using the print statement can be very helpful because then you can print multiple values. 
#
# For example, notice calling only the variable names (e.g. `a`, `jan_precip`, `b`), you are only shown the value of the last variable.

a
jan_precip
b

# Using `print()`, you can print as many things as you want. 

print(a)
print(jan_precip)
print(b)

# You can even combine the variables with a text string in a print statement by including a text string `"text"` within the print statement.
#
# To do this, simply separate the text string from the object that is being printed using a comma `,`. 

print("January precipitation:", jan_precip)

# Notice that the word `print` does not show up the output. Instead, you simply see the result, without the parentheses or quotations for the text string. 
#
# **You have now deliberately used your first Python function!** Functions in **Python** are commands that can take inputs that are used to produce output. 
#
# You will learn more about functions later in these exercises, and you will use the `print` function a lot, as it can be very handy for viewing results and for communicating the status of your code. 

# ## Relational Operators
#
# Often in **Python**, you need to compare two values against each other. To do this, you can check a statement, such as `3 < 4`, and get returned one of two values from **Python**: `True` or `False`. These are called boolean values and can be very powerful in scripting workflows. 
#
# A boolean is simply one bit of data that is either 1 (True), or 0 (False). Like strings or integers, booleans are their own data type.
#
# In **Python**, there are <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/#relational-operators" target="_blank">many relational operations</a> that can be used, including operators for: 
# * equal (`==`)
# * not equal (`!=`)
# * greater than (`>`)
# * greater than or equal (`>=`)
# * less than (`<`)
# * less than or equal (`<=`)
#
# Review the cells below to see what these operations return in different circumstances.

type(True)

# Relational operations return a boolean value. 

3 < 4

3 > 4

3 == 3

3 == 4

3 != 4

3 <= 4

3 <= 3

3 >= 4

# Similar to other types of variable types, `bool` values can be assigned to a variable. You do not need to put the operation in parenthesis, as is done below, but it helps with the legibility of the code.

# +
is_greater = (3 > 2)

is_greater
# -

# ## Identity Operators
#
# An identity operator, such as `is`, will check if two variables are referring to the same object. 
#
# It is similar to the `==` operator, except that it will not only check that the values of two variables are identical, but it will check that they are referring to the exact same thing in **Python**. It's a subtle distinction, but can be very useful. 

# +
# Create variables to compare
temp_1 = [70, 68, 74]
temp_2 = [70, 68, 74]

# Create temp_3 from temp_1
temp_3 = temp_1
# -

# Test that temp_3 the same as temp_1
temp_1 is temp_3

# While temp_1 and temp_2 contain the same values...
temp_1 == temp_2

# They have been created independently
temp_1 is temp_2

# With this example, you can easily see the distinction between `==` and `is`. 
#
# Even though `temp_1` and `temp_2` are identical to one another, they are technically not the same list. 
#
# However, since `temp_3` was set to equal `temp_1`, they are exactly the same. 

# You can also combine `is` with `not` to check that two variables are NOT the same. 

temp_1 is not temp_2

# Like all other types of boolean values, the outputs of these operations can be assigned to variables as well.

# +
is_the_same = (temp_1 is temp_2)

is_the_same
# -

# ## Membership Operators
#
# A membership operator, such as `in`, will check if one item contains another item. This can be useful with strings, lists, or other data storage objects that you will learn about in later lessons, such as dataframes. 

# +
precip = "Precipitation"

'Precip' in precip
# -

68 in temp_1

# You can also combine in with not to check for non-membership
69 not in temp_1

# ## Logical Operators
#
# Logical operators can be used to check combinations of booleans. The most common logical operators are `and` and `or`. 
#
# `and` will check that both of the statements being checked are true. `True and True` will return `True`, but `True and False` will return `False`. 
#
# `or` will check that one of the statements being checked are true. Unlike `and`, `True or True` will return `True`, and `True or False` will return `True` as well. 
#
# Both `False and False` and `False or False` will return `False`. 

# True and True
68 in temp_1 and 70 in temp_1

# True and False
68 in temp_1 and 69 in temp_1

# True or True
68 in temp_1 or 70 in temp_1

# True or False
68 in temp_1 or 69 in temp_1

# ### Interactive Activity
#
# Below, there are variables assigned to the output of either relational, identity, membership, or logical operations. Currently, each operation is returning `False`. Modify the operations so that they will all return `True`.

# +
# Modify relational operation so the assigned variable returns True
relational = (3 <= 2)

# Modify identity operation so the assigned variable returns True
identity = (4 is 3)

# Modify membership operation so the assigned variable returns True
membership = (72 in temp_1)

# Modify logical operation so the assigned variable returns True
logical = (68 in temp_1 and 69 in temp_1)
# -

# The cell below includes a set of tests to see if you correctly completed the activity in the cell above. They will provide you with feedback that can help you complete the activity. 
#
# Be sure to run the cell below to check your code (please do not modify the cell!).

# +
# Tests to see if the operations have been modified correctly

print(notebook_tests_fundamentals.operators_test_operation_modifications(relational, identity, membership, logical))
# -

#  <div class="notice--info" markdown="1">
#
# ## Additional Resources
#
# * <a href="https://docs.python.org/3/library/stdtypes.html#" target="_blank">Python docs on types and operations</a>
#
# * <a href="https://python-reference.readthedocs.io/en/latest/docs/operators/" target="_blank">Reference docs on operators</a>
#
# </div>   
