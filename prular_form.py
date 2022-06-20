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
