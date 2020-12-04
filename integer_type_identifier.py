# !/usr/bin/env Python3

# Created by Larry Nkengbeza
# Created on December 2020
# This program indicates the sign of the integer


def main():

    # Input
    integer_name = (int(input("Enter the type of integer: ")))
    print("")
    Positive = +1, +2, +3, +4, +5, +6
    Negative = -1, -2, -3, -4, -5, -6
    # Process and Output

    if integer_name == +5:
        print("+ sign")

    elif integer_name == -1:
        print("- sign")
    else:
        print("0")


if __name__ == "__main__":
    main()
