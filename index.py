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
def prular_form(count, word_1,word2 = '',word3 = ''):
    """ возвращает корректную форму существительного
    в зависимости от переданного числа
    :param count: количество 
    :param word_1: слово для анализа
    :param word_2: другая форма слова (необязательный атрибут)
    :param word_3: другая форма слова (необязательный атрибут)
    """
    from pymorphy2 import MorphAnalyzer
    morph = MorphAnalyzer()
    expample_word = morph.parse(word_1)[0].normal_form
    transform_word = morph.parse(expample_word)[0]
    result = transform_word.make_agree_with_number(count).word
    return result


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