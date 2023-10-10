# -*- coding: cp1251 -*-
#1
print('Введите вид питомца')
vid = input()
print('введите возраст:')
age = input()
print('Введите кличку питомца')
nameP = input()
print('Это', vid, 'по кличке', nameP, sep = ' ', end = '. ')
print('Возраст', age, sep = ':', end = '.')

#2
#Homo habilis, H. erectus, H. rudolfensis, H. georgicus, H. georgicus, H. ergaster, H. antecessor, H. cepranensis, H. heidelbergensis, H. neanderthalensis, H. rhodesiensis, H. sapiens sapiens, H. sapiens idaltu,H. floresiensis 
i = 1
otv = ''
while i <= 13:
    print('Введите этап развития', i)
    if i == 13:
        otv = otv + input() 
    else:
        otv = otv + input() + '=>'
    i += 1
print(otv)   
