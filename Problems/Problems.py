##6.С клавиатуры вводятся N чисел.
##Составьте программу, которая определяет количество отрицательных,
## количество положительных и количество нулей среди введенных чисел.  
##Значение N вводится с клавиатуры.

z,p,n,counter=0,0,0,0
print("sisesta 5 num")
while counter<5:
    counter+=1
    a=int(input())
    if a>0:
        p+=1
    elif a<0:
        n+=1
    else:
        z+=1
print("positive",p)
print("nigative",n)
print("zero",z)



##16.Напишите программу, печатающую столбик строк такого вида:
##1 0 0 0 0 0 0 0 0
##0 2 0 0 0 0 0 0 0
##0 0 3 0 0 0 0 0 0
##0 0 0 4 0 0 0 0 0
##0 0 0 0 5 0 0 0 0
##0 0 0 0 0 6 0 0 0
##0 0 0 0 0 0 7 0 0
##0 0 0 0 0 0 0 8 0
##0 0 0 0 0 0 0 0 9

#from math import*

for r in range(9):                            ##r=0,1,2,3,4,5,6,7,8,9
    for c in range(9):
        if r==c:
            print(r+1,end="")                 ## zna4enie indexa uveli4 na 1
        else:
            print(0,end="")
    print()
print()                                       ## perehod na novuju str


##23.В ЭВМ вводятся координаты N точек. Определить,
## сколько из них попадает в круг радиусом R с центром в точке (a,b).

N=int(input("sisestage punkite arv"))
R=int(input("ringi raadius"))
a,b=map(int,input("ringi keskpunkti koordinaadid").split())
k=0
for i in range(N):
    x,y=map(int,input("sisestage keskpunkti koordinaadid").split())
    if (x-a)**2+(y-b)**2<=R**2:
        k+=1
print(k,"punkti on ringis")


##12.В бригаде, работающей на уборке сена, имеется N сенокосилок.
##Первая сенокосилка работала m часов, а каждая следующая на 10 минут больше, чем предыдущая.
##Сколько часов проработала вся бригада?
#from math import*
##optiont.1

n=int(input("Niiduke kogus: "))
m=int(input("kui palju tootas 1ne: "))
tulemus=0
for i in range(n):
    tulemus+=m
    m+=1/6
print(f"{tulemus} tundi tootas kogu meeskond")

##option.2

N=int(input("kogus"))
m=int(input("Min"))
m*=60
summa=0
for summa in range(1,N):
    summa+=m
    m+=10
print(summa/60)

##10.Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.
###option.1
#from math import*

for i in range(1,5):
    a,b=map(int,input("sisesta num").split())
    if a==0 and b==0: break
    if a>b:
        print(f"{a} rohkem kui {b}")
        text+=" "+str(a)
    if a<b:
        print(f"{a} vahem kui {b}")
        text+=" "+str(b)
print(text)

##option2.
from math import* 
from random import *
text=""
for i in range(1,11):
    arv1=randint(-100,100)
    arv2=randint(-100,100)
    if arv1>arv2: 
        print(f"{arv1} on surem kui {arv2}") 
        text+=" "+str(arv1)
    elif arv2>arv1: 
        print(f"{arv2} on surem kui {arv1}")
        text+=" "+str(arv2)
    else:
        print(f"{arv1},{arv2} on vordsed")
print(text)
  
## 17.Напишите программу, печатающую столбик таблицу умножения такого вида:
##2*1=2
##2*2=4
##2*3=6
##2*4=8
##2*5=10
##2*6=12
##2*7=14
##2*8=16
##2*9=18

n=int(input("sisesta n:"))
for i in range(1,10):
    print(f"{n} *{i}={n * i}")
    
##Напишите программу, печатающую столбик таблицу умножения такого вида:
##Option.1
 #6   12  18  24  30  36  42  48  54  60 
 #7   14  21  28  35  42  49  56  63  70 
 #8   16  24  32  40  48  56  64  72  80 
 #9   18  27  36  45  54  63  72  81  90 
 #10  20  30  40  50  60  70  80  90 100 

from math import*

for r in range(1,11):                          ##r=0,1,2,3,4,5,6,7,8,9
    for c in range(1,11):
            print(str(r*c).center(4), end="")
    print()


## Option.2
r=0
c=0
while r<11:
    r+=1
    while c<11:
        c+=1
        print(str(r*c).center(4), end="")
    c=0                                         ##obnovlenie c opjat =0
    print()                                     ##/n


print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                      #pomenjal 4islo 0 na 1 potomu4to s 0 delat ne4ego
while True:
    try:
        a = (abs(int(input("Введите целое число => "))))     #ubral liwnuii skobki
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
                                                  ##raspolozenie peremennqh, znaki "=="
                                                  ## dobavil int(input) neuveren nadoli

    c=b=a                                         ##c=453,a=453,b=453
    paaris=0
    paaritu=0
    while b>0:
        if b%2==0:                               ##proverijaem esli delitsa na 2, esli da uveli4icaem paaris +1
            paaris+=1
        else:                                    ## esli else to ne4etnoe +1
            paaritu+=1
        b=b//10
    #b=0                                         ## otkidavaem drobnuju 4ast 453//10=polu4aem tolko 45 , 45 bolwe paaris uveli4ivaem+1 , 45 //10=4 4>0 S=1 4//10=0
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Переворачиваем* введённое число")
    print()
    b=0                                         ##c=453 a=453 b=0                                      4%10=4
    while a>0:                                  ##                                        n=5          4>0
        number =a%10                            ##  n=453%10-->n=3                        a=4          n=4
        a = a//10                               ##  a=453//10-->a=45                      b*10=30      a=0
        b = b*10                                ##  b*=10>=0 sledujuwii wag b+=n--/=3     b+n=35       b=350
        b+=number                               ##                                                     b=354
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз")
    print()
                                                         ##dobavil skobki tam gde nado bqlo, i ubral tam gde ne nado bqlo, dobail ""                                      # peredcezenie peremennqh
    if c%2==0:
       
        print("c -чётное число. Делим на 2.")
    else:
        print("c - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c!=1:
        if c%2==0:
            c=c/2
        else:
            c=(3*c+1)/2
        print(int(c), end=" ")
    print()
    print("Гипотеза верна")
