import tkinter as tk

# Функция принимающая входные параметры
def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

# Функция вывода результата
def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

# Функции арифметических операций
def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)
def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)
def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)
def dif():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

# Создание окна:
window = tk.Tk()

# Имя окна
window.title("Калькулятор")
# Размер окна
window.geometry("200x250")
# Ограничим изменение размеров окна
window.resizable(False, False)

# Создание элементов
button_add = tk.Button(window, text=" + ", width=4, height=2, command=add)
button_add.place(x=20, y=120)

button_sub = tk.Button(window, text=" - ", width=4, height=2, command=sub)
button_sub.place(x=60, y=120)

button_mul = tk.Button(window, text=" * ", width=4, height=2, command=mul)
button_mul.place(x=100, y=120)

button_dif = tk.Button(window, text=" / ", width=4, height=2, command=dif)
button_dif.place(x=140, y=120)

number1_entry = tk.Entry(window, width=26)
number1_entry.place(x=20, y=30)
number1 = tk.Label(window, text="Введите первое число")
number1.place(x=20, y=5)

number2_entry = tk.Entry(window, width=26)
number2_entry.place(x=20, y=80)
number2 = tk.Label(window, text="Введите второе число")
number2.place(x=20, y=55)

answer_entry = tk.Entry(window, width=26)
answer_entry.place(x=20, y=200)
answer = tk.Label(window, text="Ответ")
answer.place(x=20, y=175)

# цикл обновления событий, для обновление происходящего на экране
window.mainloop()

# Для формирования исполняемого файла необходимо выполнить в терминале команду auto-py-to-exe