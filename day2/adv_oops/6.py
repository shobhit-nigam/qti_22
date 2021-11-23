tot = len(dir())
import sys

lista = [100, 200, 300]
ia = 23

def funca():
    la = 100
    lb = 200
    return dir()

listx = dir()
print("available in entire code:\n", listx[tot:])
print("----")
listy = funca()
print("available in funca:\n", listy)
