a=input("Enter letter: ")
vowels="a e i o u A E I O U".split(' ')
flag=0
for l in vowels:
    if a==l:
        flag=1
    elif (a=='y' or a=='Y'):
        flag=2
if flag==1:
    print(f'{a} is a vowel.')
elif flag==2:
    print('sometimes y is a vowel, sometimes it is a consonant.')
else:
    print(f'{a} is a consonant')
print(vowels)

###############################################################################

sides=int(input("Enter number of sides: "))
flag=0
dict={3:'Triangle',4:'Square',5:'Pentagon',6:'Hexagon',7:'Heptagon',8:'Octagon',9:'Nonagon',10:'Decagon'}
for a in dict.keys():
    if sides==a:
        flag=1
if flag==1:
    print(f'The shape is {dict[sides]}')
else:
    print('wrong input')
    
###############################################################################

month=input('Enter month name: ').lower()
month_list='january,february,march,april,may,june,july,august,september,october,november,december'.split(',')
dict={}
lst='31,28 or 29,31,30,31,30,31,31,30,31,30,31'.split(',')
for i in range(0,12):
    dict[month_list[i]]=lst[i]
for mnt in dict.keys():
    if month==mnt:
        print(f'{month} has {dict[month]} days in it.')
if month not in dict.keys():
    print('Invalid month entered.')

###############################################################################

a=float(input('Enter side a: '))
b=float(input('Enter side b: '))
c=float(input('Enter side c: '))
if a==b or b==c or c==a:
    if a==b and b==c:
        print('Equilateral')
    else:
        print('Isosceles')
else:
    print('Scalene')

###############################################################################

date=input('Enter date (DD-MM-YYYY): ').split('-')

