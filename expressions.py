def calc_math_expression(num1, num2, operator):
    if num2 == 0:
        return None
    elif operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == ':':
        return num1 / num2
    else:
        return None


def calc_math_expression_from_str(str_input):
    # Split the input string by ' '
    str_list = str_input.split()
    # Get the first two numbers
    num1 = float(str_list[0])
    num2 = float(str_list[2])
    # Get the operator
    operator = str_list[1]
    # Calculate the result
    result = calc_math_expression(num1, num2, operator)
    return result


def find_largest_and_smallest_numbers(num1=0.0,  num2=0.0, num3=0.0):
    # Calculate the largest and smallest numbers
    largest = max(num1, num2, num3)
    smallest = min(num1, num2, num3)
    return (largest, smallest)


def quadratic_equation_solver(a, b, c):
    # Calculate the discriminant
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return (None, None)
    elif discriminant == 0:
        return ((-b / (2 * a)), None)
    else:
        solution1 = (-b + discriminant ** 0.5) / (2 * a)
        solution2 = (-b - discriminant ** 0.5) / (2 * a)
        return (solution1, solution2)


def quadratic_equation_solver_from_user_input():
    coefficients = input("Enter the coefficients of the equation: ")
    coefficients = coefficients.split()
    a = float(coefficients[0])
    b = float(coefficients[1])
    c = float(coefficients[2])
    return quadratic_equation_solver(a, b, c)

# print(quadratic_equation_solver_from_user_input())


def temp_checker(min_temp, temp_1, temp_2, temp_3):
    if (temp_1 and temp_2) > min_temp or (temp_1 and temp_3) > min_temp:
        return True
    else:
        return False