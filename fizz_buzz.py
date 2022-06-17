def fizz_buzz(begin_range,end_range):
    """ Проверка деления чисел на 3 и 5 и суммирование числового ряда
    и вывод призанака при делении на 3  Fizz, на 5 Buzz и на 3 и 5 FizzBuzz
    :param begin_range: начало диапазона
    :param end_range: конец диапазона
    """
    summarize = 0
    for i in range(begin_range,end_range + 1):
        if (i % 3 == 0 and i % 5 == 0):
            summarize += i
    return summarize

print('0-3:', fizz_buzz(0, 3))
print('0-5:', fizz_buzz(0, 5))
print('15-15:', fizz_buzz(15, 15))
print('1000-20000:', fizz_buzz(1000, 20000))


