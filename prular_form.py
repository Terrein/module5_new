def plural_form(count, word_1,word2 = '',word3 = ''):
    """ возвращает корректную форму существительного
    в зависимости от переданного числа
    :param count: количество 
    :param word_1: слово для анализа
    :param word_2: другая форма слова (необязательный атрибут)
    :param word_3: другая форма слова (необязательный атрибут)
    """
    from pymorphy2 import MorphAnalyzer
    from transliterate import translit
    morph = MorphAnalyzer()
    expample_word = morph.parse(word_1)[0].normal_form
    transform_word = morph.parse(expample_word)[0]
    result = transform_word.make_agree_with_number(count).word
    translite_result = translit(result, 'ru', reversed = True)
    return translite_result

print(plural_form (115,'студентов'))



def plural_form_old(number, form_1, form_2, form_3):
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

print(1, plural_form_old(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form_old(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form_old(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form_old(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form_old(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form_old(125, 'яблоко', 'яблока', 'яблок'))