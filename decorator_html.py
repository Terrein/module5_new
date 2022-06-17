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
@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))
