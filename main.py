def checking_calculator():
    while True:
        print("enter the first operand (введите первый операнд)")
        operand1 = int(input("-" * 10 + ":"))
        print("enter the operator (введите оператор): + , - , * , /")
        operator = input("-" * 10 + ":")
        print("enter the second operand (введите второй операнд)")
        operand2 = int(input("-" * 10 + ":"))
        print("provide a response for verification (введите ответ для проверки)")
        user_result = int(input("-" * 10 + ":"))

        if operator == "+":
            result = operand1 + operand2
            if user_result == result:
                print(f"This is the right decision. = {user_result} \n {"-" * 50}")
            else:
                print(f"This is the wrong decision. result = {result} \n {"-" * 50}")
        if operator == "-":
            result = operand1 - operand2
            if user_result == result:
                print(f"This is the right decision. = {user_result} \n {"-" * 50}")
            else:
                print(f"This is the wrong decision. result = {result} \n {"-" * 50}")
        if operator == "*":
            result = operand1 * operand2
            if user_result == result:
                print(f"This is the right decision. = {user_result} \n {"-" * 50}")
            else:
                print(f"This is the wrong decision. result = {result} \n {"-" * 50}")
        if operator == "/":
            result = operand1 / operand2
            if user_result == result:
                print(f"This is the right decision. = {user_result} \n {"-" * 50}")
            else:
                print(f"This is the wrong decision. result = {result} \n {"-" * 50}")

integer1 = None
integer2 = None

numerator1 = None
numerator2 = None

denominator1 = None
denominator2 = None

operator = ''

def input_fraction_calculator():
    print("введите первую дробь")
    global numerator1
    numerator1 = int(input("              числитель:"))
    global integer1
    integer1 = int(input("целое число дроби:"))
    global denominator1
    denominator1 = int(input("            знаменатель:"))

    print("введите оператор:+")
    global operator
    operator = "+"
    """input("-" * 10 + ":")"""

    print("введите вторую дробь")
    global numerator2
    numerator2 = int(input("              числитель:"))
    global integer2
    integer2 = int(input("целое число дроби:"))
    global denominator2
    denominator2 = int(input("            знаменатель:"))
    if denominator1 == denominator2:
        print("данные вами знаменатели равны")
    elif denominator1 != denominator2:
        print(" данные вами знаменатели не равны ".center(64, "+"))
    if operator == "+": fraction_calculator_plus()
    if operator == "-": fraction_calculator_minus()
    # return integer1, integer2, numerator1, numerator2, denominator1, denominator2

def fraction_calculator_plus():
    # БАГ- не прекращает работу если знаменатель равен 0 !!!!!!!!!
    global integer1
    global integer2

    global numerator1
    global numerator2

    global denominator1
    global denominator2

    if operator == "+":
        result_integer = integer1 + integer2
        result_numerator = numerator1 + numerator2

        if result_numerator >= denominator1:
            while range(numerator1 >= denominator1):
                numerator1 -= denominator1
                result_integer += 1
            print("решено правильно")

        if result_numerator >= denominator1:
            denominator1 = 0

    print(f"""              числитель:{numerator1}
    целое число дроби:{result_integer + 1} {"-" * 5}
                знаменатель:{denominator1}""")

    print("the end")


def fraction_calculator_minus():  # БАГ- не прекращает работу если знаменатель равен 0 !!!!!!!!!
    global integer1
    global integer2

    global numerator1
    global numerator2

    global denominator1
    global denominator2

    if operator == "-":
        result_integer = integer1 - integer2
        result_numerator = numerator1 - numerator2

        if result_numerator >= denominator1:
            while range(numerator1 >= denominator1):
                numerator1 -= denominator1
                result_integer -= 1
            print("решено правильно")

        if result_numerator >= denominator1:
            denominator1 = 0

    print(f"""              числитель:{numerator1}
    целое число дроби:{result_integer} {"-" * 5}
                знаменатель:{denominator1}""")
    print("the end")


def main():
    input_fraction_calculator()
    # checking_calculator()


if __name__ == '__main__':
    main()
