Green_Tea = 3
sushi_plates = 15

Price_1 = 2.50
Price_2 = 1.99

print("==================================")
print("green tea: $" + str(Green_Tea * Price_1))
print("sushi plates: $" + str(sushi_plates * Price_2))

total = (Green_Tea * Price_1) + (sushi_plates * Price_2)
tip = 0.18

total_with_tip = total * tip + total

print("total with tip: $", total_with_tip)

# remove decimals after 2nd
print(((44.073*100)//1)/100)

# math operators: */+-%,//

"""todo:
1. Make a total which holds the entire cost of the meal
2. Calculate the tip (15, 18, or 20%)
3. Add the tip to the total
pay amount and print this last
value out like so: "total with tip: 99.99"
bonus: add dollar signs $ to your print outs
"""

#<!-- this is an HTML comment -->