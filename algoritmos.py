import pandas
import re
import math

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

#Diferencias finitas dos puntos
def finite_difference(str_equ, x, h):
    #Hacía adelante
    #a) x^2 + 1
    #b) 1 − e^−x
    #c)
    #d)
    #f)
    
    #Ecuación general 
    #(f(x+h)-f(x))/h
    
    #-f(x)
    strOut=str_equ.replace("x", x) #x^2 + 1= 2^2 + 1;   1 − e^−0
    strOut =strOut.replace("^", "**") #2^2 + 1 + 1= 2**2 + 1;    1 − e**−0
    strOut="-1*("+strOut+")"#2**2 + 1=-(2**2 + 1);    -(1 − e**−0)
    strOut=strOut.replace("e**-0", "math.exp(-0)")# -(1 − e**−0)= -(1 − math.exp(-0))
    strOut=strOut.replace("e**-1", "*math.exp(-1)")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)#-5 #-(1 − math.exp(-0))
    
    #f(x+h)
    strOut = str_equ.replace("x", '(x + h)')#x^2 + 1= (x+h)^2 + 1;    1 − e^−(x+h)
    strOut = strOut.replace("^", "**")#x^2 + 1= (x+h)**2 + 1;     1 − e**−(x+h)
    strOut = strOut.replace("x", x)#(x+h)**2 + 1=(2+h)**2 + 1;   1 − e**−(0+h)
    strOut = strOut.replace("h", h)#(2+h)**2 + 1=(2+0.1)**2 + 1;    1 − e**−(0+0.05)
    strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")#1 − math.exp(-(0 + 0.05))
    strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)+out#f(x+h)-f(x)=5.41+(-5)=0.41
    difAdelante = out/float(h)#(f(x+h)-f(x))/h=0.41/0.1
    
    #Hacía atras
    strOut=str_equ.replace("x", x)
    strOut = strOut.replace("^", "**")
    strOut=strOut.replace("e**-0", "math.exp(-0)")
    strOut=strOut.replace("e**-1", "*math.exp(-1)")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)
    
    strOut = str_equ.replace("x", '(x - h)')
    strOut = strOut.replace("^", "**")
    strOut = strOut.replace("x", x)
    strOut = strOut.replace("h", h)
    strOut="-1*("+strOut+")"
    strOut=strOut.replace("e**-(0 - 0.05)", "math.exp(-(0 - 0.05))")
    strOut=strOut.replace("e**-(1 - 0.05)", "*math.exp(-(1 - 0.05))")
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
    strOut=strOut.replace("e**-(0 + 0.05)", "math.exp(-(0 + 0.05))")
    strOut=strOut.replace("e**-(1 + 0.05)", "*math.exp(-(1 + 0.05))")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)
    
    strOut = str_equ.replace("x", '(x - h)')
    strOut = strOut.replace("^", "**")
    strOut = strOut.replace("x", x)
    strOut = strOut.replace("h", h)
    strOut="-1*("+strOut+")"
    strOut=strOut.replace("e**-(0 - 0.05)", "math.exp(-(0 - 0.05))")
    strOut=strOut.replace("e**-(1 - 0.05)", "*math.exp(-(1 - 0.05))")
    strOut=strOut.replace("sin", "math.sin")
    strOut=strOut.replace("sen", "math.sin")
    #print(strOut)
    out=eval(strOut)+out
    
    difCentral=out/(2*float(h))
    
    TableOut = pandas.DataFrame({'Hacía adelante':difAdelante, 'Hacía atras':difAtras, 'Centrales': difCentral}, index=[0])
    return TableOut

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
