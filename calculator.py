import re as regular_expression


def calculator(expression):
    try:
        if not regular_expression.search(r'^[0-9+\-*/()**\s]+$', expression):
            raise ValueError("expression can be number and mathematics operation")
        if regular_expression.search(r"0\s*\*\*\s*0", expression):
            raise ZeroDivisionError("0 to the power of 0 undefined")
        print(f"{expression} = {eval(expression)}")
    except (SyntaxError, NameError, ZeroDivisionError, TypeError, ValueError) as e:
        print(f"Error: {e}")


def main():
    while True:
        print("if you want to leave write exit")
        user_input = input("Enter a mathematical expression: ")
        if user_input == "exit":
            break
        else:
            calculator(user_input)


if __name__ == '__main__':
    main()
