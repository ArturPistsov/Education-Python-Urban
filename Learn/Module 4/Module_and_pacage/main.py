# Импорт модулей или отдельных функций из них

# В одной директории с этим файлом есть файл "module1.py"

# Его содержимое можно целиком импортировать в этот файл
# import module1
# print(module1.get_summation_digits(6543))
# print(module1.get_multiplied_digits(2354))

# Можно импортировать его под новым коротким именем для обращения к нему
import module1 as m1
print(m1.get_summation_digits(5473))
print(m1.get_multiplied_digits(3642))

# Или импортировать только определенную функцию из module1
from module1 import get_summation_digits
print(get_summation_digits(3435))
from module1 import get_multiplied_digits
print(get_multiplied_digits(4873))

# Им также можно дать короткие имена
from module1 import get_summation_digits as get_sum
from module1 import get_multiplied_digits as get_mul

# В терминале можно увидеть сообщение о внешнем вызове module1.py
# это сообщение прописано в условии else условия if __name__ == '__main__' в файле module1.py
# вызывающим функцию main - все что помещено в эту функцию выполняется только при вызове в файле module1.py