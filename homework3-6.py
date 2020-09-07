# Реализовать функцию int_func(), принимающую слово из маленьких латинских
# букв и возвращающую его же, но с прописной первой буквой. Например,
# print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Сделать вывод исходной строки, но каждое слово должно начинаться
# с заглавной буквы. Необходимо использовать написанную ранее функцию
# int_func()

def my_title(string=''):
    """The function takes a string of lowercase letters of the latin alphabet.
    Returns a string starting with a capital letter.
    """
    if string == '':
        string = input(
            'Enter a string of lowercase letters of the latin alphabet: ')
    if not string.isalpha():
        print(f'Input error type 1! "{string}" contains characters other '
              f'than letters!')
        return
    for i in range(len(list(string))):
        if ord(list(string)[i].lower()) in range(97, 123):
            i += 1
        else:
            print(f'Input error type2! "{string}" contains non-Latin letters!')
            return
    return (string.title())


def my_alltitle(text=''):
    if text == '':
        text = list(input(
            'Enter a string of lowercase word of the latin alphabet: ').split())
    for i in range(len(text)):
        text[i] = my_title(text[i])
    return ' '.join(text)


print(my_alltitle())
