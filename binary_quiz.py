# give the user a quiz question to
# convert a decimal number to a binary number
# such as: 'convert decimal 5 to binary:' and
# the user would write '101' to get the answer
# correct. the program will tell the user if they got the correct answer or not.

# binary to decimal
b_2_d = {
	0:0, 1:1, 10:2, 11:3,
	100:4, 101:5, 110:6, 111:7,
	1000:8, 1001:9, 1010:10, 1011:11,
	1100:12, 1101:13, 1110:14, 1111:15
}
#print(b_2_d.get(1110))
correct = 1110
print("====================")
answer = input("What is " + str(b_2_d.get(correct)) + " in binary?")
print("You answered",answer)