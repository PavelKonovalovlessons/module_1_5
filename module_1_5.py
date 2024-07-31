immutable_var = 1, 'string', True, 2.5

print(immutable_var)

# immutable_var[0] = 2
# кортежи в пайтон являются не изменяемыми структурами данных!

mutable_list = [1, 2, 3]
print(mutable_list)
mutable_list[0] = 100
mutable_list[1] = 'Turtle'
mutable_list[2] = False
print(mutable_list)