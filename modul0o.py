import sys
def menu (n,d,m,t):
    print("ingrese la operacion que desea realizar")
    print("\t 1. reporte")
    print("\t 2. cambio de tipo fondo")
    print("\t 3. ahorros en fondo mutuo")
    print("\t 4. salir")
    o=input()
    if o=="1":
        reporte(n,d,m,t)
    if o=="2":
        cambio(n,d,m,t)
    if o=="3":
        ahorro(n,d,m,t)
    if o=="4":
        salir(n,d,m,t)

def reporte(n,d,m,t):
    print("Ud. se ha identificado como:", n)
    print("con DNI:", d)
    print("con monto:", m)
    print("con tipo de fondo:",t)
    menu(n,d,m,t)
    
def cambio(n,d,m,t):
        print("Ud. esta en el:", t)
        print("¿A que tipo de fondo desea cambiar?")
        print("\t 1. fondo1")
        print("\t 2. fondo2")
        print("\t 3. fondo3")
        op=input()
        if op=="1":
            print("Ud se ha cambiado a fondo 1")
            t="fondo1"
        if op=="2":
            print("Ud se ha cambiado a fondo 2")
            t="fondo2"
        if op=="3":
            print("Ud se ha cambiado a fondo 3")
            t="fondo3"
        menu(n,d,m,t)
def ahorro(n,d,m,t):
    m=float(input("ingrese el monto:"))
    nm=int(input("ingrese el numero de meses:"))
    if t=="fondo1":
        at=m+(m*0.02*nm)
        am=at/nm
        print("su ahorro total es:",at)
        print("su ahorro mensual es:", am)
        reporte(n,d,m,t)
        
    if t=="fondo2":
        at=m+(m*0.04*nm)
        am=at/nm
        print("su ahorro total es:",at)
        print("su ahorro mensual es:", am)
        reporte(n,d,m,t)
    if t=="fondo3":
        at=m+(m*0.07*nm)
        am=at/nm
        print("su ahorro total es:",at)
        print("su ahorro mensual es:", am)
        reporte(n,d,m,t)
    
def salir(n,d,m,t):
    print("¿esta seguro que desea salir?")
    o1=input()
    if o1=="si":
        print("el programa se esta cerrando")
        sys.exit(1)
    if o1=="no":
        menu(n,d,m,t)
                
                
            
