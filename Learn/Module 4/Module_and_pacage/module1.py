# Пример модуля - файла выполняющего в себе определенные функции которые можно использовать в другом файле

# Модуль содержит функции get_summation_digits и get_multiplied_digits к которым можно обращаться из других файлов
# и функцию main, выполняемую только при запуске внутри этого файла благодаря условию if __name__ == '__main__'

# Функция суммирующая все числа из которых состоит число
def get_summation_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return  first + get_summation_digits(int(str_number[1:]))

# Функция перемножающая все числа из которых состоит число
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) == 1:
        return first
    else:
        return  first * get_multiplied_digits(int(str_number[1:]))

# Пример выполнения внутри функции main
def main():
    print(get_summation_digits(325))
    print(get_multiplied_digits(522))
    print(get_multiplied_digits(2045))
    print(get_multiplied_digits(25275))

# Условие выполнения функции main только при запуске из этого файла, при внешнем вызове выполняется условие else
if __name__ == '__main__':
    main()
else:
    print("Внешний вызов module1.py")