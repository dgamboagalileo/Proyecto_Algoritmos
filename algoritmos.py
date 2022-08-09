import pandas
import re
import math
from math import e

#Evaluación REGREX
def evaluate_Fx(str_equ, valX):
  x = valX
  #strOut = str_equ
  strOut = str_equ.replace("x", '*(x)')
  strOut = strOut.replace("^", "**")
  out = eval(strOut)
  print(strOut)
  return out

#Deferencias finitas para derivadas
def evaluate_derivate_fx(str_equ, x, h):
  strOut = str_equ.replace("x", '*(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = "-4*(" + strOut + ")"
  out = eval(strOut)
  
  strOut = str_equ.replace("x", '*(x + 2*h)')
  strOut = strOut.replace("^", "**")
  out = out + eval(strOut)
  
  strOut = str_equ.replace("x", '*(x)')
  strOut = strOut.replace("^", "**")
  strOut = "3*(" + strOut + ")"
  out = out + eval(strOut)
  
  out = -out/(2*h)
  print(out)
  return out


#Extrapolación de Richardson

def extra_richards(str_equ, x, h):
  
  #f(x)
  strOut=str_equ.replace("x", x)
  strOut = strOut.replace("^", "**")
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**0", "math.exp(0)")
  #strOut=strOut.replace("e**-1", "*math.exp(-1)")
  strOut="-3*("+strOut+")"
  out=eval(strOut)
  a=out
  
  strOut = str_equ.replace("x", '(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")
  #strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
  strOut="4*("+strOut+")"
  out=eval(strOut)
  b=out
  
  
  strOut = str_equ.replace("x", '(x + 2*h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.1)", "math.exp(-(0 + 0.1))")
  #strOut=strOut.replace("e**-(1 + 0.1)", "*math.exp(-(1 + 0.1))")
  strOut="-1*("+strOut+")"
  out=eval(strOut)
  c=out
  
  fh = (a+b+c)/(2*float(h))
  
  strOut=str_equ.replace("x", x)
  strOut = strOut.replace("^", "**")
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-0", "math.exp(-0)")
  #strOut=strOut.replace("e**-1", "*math.exp(-1)")
  strOut="-3*("+strOut+")"
  out=eval(strOut)
  d=out
  
  strOut = str_equ.replace("x", '(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")
  #strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
  strOut="-1*("+strOut+")"
  out=eval(strOut)
  f=out
  #f=-0.364218
  
  strOut = str_equ.replace("x", '(x + h/2)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.025)", "math.exp(-(0 + 0.025))")#1 − math.exp(-(0 + 0.05))
  #strOut=strOut.replace("e**-(1 + 0.025)", "*math.exp(-(1 + 0.025))")
  strOut="4*("+strOut+")"
  out=eval(strOut)
  e=out
  

  fhmed = (d+e+f)/float(h)
  
  fr = (4*fhmed-fh)/3
  
  TableOut = pandas.DataFrame({'Derivada fr': fr}, index=[0])  #'f(h)': fh, 'f(h/2)': fhmed, 'f(r)': fr, 'fx':a,'fx+h':b,'fx+2h':c,'fx':d,'fx+h/2':e,'-fx+h':f
  return TableOut

#Extrapolación de Richardson CDF

def extra_richardsCDF(str_equ, x, h):
  
  #f(x+h)
  strOut = str_equ.replace("x", '(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")
  #strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
  strOut="("+strOut+")"
  out=eval(strOut)
  a=out
  
  
  strOut = str_equ.replace("x", '(x - h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.1)", "math.exp(-(0 + 0.1))")
  #strOut=strOut.replace("e**-(1 + 0.1)", "*math.exp(-(1 + 0.1))")
  strOut="-1*("+strOut+")"
  out=eval(strOut)
  b=out
  
  fh = (a+b)/(2*float(h))
  
  strOut = str_equ.replace("x", '(x + h/2)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.025)", "math.exp(-(0 + 0.025))")#1 − math.exp(-(0 + 0.05))
  #strOut=strOut.replace("e**-(1 + 0.025)", "*math.exp(-(1 + 0.025))")
  strOut="("+strOut+")"
  out=eval(strOut)
  c=out
  
  strOut = str_equ.replace("x", '(x - h/2)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.025)", "math.exp(-(0 + 0.025))")#1 − math.exp(-(0 + 0.05))
  #strOut=strOut.replace("e**-(1 + 0.025)", "*math.exp(-(1 + 0.025))")
  strOut="-1*("+strOut+")"
  out=eval(strOut)
  d=out
  
  fhmed = (c+d)/float(h)
  
  fr = (4*fhmed-fh)/3
  
  TableOut = pandas.DataFrame({'Derivada fr': fr}, index=[0]) #'f(h)': fh, 'f(h/2)': fhmed, 'f(r)': fr, 'fx+h':a,'fx-h':b,'fx+h/2':c,'fx-h/2':d
  return TableOut



#Deferencias finitas para derivadas
def evaluate_derivate_fx(str_equ, x, h):
      strOut = str_equ.replace("x", '*(x + h)')
      strOut = strOut.replace("^", "**")
      strOut = "-4*(" + strOut + ")"
      out = eval(strOut)

      strOut = str_equ.replace("x", '*(x + 2*h)')
      strOut = strOut.replace("^", "**")
      out = out + eval(strOut)

      strOut = str_equ.replace("x", '*(x)')
      strOut = strOut.replace("^", "**")
      strOut = "3*(" + strOut + ")"
      out = out + eval(strOut)

      out = -out/(2*h)
      print(out)
      return out

#Diferencias finitas dos puntos
def finite_difference(str_equ, x, h):
    
    #-f(x)
    strOut=str_equ.replace("x", x) #x^2 + 1= 2^2 + 1;   1 − e^−0
    strOut =strOut.replace("^", "**") #2^2 + 1 + 1= 2**2 + 1;    1 − e**−0
    strOut="-1*("+strOut+")"#2**2 + 1=-(2**2 + 1);    -(1 − e**−0)
    #strOut=strOut.replace("e**-0", "math.exp(-0)")# -(1 − e**−0)= -(1 − math.exp(-0))
    #strOut=strOut.replace("e**-1", "*math.exp(-1)")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)#-5 #-(1 − math.exp(-0))
    
    #f(x+h)
    strOut = str_equ.replace("x", '(x + h)')#x^2 + 1= (x+h)^2 + 1;    1 − e^−(x+h)
    strOut = strOut.replace("^", "**")#x^2 + 1= (x+h)**2 + 1;     1 − e**−(x+h)
    strOut = strOut.replace("x", x)#(x+h)**2 + 1=(2+h)**2 + 1;   1 − e**−(0+h)
    strOut = strOut.replace("h", h)#(2+h)**2 + 1=(2+0.1)**2 + 1;    1 − e**−(0+0.05)
    #strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")#1 − math.exp(-(0 + 0.05))
    #strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)+out#f(x+h)-f(x)=5.41+(-5)=0.41
    difAdelante = out/float(h)#(f(x+h)-f(x))/h=0.41/0.1
    
    #Hacía atras
    strOut=str_equ.replace("x", x)
    strOut = strOut.replace("^", "**")
    #strOut=strOut.replace("e**-0", "math.exp(-0)")
    #strOut=strOut.replace("e**-1", "*math.exp(-1)")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)
    
    strOut = str_equ.replace("x", '(x - h)')
    strOut = strOut.replace("^", "**")
    strOut = strOut.replace("x", x)
    strOut = strOut.replace("h", h)
    strOut="-1*("+strOut+")"
    #strOut=strOut.replace("e**-(0 - 0.05)", "math.exp(-(0 - 0.05))")
    #strOut=strOut.replace("e**-(1 - 0.05)", "*math.exp(-(1 - 0.05))")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)+out
    difAtras = out/float(h)
    
    #Central
    strOut = str_equ.replace("x", '(x + h)')
    strOut = strOut.replace("^", "**")
    strOut = strOut.replace("x", x)
    strOut = strOut.replace("h", h)
    #strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")
    #strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)
    
    strOut = str_equ.replace("x", '(x - h)')
    strOut = strOut.replace("^", "**")
    strOut = strOut.replace("x", x)
    strOut = strOut.replace("h", h)
    strOut="-1*("+strOut+")"
    #strOut=strOut.replace("e**-(0 - 0.05)", "math.exp(-(0 - 0.05))")
    #strOut=strOut.replace("e**-(1 - 0.05)", "*math.exp(-(1 - 0.05))")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)+out
    
    difCentral=out/(2*float(h))
    
    TableOut = pandas.DataFrame({'Hacia adelante':difAdelante, 'Hacia atras':difAtras, 'Centrales': difCentral}, index=[0])
    return TableOut


#Deferencias finitas para derivadas
def evaluate_derivate_fx(str_equ, x, h):
      strOut = str_equ.replace("x", '*(x + h)')
      strOut = strOut.replace("^", "**")
      strOut = "-4*(" + strOut + ")"
      out = eval(strOut)

      strOut = str_equ.replace("x", '*(x + 2*h)')
      strOut = strOut.replace("^", "**")
      out = out + eval(strOut)

      strOut = str_equ.replace("x", '*(x)')
      strOut = strOut.replace("^", "**")
      strOut = "3*(" + strOut + ")"
      out = out + eval(strOut)

      out = -out/(2*h)
      print(out)
      return out

#Diferencias finitas tres puntos
def finite_difference3(str_equ, x, h):
   
   #f(x)
  strOut=str_equ.replace("x", x)
  strOut = strOut.replace("^", "**")
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**0", "math.exp(0)")
  #strOut=strOut.replace("e**-1", "*math.exp(-1)")
  strOut="-3*("+strOut+")"
  out=eval(strOut)
  a=out
  
  strOut = str_equ.replace("x", '(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")
  #strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
  strOut="4*("+strOut+")"
  out=eval(strOut)
  b=out
  
  
  strOut = str_equ.replace("x", '(x + 2*h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.1)", "math.exp(-(0 + 0.1))")
  #strOut=strOut.replace("e**-(1 + 0.1)", "*math.exp(-(1 + 0.1))")
  strOut="-1*("+strOut+")"
  out=eval(strOut)
  c=out
  
  ffdf = (a+b+c)/(2*float(h))
  
  
  #f(x)
  strOut=str_equ.replace("x", x)
  strOut = strOut.replace("^", "**")
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**0", "math.exp(0)")
  #strOut=strOut.replace("e**-1", "*math.exp(-1)")
  strOut="3*("+strOut+")"
  out=eval(strOut)
  d=out
  
  strOut = str_equ.replace("x", '(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")
  #strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
  strOut="4*("+strOut+")"
  out=eval(strOut)
  e=out
  
  
  strOut = str_equ.replace("x", '(x + 2*h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.1)", "math.exp(-(0 + 0.1))")
  #strOut=strOut.replace("e**-(1 + 0.1)", "*math.exp(-(1 + 0.1))")
  strOut="("+strOut+")"
  out=eval(strOut)
  f=out
  
  fbdf = (a+b+c)/(2*float(h))
  
  TableOut = pandas.DataFrame({'Hacia adelante':ffdf, 'Hacia atras':fbdf}, index=[0])
  return TableOut


def finite_difference3(str_equ, x, h):
   
   #f(x)
  strOut=str_equ.replace("x", x)
  strOut = strOut.replace("^", "**")
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**0", "math.exp(0)")
  #strOut=strOut.replace("e**-1", "*math.exp(-1)")
  strOut="-3*("+strOut+")"
  out=eval(strOut)
  a=out
  
  strOut = str_equ.replace("x", '(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")
  #strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
  strOut="4*("+strOut+")"
  out=eval(strOut)
  b=out
  
  
  strOut = str_equ.replace("x", '(x + 2*h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.1)", "math.exp(-(0 + 0.1))")
  #strOut=strOut.replace("e**-(1 + 0.1)", "*math.exp(-(1 + 0.1))")
  strOut="-1*("+strOut+")"
  out=eval(strOut)
  c=out
  
  ffdf = (a+b+c)/(2*float(h))
  
  
  #f(x)
  strOut=str_equ.replace("x", x)
  strOut = strOut.replace("^", "**")
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**0", "math.exp(0)")
  #strOut=strOut.replace("e**-1", "*math.exp(-1)")
  strOut="3*("+strOut+")"
  out=eval(strOut)
  d=out
  
  strOut = str_equ.replace("x", '(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")
  #strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
  strOut="4*("+strOut+")"
  out=eval(strOut)
  e=out
  
  
  strOut = str_equ.replace("x", '(x + 2*h)')
  strOut = strOut.replace("^", "**")
  strOut = strOut.replace("x", x)
  strOut = strOut.replace("h", h)
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  #strOut=strOut.replace("e**-(0 + 0.1)", "math.exp(-(0 + 0.1))")
  #strOut=strOut.replace("e**-(1 + 0.1)", "*math.exp(-(1 + 0.1))")
  strOut="("+strOut+")"
  out=eval(strOut)
  f=out
  
  fbdf = (a+b+c)/(2*float(h))
  
  TableOut = pandas.DataFrame({'Hacia adelante':ffdf, 'Hacia atras':fbdf}, index=[0])
  return TableOut


### Método de Trapezoide 
def metodo_trapezoide(str_equ,a,b,n):
  
  #f(a)
  strOut=str_equ.replace("x", a)
  strOut = strOut.replace("^", "**")
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  strOut="("+strOut+")"
  out=eval(strOut)
  fa = float(out)
  
  a = float(eval(a))
  b = float(eval(b))
  n = float(n)
  x_i = 0
  
  s = float(fa)
  h = (b-a)/n
  arrayIters = []
  arrayF_x = []
  arrayfXi = []
  arrayXi = []
  arrayS = []

  i = 0
  while(i < n):
    print("...")
    
    #f(xi)
    x_i = str(a + h * i)
    strOut=str_equ.replace("x", x_i)
    strOut = strOut.replace("^", "**")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    strOut="("+strOut+")"
    out=eval(strOut)
    fxi = out
    
    if(i <= 0):
      s = float(fa)
    else:
      s = float(s + 2*fxi)
    
    arrayIters.append(i)
    arrayXi.append(x_i)
    arrayfXi.append(fxi)
    arrayS.append(s)
    solution = [i, x_i, fxi, s]
    i = i + 1
    
  
  x_i=b
  b= str(b)
  strOut=str_equ.replace("x", b)
  strOut = strOut.replace("^", "**")
  strOut=strOut.replace("sin", "math.sin")
  strOut=strOut.replace("sen", "math.sin")
  strOut="("+strOut+")"
  out=eval(strOut)
  fxi = out
  s = s + fxi
  
  arrayIters.append(n)
  arrayXi.append(x_i)
  arrayfXi.append(fxi)
  arrayS.append(s)
  solution = [i, x_i, fxi, s]
  
  s = s * h/2
  arrayIters.append("-")
  arrayXi.append("-")
  arrayfXi.append("S =")
  arrayS.append(s)
  solution = [i, x_i, fxi, s]

  print("Finalizo...")
  TableOut = pandas.DataFrame({'Iter':arrayIters, 'Xi':arrayXi, 'fxi': arrayfXi, 's': arrayS })
  #TableOut = pandas.DataFrame({'a':a}, index=[0])
  return TableOut

## Metodo de Simpson
def metodo_simpson(str_equ,a,b,n):
    #f(a)
    strOut=str_equ.replace("x", a)
    strOut = strOut.replace("^", "**")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    strOut="("+strOut+")"
    out=eval(strOut)
    fa = float(out)
    
    a = float(eval(a))
    b = float(eval(b))
    n = float(n)
    x_i = 0

    s = float(fa)
    h = (b-a)/n
    arrayIters = []
    arrayF_x = []
    arrayfXi = []
    arrayXi = []
    arrayS = []
   
    i = 0
    while(i < n):
        print("...")
        #f(xi)
        x_i = str(a + h * i)
        strOut=str_equ.replace("x", x_i)
        strOut = strOut.replace("^", "**")
        strOut=strOut.replace("sin", "math.sin")
        strOut=strOut.replace("sen", "math.sin")
        strOut="("+strOut+")"
        out=eval(strOut)
        fxi = out
    
        if(i % 2==0):
          s = float(s + 2*fxi)
        else:
          s = float(s + 4*fxi)
    
        arrayIters.append(i)
        arrayXi.append(x_i)
        arrayfXi.append(fxi)
        arrayS.append(s)
        solution = [i, x_i, fxi, s]
        i = i + 1
        
    x_i=b
    b= str(b)
    strOut=str_equ.replace("x", b)
    strOut = strOut.replace("^", "**")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    strOut="("+strOut+")"
    out=eval(strOut)
    fxi = out
    s = s + fxi

    arrayIters.append(n)
    arrayXi.append(x_i)
    arrayfXi.append(fxi)
    arrayS.append(s)
    solution = [i, x_i, fxi, s]

    s = s * h/3
    arrayIters.append("-")
    arrayXi.append("-")
    arrayfXi.append("S =")
    arrayS.append(s)
    solution = [i, x_i, fxi, s]
    
    print("Finalizo...")
    TableOut = pandas.DataFrame({'Iter':arrayIters, 'Xi':arrayXi, 'fxi': arrayfXi, 's': arrayS })
    return TableOut

#def add(a, b):
  #a = int(a)
  #b = int(b)
  #resultado = a + b
  #return "El resultado es: " + str(resultado)

#Resolverdor de Newton
def newtonSolverX(x0, f_x, eps):
  x0 = float(x0)
  eps = float(eps)
  xn = x0
  error = 1
  arrayIters = []
  arrayF_x = []
  arrayf_x = []
  arrayXn = []
  arrayErr = []
  
  i = 0
  h = 0.000001
  while(error > eps):
    print("...")
    x_n1 = xn - (evaluate_Fx(f_x, xn)/evaluate_derivate_fx(f_x, xn, h))
    error = abs(x_n1 - xn)
    i = i + 1
    xn = x_n1
    arrayIters.append(i)
    arrayXn.append(xn)
    arrayErr.append(error)
    solution = [i, xn, error]

  print("Finalizo...")
  TableOut = pandas.DataFrame({'Iter':arrayIters, 'Xn':arrayXn, 'Error': arrayErr})
  return TableOut

def add(a, b):
  a = int(a)
  b = int(b)
  resultado = a + b
  return "El resultado es: " + str(resultado)