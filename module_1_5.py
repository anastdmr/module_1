immutable_var = (1, 2, [4,6], "DINO", True, 4.8)
print (immutable_var)
#попытка изменения значения
#immutable_var[0] = 2
#попытка будет неудачная, потому что кортеж - это неизменяемый объект
mutable_lis = [1, 4, "BINGO", 2.5]
print (mutable_lis)
mutable_lis[1] = 0
print (mutable_lis)