from typing import List, NewType, Union


def log_clause(clause: str) -> None:
    print(f"--- {clause} ---")

# A
log_clause("A")
x, y = 3, 4

if x > y:
    print("BIG")
else:
    print("SMALL")


# B
log_clause("B")
for idx in range(5):
    print(idx)


# C
log_clause("C")
my_number = 3
season = "" # Initialize with empty string
if my_number == 1:
    season = "summer"
elif my_number == 2:
    season = "winter"
elif my_number == 3:
    season = "fall"
elif my_number == 4:
    season = "spring"

print(season)


# D
log_clause("D")
print("Answer is 10")


# E
log_clause("D")
age = 24
usd_ils_rate = 3.22
flew_aboard = True
print(age, usd_ils_rate, flew_aboard)
print(age + usd_ils_rate)


# F
log_clause("F")
phone_number_str: str = input("Please insert your phone number:")
# Validation
str_digits: List[str] = []
for int_digit in range(10):
    str_digit = str(int_digit)
    str_digits.append(str_digit)
# Now we have str_digits populated with from 0-9 string digits 
is_valid = True
for char in phone_number_str:
    if char not in str_digits:
        is_valid = False
        print(f" \"{char}\" is not valid digit! please use only: {str_digits}")
        break

if is_valid:
    print("phone number", phone_number_str)


# G
log_clause("G")

def print_hello() -> None:
    print("Hello")

def calculate() -> None:
    print(5 + 3.2)

print_hello()
calculate()

# H
log_clause("H")

NumberType = NewType("Number", List[Union[int, float]])

def print_name(name: str) -> None:
    print(name)

def devide_by_2(num_to_devide: NumberType) -> None:
    print(num_to_devide / 2)

# I
log_clause("I")

def sum(a: NumberType, b: NumberType) -> None:
    print(a + b)

def print_with_space(a: str, b: str) -> None:
    print(f"{a} {b}")


# K
log_clause("K")

for i in range(1, 6):
    line = "*" * i
    print(line)


# L
log_clause("L")

for i in range(7):
    line = ""
    for j in range(7):
        char = " "
        if i == j or i+j == 6:
            char += "*"
        line += char

    print(line)

# M
log_clause("M")

def get_number_from_input():
    return input("Give me a number:")

def sum_of_digits(number_str: str):
    sum = 0
    for digit_str in number_str:
        digit_int = int(digit_str)
        sum += digit_int

    return sum

number_from_user = "1005" # get_number_from_input()
sum_ = sum_of_digits(number_from_user)
print(f"sum of {number_from_user} is {sum_}")
