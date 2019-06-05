"""
A program to demo
what functions
can do.
"""

# we start with a function "definition"
def add_3(a,b,c): # 1st line is called the header
	return a + b + c

print("===================")
# we then "call" (use) our function
# and "pass" it "parameters"
print(add_3(3.5,7.25,2))
print(add_3("polar","bear","baby"))
# todo: make function that joins words w/ a space inbetween (Google search: "join Python string")