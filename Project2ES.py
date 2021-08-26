#Creado por Main_Cloro

import random


repeat = True

while repeat == True:
    value = random.randint(1,4)

    if value == 1:
        print("La frase es: Tu <persona> se ha <verbo> y un perro ha echo que se caiga a un <lugar>")
        a = input("Dime una persona ")

        b = input("Dime un verbo ")

        c = input("Dime un lugar ")

        print("Tu " + a + " se ha " + b + " y un perro ha echo que se caiga a un " + c)
    if value == 2:
        print("La frase es: Estoy enamorado de <persona>, es tan increible como agita su <sustantivo> y le queda muy bien llevar esa ropa sobre <tema>")
        d = input("Dime una persona ")

        e = input("Dime un sustantivo ")

        f = input("Dime un tema ( ͡° ͜ʖ ͡°) ")

        print("Estoy enamorado de " + d + ", es tan increible como agita su " + e + " y le queda muy bien llevar esa ropa sobre " + f)
    if value == 3:
        print("La frase es: Me encanta la historia de <evento historico>, mi parte favorita es cuando <evento concreto>, son <adgetivo>")
        g = input("Dime un evento historico\n")

        h = input("Dime un evento concreto\n")

        i = input("Dime un adgetivo\n")

        print("Me encanta la historia de " + g + " mi parte favorita es cuando " + h +", son " + i)
    if value == 4:
        print("\033[31m"+"Evento no programado"+"\033[39m")
    answ = input("Quieres jugar de nuevo? Hay mas opciones de frase! Si/No\n")
    
    if answ == "Si" or answ == "si":
        repeat = True
    else:
        repeat = False
