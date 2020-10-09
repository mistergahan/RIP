#-*- coding: utf-8 -*-
import argparse
import math
complete = 'y'
parser = argparse.ArgumentParser()
parser.add_argument("--A", help="Коэффициент А Биквадратного уравнения", type=float)
parser.add_argument("--B", help="Коэффициент B Биквадратного уравнения", type=float)
parser.add_argument("--C", help="Коэффициент C Биквадратного уравнения", type=float)
args = parser.parse_args()
print ("Введите коэффициенты А, В, С биквадратного уравнения Ах^4+Bx^2+C=0\n")
while complete == 'y':
    A = args.A
    B = args.B
    C = args.C
    if A == None and B == None and C == None:
        A = input('A= ')
        B = input('B= ')
        C = input('C= ')
    try:
        A = float(A)
        B = float(B)
        C = float(C)
    except ValueError:
        print('Введены некорректные символы, повторите ввод.')

if A==0:
    if B==0:
        if C==0:
            print ("x - любое число\n")
        else:
            print ("Корней нет\n")
    else:
        d=-C/B
        if d>0:
            print("x1=",-math.sqrt(d))
            print("\nx2=", math.sqrt(d))
        elif d<0:
            print ("Корней нет\n")
        else:
            print("x=0")
else:
    if B==0:
        if C==0:
            print("x=0")
        else:
            d=-C/A
            if d<0:
                print("Корней нет\n")
            else:
                print ("x1=", math.sqrt(math.sqrt(d)))
                print ("x2=", -math.sqrt(math.sqrt(d)))
    else:
        d=B*B-4*A*C
        if d<0:
            print("Корней нет")
        elif d==0:
            m=(-B+math.sqrt(d))/(2*A)
                    if m<0:
                        print("Корней нет")
                    elif m==0:
                        print("x=0")
                else:
                    print("x1=", math.sqrt(m))
                    print("\nx2=",-math.sqrt(m))
            else:
                m1=(-B+math.sqrt(d))/(2*A)
                m2=(-B-math.sqrt(d))/(2*A)
                if m1>0:
                    print("x1=", math.sqrt(m1))
                    print("x2=", -math.sqrt(m1))
                    if m2>0:
                        print("x3=", math.sqrt(m2))
                        print("x4=", -math.sqrt(m2))
                    elif m2==0:
                        print("x3=0")
                elif m1==0:
                    print("x1=0")
                    if m2>0:
                        print("x2=", math.sqrt(m2))
                        print("x3=", -math.sqrt(m2))
                    elif m2==0:
                        print("x2=0")
             else:
                    if m2>0:
                        print("x1=", math.sqrt(m2))
                        print("x2=", -math.sqrt(m2))
                    elif m2==0:
                        print("x1=0")
                    else:
                        print ("Корней нет")





