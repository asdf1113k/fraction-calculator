integer1 = 0
integer2 = 0

numerator1 = 2132
numerator2 = 872

denominator1 = 11
denominator2 = 11




def fraction_calculator_plus():
    "сделать правильное решение не правильных дробей"
    global integer1
    global integer2
    global numerator1
    global numerator2
    global denominator1
    global denominator2

    operator = "+"
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

            common_divisor = reduce_fractional(result_numerator, result_denominator)
            print_fraction_calculator(result_numerator,result_integer,result_denominator,common_divisor)


        if denominator1 != denominator2:
            "подключить исправление не правильных дробей"


        print("the end")

def reduce_fractional(numerator, denominator):
    "функция которая сокращает дробь"
    print("\n")
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
        common_divisor = result_num1
        return common_divisor
    else:
        print('возможно можно ещё сократить дробь ')
        common_divisor = 1
        return common_divisor

def incorrect_fraction_in_correct_fraction(numerator: int,integer: int,denominator: int):
    "переводит не правильную дробь в смешанное число"

    result_numerator = numerator & denominator
    result_integer = numerator // denominator
    result_integer += integer
    return


def print_fraction_calculator(result_numerator,result_integer,result_denominator, common_divisor=1):
    print("="*40)

    print(f"""              числитель:{result_numerator // common_divisor}
    целое число дроби:{result_integer} {"-" * 5}
                знаменатель:{result_denominator // common_divisor}""")

    # try:
    #     reduce_fractional(result_numerator, result_denominator)
    # except ZeroDivisionError:
    #     print("не удалось сократить дробь")












def main():
    fraction_calculator_plus()

if __name__ == '__main__':
    main()