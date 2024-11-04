#работа со словарем
my_dict = {'Pasha':'отличник', 'Sofia':'ударник','Katya':'двоечник'}
print (my_dict)
print (my_dict['Sofia'])
my_dict['Olga'] = 'отличник'
print (my_dict)
my_dict.update({'Marina':'двоченик','Fedor':'ударник'})
print(my_dict)
val_1 = my_dict.pop('Olga')
print(my_dict)
print (val_1)
#работа с множеством
my_set = {2, 4.9, "no", "yes", "no", 4, False, -9.2, 4.9}
print (my_set)
my_set.add('hi!')
my_set.add(5)
print (my_set)
my_set.discard(-9.2)
print (my_set)