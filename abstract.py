import numpy as np


def printer(what_print):
    return print(what_print, end="\n\n\n")


"""
    Мы не используем классический(пайтон) генератор например value = np.array([0]*10) ибо он медленее
"""


# простое взаимодействие с массивом в нумипаи
value = np.array([x for x in range(1, 11)])
printer(value)

# меняет сам массив а не представление как в случае shape и reshape
value.resize(2, 5)
printer(value)
value.resize(5, 5, refcheck=False)  # он ещё может дописывать ахуеть
printer(value)

# транспонирование матрицы столбцы теперь строки
value = np.empty((3, 3), dtype="int32")
printer(value)
value = value.T
printer(value)

# ravel из матрицы делает векто или же список
a = np.zeros((5, 5))
a[4][2] = 999
printer(a)

value = np.ravel(a)
printer(value)

# заполнить рандомными значениями такого то типа
value = np.empty(10, dtype="int32")
print(value)

value = np.empty((3, 3, 3), dtype="int32")
print(value)

# по главной диагонали все 1 1 1 не важно какая матрица прямоугольная или еще какая
value = np.eye(4, 5)
print(value, end='\n\n\n')

# по главной диагонали все 1 1 1 матрица всегда квадратная
value = np.identity(5)
print(value, end="\n\n")

# матрица из 0
value = np.zeros((5, 5))
print(value)

# матрица из 1
value = np.ones((5, 5), dtype="bool")
printer(value)

# матрица из любых значений
value = np.full((3, 3), -10)
printer(value)

# матрица из строки блять Карл как угодно с запятыми и без, разделять на строки можно этим ;
value = np.mat("1, 2 3 4")
printer(value)
value = np.mat("1,2; 3, 4")
printer(value)
# можно списки засовывать и даже двумерно сразу
a = [1, 2, 3, 4]
a1, a2 = a[:2], a[2:4]
value = np.mat([(a1), (a2)])
printer(value)

# задаем свои значения на диоганаль
value = np.diag(a)
printer(value)
# и тут разъеб функция сама считает какие значения по центру
value = np.diag([(a1), (a2)])
printer(value)

# а это два списка в одну диагональ
value = np.diagflat([(a1), (a2)])
printer(value)

# снизу 1 а ОТ главной диагонали 0
value = np.tri(3)
printer(value)
# ===
data = np.array([x for x in range(25)]).reshape(5, 5)
printer(data)
# снизу наши значения а ОТ главной диагонали 0
value = np.tril(data)
printer(value)
# наоборот
value = np.triu(data)
printer(value)

# треугольная матрица на основе нашего списка
value = np.tril([1, 2, 3])
printer(value)

# слева умножает справа 1
value = np.vander([1, 2, 5])
printer(value)

# диапазон от чисел с плавающей запятой, можно и простые
a = np.arange(5)
print(a)
value = np.arange(0, 12.5, 0.5)
value = np.array(value).reshape(5, 5)
printer(value)

# start ------- stop делит всегда пополам значения
value = np.linspace(0, np.pi, 3)
printer(value)

# аналог верхнему, но все делает логорифмически умножая на 10
# и получает серединое значение возводя в корень
# то есть 1 в этом случае это 10 а 3,16 - корень квад. из 10
value = np.logspace(0, 1, 3)
printer(value)

# геометрическая прогрессия 1 - с чего начинаем 4 - до какого числа 3 - сколько значений
value = np.geomspace(1, 4, 3)
printer(value)

# создание копии матрицы
d = np.array([(1, 2), (3, 4)])
b = np.copy(d)
b[1] = 1000
print(b, d, sep='\n\n', end='\n\n\n')


def get_range(num):
    for i in range(1, num+1):
        yield i


# массив из любого итерируемого объекта
value = np.fromiter("popa griz", dtype='U1')
printer(value)
value = np.fromiter(get_range(10), dtype='int')
printer(value)

# массив из любого итерируемого объекта
value = np.fromstring("1, 2, 3", dtype='int', sep=', ')
printer(value)

# возвращает размеры
value = value.shape
printer(value)

# добавляет ось в начало
value = np.arange(32).reshape(8, 2, 2)
printer(value)
value = np.expand_dims(value, axis=0)
value = value.shape
printer(value)

# # удаление оси
# c = np.squeeze(value, axis=0)
# printer(value)
#
# # нормальное добавление оси
# c = value[np.newaxis, :, np.newaxis]  # двоеточие это данные, а np.newaxis там где нужна ось
# printer(value)

"""
    Объединение массивов 
"""

a = np.array([(1, 2), (3, 4)])
b = np.array([(5, 6), (7, 8)])
aa = np.fromiter(range(18), dtype='int32')
# объединение по горизонтали (создает новый массив)
con = np.hstack([a, b])
# объединение по вертикали (создает новый массив)
con_one = np.vstack([a, b])
printer(con)
printer(con_one)

# объединение по колонкам (создает новый массив)
con = np.column_stack([a, b])
printer(con)
# объединение по горизонтальным колонкам (создает новый массив)
con = np.row_stack([a, b])
printer(con)

# объединение данных в один массив по строке
con = np.r_[aa, 1, 223, [1, 2, 3]]
printer(con)
con = np.r_[np.array([1, 2, 3]), np.array([1, 2, 3])]
printer(con)
con = np.r_[[(1, 2), (3, 4)], [(5, 6)]]
printer(con)

# объединение данных в один массив по столбцу
con = np.c_[[3, 2, 1], [1, 2, 3]]
printer(con)
