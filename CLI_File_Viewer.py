from functions import typer
from functions import cls
import schedule
import time
import sys 
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def typer(string,timer=(0.03),remove="no"):
    for c in string:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(timer)
    if remove=="yes":
        cls()

def errormsg():
    cls()
    typer("No file detected! \n")
    exit()

file = sys.argv[1] if len(sys.argv)>1 else errormsg()
def orig():
            with open(file, 'r') as f:
                original= f.read()
                typer(original,0.0000001,"no")

def displayfile(file,type='loop'):
    if type=="changes":
        cls()
        with open(file, 'r') as f:
                original= f.read()
                typer(original,0.001,"no")  
        while 1:
            with open(file, 'r') as f:
                new= f.read()
                if original!=new:
                    original=new
                    cls()
                    orig()
    if type=="loop":
        while 1:
            with open(file, 'r') as f:
                t= f.read()
                typer(t,0.0000001,"no")
                time.sleep(5)
                cls()

if __name__ == "__main__":
    cls()
    displaytype = str(input("'changes' or 'loop'\n\nType here: "))
    displayfile(file,displaytype)


