import logging
import os
import sys
import time
import asyncio
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

result_integer = None
result_numerator = None
result_denominator = None

def input_fraction_calculator():
    global denominator1
    global numerator1
    global integer1
    global operator
    global numerator2
    global denominator2
    global integer2
    print("введите первую дробь")

    try:
        numerator1 = int(input("              числитель:"))
    except ValueError:
        print(logging.error("только числа"))
        numerator1 = int(input("              числитель:"))

    try:
        integer1 = int(input("целое число дроби:"))
    except ValueError:
        print(logging.error("только числа"))
        integer1 = int(input("целое число дроби:"))

    try:
        denominator1 = int(input("            знаменатель:"))
    except ValueError:
        print(logging.error("только числа"))
        denominator1 = int(input("            знаменатель:"))


    print("введите оператор:")
    operator = input("-" * 10 + ":")


    print("введите вторую дробь")
    try:numerator2 = int(input("              числитель:"))

    except ValueError:
        print(logging.error("только числа"))
        numerator2 = int(input("              числитель:"))

    try:
        integer2 = int(input("целое число дроби:"))
    except ValueError:
        print(logging.error("только числа"))
        integer2 = int(input("целое число дроби:"))

    try:
        denominator2 = int(input("            знаменатель:"))
    except ValueError:
        print(logging.error("только числа"))
        denominator2 = int(input("            знаменатель:"))

    if denominator2 == 0 or denominator1 == 0:
        print("программа прекратит работу через 5 сек.")
        print(logging.error("знаменатели не могут быть, меньше или равны нулю"))
        time.sleep(5)
        os.execv(sys.executable, [sys.executable] + sys.argv)

    if operator == "+": fraction_calculator_plus()
    if operator == "-": fraction_calculator_minus()
    if operator == "/": fraction_calculator_divide()



def fraction_calculator_plus():  # сделать сокращение решения !!!!!!
    global integer1
    global integer2

    global numerator1
    global numerator2

    global denominator1
    global denominator2

    if operator == "+":
        if denominator1 == denominator2:
            result_integer = integer1 + integer2
            result_numerator = numerator1 + numerator2
            result_denominator = denominator2 = denominator1

            while range(result_numerator >= result_denominator):
                result_numerator -= result_denominator
                result_integer += 1
            if result_numerator == 0:
                result_denominator  = 0
            reduce_fractional(result_numerator,result_denominator)
            print_fraction_calculator(result_numerator,result_integer,result_denominator)


        if denominator1 != denominator2:
            # дописать до идиала, потому что знаменатель 6 и знаменатель 12 можно решить как 6 * = 12 !!!!!!
            print(" данные вами знаменатели не равны ".center(64, "+"))
            result_integer = integer1 + integer2  # (done)
            # умножить числитель и знаменатель1 на знаменатель2, и наоборот
            result_denominator = denominator2 * denominator1  # (done)
            numerator1 *= denominator2  # (done)
            denominator1 *= denominator2  # (done)
            numerator2 *= denominator1  # (done)
            denominator2 *= denominator1  # (done)
            result_numerator = numerator1 + numerator2

            if result_numerator >= result_denominator:
                while range(result_numerator >= result_denominator):
                    result_numerator -= result_denominator
                    result_integer += 1

            if result_numerator == 0:
                denominator1 = denominator2 = 0
            print_fraction_calculator(result_numerator,result_integer,result_denominator)

        print("the end")


def fraction_calculator_minus():# бывает решает не правильно (надо исправит) !!!!!!
    global integer1
    global integer2

    global numerator1
    global numerator2

    global denominator1
    global denominator2

    if operator == "-":
        if denominator1 == denominator2:
            result_integer = integer1 - integer2
            result_numerator = numerator1 - numerator2
            result_denominator = denominator2 = denominator1


            while range(result_numerator >= result_denominator):
                result_numerator -= result_denominator
                result_integer += 1

            if result_numerator == 0:
                result_denominator = 0
            print_fraction_calculator(result_numerator,result_integer,result_denominator)

        if denominator1 != denominator2:
            result_integer = integer1 - integer2  # (done)
            # умножить числитель и знаменатель1 на знаменатель2, и наоборот
            numerator1 *= denominator2
            numerator2 *= denominator1
            result_denominator = denominator2 * denominator1

            # print(f"result_denominator: {result_denominator}")

            result_numerator = numerator1 - numerator2
            if result_numerator <= -1:
                result_numerator *= -1

            if result_numerator == 0:
                result_denominator = 0



            print_fraction_calculator(result_numerator,result_integer,result_denominator)

    print("the end")


def fraction_calculator_divide(): # сыровато!!!!!!!!!!

    if operator == "/":
        global integer1
        global integer2

        global numerator1
        global numerator2

        global denominator1
        global denominator2

        if denominator1 == denominator2:

        # Умножить целую часть дроби (целое число) на знаменатель2.
        # Прибавить к произведению числитель.
        # Полученное число становится числителем неправильной дроби, а знаменатель остаётся неизменным.

            result_product_number1 = integer1 * denominator2
            result_product_number1 += numerator1

            result_product_number2 = integer2 * denominator1
            result_product_number2 += numerator2


            numerator1 = result_product_number1
            numerator2 = result_product_number2


            temporary_num1 = numerator2
            temporary_num2 = denominator2
            denominator2 = temporary_num1
            numerator2  = temporary_num2

            result_numerator = numerator1 * numerator2
            result_denumerator = denominator2 * denominator1

            if result_numerator == result_denumerator:
                result_integer = 1
                result_numerator = 0
                result_denumerator = 0
            print_fraction_calculator(result_numerator,result_integer,result_denominator)


        print("the end")

def reduce_fractional(numerator, denominator):
    test_remains = numerator % denominator
    if test_remains == 0:
        print(denominator)
    elif test_remains != 0:
        for a in range(2, 1000):
            test_remains = numerator % a
            if test_remains == 0:
                return a
    else:
        print("не сокращаеться !!!!!")

def print_fraction_calculator(result_numerator,result_integer,result_denominator):


    print(f"""              числитель:{result_numerator}
    целое число дроби:{result_integer} {"-" * 5}
                знаменатель:{result_denominator}""")

# функция которая сокращает дробь

def reduce_fractional(numerator, denominator):
    result_num1 = 0
    result_num2 = 0
    test_remains = numerator % denominator

    if test_remains == 0:
        result_num1 = denominator
    elif test_remains != 0:

        for num1 in range(2,1000):
            test_remains = numerator % num1

            if test_remains == 0:
                result_num1 = num1

    else:print("числитель не сокращаеться !!!!!")


    test_remains = denominator % numerator
    if test_remains == 0:
        result_num2 = numerator

    elif test_remains != 0:
        for num2 in range(2, 1000):
            test_remains = denominator % num2

            if test_remains == 0:
                result_num2 = num2
    else:
        print("знаменатель не сокращаеться !!!!!")


    # проверка равен ли делитель знаменателя и числителя

    if result_num1 == result_num2:
        print(f"общий разделитель: {result_num1}")
    else:
        print('Не возможно сократить дробь')


def main():
    input_fraction_calculator()
    # checking_calculator()


if __name__ == '__main__':
    main()
