# Input a number and count how many times each digit (0–9) appears.

num = 67398764
"""
3 - 1
4 - 1
6 - 2
7 - 2
8 - 1
9 - 1


1. dictionary
2. array, list
3. multiple variables
"""

zero_counter = 0
one_counter = 0
two_counter = 0
three_counter = 0
four_counter = 0
five_counter = 0
six_counter = 0
seven_counter = 0
eight_counter = 0
nine_counter = 0

while num>0:
    ld = num % 10       # 4
    num = num // 10     # 6739876
    
    if ld == 0:
        zero_counter = zero_counter + 1
    elif ld == 1:
        one_counter = one_counter + 1
    elif ld == 2:
        two_counter = two_counter + 1
    elif ld == 3:
        three_counter = three_counter + 1
    elif ld == 4:
        four_counter = four_counter + 1
    elif ld == 5:
        five_counter = five_counter + 1
    elif ld == 6:
        six_counter = six_counter + 1
    elif ld == 7:
        seven_counter = seven_counter + 1
    elif ld == 8:
        eight_counter = eight_counter + 1
    elif ld == 9:
        nine_counter = nine_counter + 1

if zero_counter != 0:
    print(f"0 -> {zero_counter}")
if one_counter != 0 :
    print(f"1 -> {one_counter}")
if two_counter != 0:
    print(f"2 -> {two_counter}")
if three_counter != 0:
    print(f"3 -> {three_counter}")
if four_counter != 0:
    print(f"4 -> {four_counter}")
if five_counter != 0:
    print(f"5 -> {five_counter}")
if six_counter != 0:
    print(f"6 -> {six_counter}")
if seven_counter != 0:
    print(f"7 -> {seven_counter}")
if eight_counter != 0:
    print(f"8 -> {eight_counter}")
if nine_counter != 0:
    print(f"9 -> {nine_counter}")

