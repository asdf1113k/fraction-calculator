import logging
import time
import os
import sys



# def input_fraction_calculator():
#     global denominator1
#     global numerator1
#     global integer1
#     global operator
#     global numerator2
#     global denominator2
#     global integer2
#     print("введите первую дробь")
#
#     try:
#         numerator1 = int(input("              числитель:"))
#     except ValueError:
#         print(logging.error("только числа"))
#         numerator1 = int(input("              числитель:"))
#
#     try:
#         integer1 = int(input("целое число дроби:"))
#     except ValueError:
#         print(logging.error("только числа"))
#         integer1 = int(input("целое число дроби:"))
#
#     try:
#         denominator1 = int(input("            знаменатель:"))
#     except ValueError:
#         print(logging.error("только числа"))
#         denominator1 = int(input("            знаменатель:"))
#
#
#     print("введите оператор:")
#     operator = "-"#input("-"*10+":")
#
#
#     print("введите вторую дробь")
#     try:numerator2 = int(input("              числитель:"))
#
#     except ValueError:
#         print(logging.error("только числа"))
#         numerator2 = int(input("              числитель:"))
#
#     try:
#         integer2 = int(input("целое число дроби:"))
#     except ValueError:
#         print(logging.error("только числа"))
#         integer2 = int(input("целое число дроби:"))
#
#     try:
#         denominator2 = int(input("            знаменатель:"))
#     except ValueError:
#         print(logging.error("только числа"))
#         denominator2 = int(input("            знаменатель:"))
#
#     if denominator2 == 0 or denominator1 == 0:
#         print("программа прекратит работу через 5 сек.")
#         print(logging.error("знаменатели не могут быть, меньше или равны нулю"))
#         time.sleep(5)
#         os.execv(sys.executable, [sys.executable] + sys.argv)
#
#     # if operator == "+": fraction_calculator_plus()
#     # if operator == "-": fraction_calculator_minus()
#     # if operator == "/": fraction_calculator_divide()



# код над которым идёт работа !!!!!!!



# код над которым идёт работа !!!!!!!



def print_fraction_calculator(result_numerator,result_integer,result_denominator):
    print(f"""              числитель:{result_numerator}
    целое число дроби:{result_integer} {"-" * 5}
                знаменатель:{result_denominator}""")


def main():
    reduce_fractional(4,2)
    # checking_calculator()


if __name__ == '__main__':
    main()
