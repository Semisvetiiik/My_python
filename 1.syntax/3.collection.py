# *** list ***

# сощдание пстого списка
my_list = []
my_list_2 = list()

# добавление объекта (в конец списка)
my_list.append(100)
my_list.append(77)
my_list.append("A")
my_list.append([1,2,3])

# обращение к элементам списка
my_list[0] = 5
my_list[-2] = 'B'


# чиение значений
element_value = my_list[1]

# удаление значений
# del my_list[-1]

# my_list.remove(5)

# a = my_list.pop(0)


# создание заполненного списка

my_list_2 = [10, 20, 30, 'A', "hello", True, 3.14, [1,2,3]]

# "длина" списка - количество элементов
# print(len(my_list_2))

# создание списка из строки
s = "Привет, мир!"
listFromStr = list(s)

# print(listFromStr)

# методы списка

# исходный список
x = [1,2,3,4,5]

# представление
y = x

# y[2] = 100

# копия
z = x.copy()

z[2] =100

# print(f"x: {x}; z: {z}")

# срез списка 

my_list = [10,20,30,40,50,60,70]

# прямой срез
slice_f = my_list[1:4] # с 1 индекса до 4 не вкл

slice_f = my_list[2:] # с 2 индекса до конца

slice_f = my_list[::2] # с самого начала до конца списка с шагом=2

slice_f = my_list[1:6:2] # с 1 индекса до 6 не вкл с шагом=2

#  обратный срез
slice_b = my_list[-1::-1] # с -1 индек до конца с шагом - одтн в обратном направл
 
slice_b = my_list[-3:-6:-1]


# print(slice_b)



# *** кортеж (tuple) ***

# неизменяемая (immutable) коллекция
my_tuple = (10, 20, 30)

# чтение данных 
el = my_tuple[-1]

# можно делать срез кортежи
el = my_tuple[-1:-3:-1]

# нельзя удалять значения
# del my_tuple[0]

# нельзя менять значения
# my_tuple[1] = 100

# нельзя добавлять элемент


# print(el)


# *** Словарь (dictionary) ***

# Создание словаря

my_dict = {1 : 100, 2:200, 3:777}
my_dict_2 = {'a':10, 'b':"hello", 'c':[1,2,3], 10:1000}

item = my_dict_2[10]
item = my_dict_2['a']


# пример с ловаря в кач.альтернативы

condition = 'key_2'

d = {'key_1':100, 'key_2':200}

my_dict_2['b'] = "python"

del my_dict_2[10]

my_dict_2["newKey"] = 777

# val = my_dict_2["key_2"]

# val = my_dict_2.get("newKey")
val = my_dict_2.get("Key_2", 0)

# print(val)

d_1 = {'a':10, 'b':20, 'c':30, 'd':40}

u_d_1 = {'b':200, 'd':1000}
u_d_2 = {'b':777, 'e':888}

# d_1.update(u_d_1)
d_1.update(u_d_2)

print(d_1)
