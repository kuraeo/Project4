# while True:
#     a = int(input("A "))
#     try:
#         c = 10 / a
#         #c = b / a
#         break
#     except ZeroDivisionError:
#         print("Ділення на 0 заборонено, введіть а ще раз")
#     except NameError:
#         print("Змінну ми не знаємо")
#     except ValueError:
#         print("ValueError")
#     else:
#         print("TRY - виконався")
#         break
#     finally:
#         print("Виконається завжди!")
#
# print(f"C = {c}")

# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"Sorry, we can't work with {type(var_1)}")
#     else:
#         return var_1
#
# first_var = '10'
# checker(first_var)

# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built!"
#
# def checker_material(material, limit_material):
#     if material > limit_material:
#         return "enough material"
#     else:
#         raise BuildingError(material)
#
# material = 123
# print(checker_material(material, 300))


import sys
# print(sys.executable)
# print(sys.version)
# print(sys.platform)
# print(sys.modules)
# for name, module_path in sys.modules.items():
#     print(name, module_path)
#
# for _ in dir(__builtins__):
#     print(_)
#
#     print(help("tuple"))




# my_lst = [1, 2 , 3, 4, 5]
# iterator = iter(my_lst)
#
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# a = list(range(1, 10))
# a = a.__iter__()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())



class Counter:
    def __init__(self, start, stop):
        self.i = start
        self.j = stop

    def __iter__(self):
        self.i = self.i - 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.j - 1:
            raise StopIteration
        return self.i

count = Counter(5, 10)
for i in count:
    print(i)



