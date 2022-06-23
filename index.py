# Функция fizz_buzz
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


# Функция plural_form
def plural_form(number, form_1, form_2, form_3):
    """ Согласование окончаний  числительный множественного числа. 
    :param number: кол-во объектов
    :param form_1: форма единственного числа
    :param form_2: форма множественного числа до 4 объектов
    :param form_3: форма множественного числа от 5 объектов
    """

    if number % 100 in (11, 12, 13, 14):
         nessesary_form = form_3
    elif number % 10 == 1:
        nessesary_form = form_1
    elif number % 10 in (2, 3, 4):
        nessesary_form = form_2
    else:
        nessesary_form = form_3
    return(f'{ nessesary_form}')


# Декоратор html
def html(*args,**kwargs):
    def decorator(decrated_function):
        def wrapper(input_value):
            result = decrated_function(input_value)
            result = f'>{result}'
            attribute = ''
            open_tag = ''
            close_tag = ''
            for i in args:
                open_tag = f'<{i}'
                close_tag = f'</{i}>'
            for k,v in kwargs.items():
                attribute += f' {k}="{v}"'
            result = open_tag + attribute + result + close_tag
            return result
        return wrapper
    return decorator