# -*- coding: cp1251 -*-
#1
print('������� ��� �������')
vid = input()
print('������� �������:')
age = input()
print('������� ������ �������')
nameP = input()
print('���', vid, '�� ������', nameP, sep = ' ', end = '. ')
print('�������', age, sep = ':', end = '.')

#2
#Homo habilis, H. erectus, H. rudolfensis, H. georgicus, H. georgicus, H. ergaster, H. antecessor, H. cepranensis, H. heidelbergensis, H. neanderthalensis, H. rhodesiensis, H. sapiens sapiens, H. sapiens idaltu,H. floresiensis 
i = 1
otv = ''
while i <= 13:
    print('������� ���� ��������', i)
    if i == 13:
        otv = otv + input() 
    else:
        otv = otv + input() + '=>'
    i += 1
print(otv)   
