import random

def Russian_Roulette():
    print("                                                         RUSSIAN ROULETTE")
    

    while True:
        Difficulty = str(input("Select difficulty\n1 Bala\n2 Balas\n3 Balas\n"))
        Rounds = 0  # Numero de cabinas vacías. Si llega a 0, significará que sobrevivió y ganó el juego.
        if (Difficulty == '1 Bala') or (Difficulty == '1') or (Difficulty == '1 bala'):
            Dif = 1 
            Rounds = 5
        elif (Difficulty == '2 Balas') or (Difficulty == '2') or (Difficulty == '2 balas'):
            Dif = 2
            Rounds = 4
        elif (Difficulty == '3 Balas') or (Difficulty == '3') or (Difficulty == '3 balas'):
            Dif = 3
            Rounds = 3
        else:
            print("Valor no válido, intente otra vez")
            continue

        i = 0
        Revolver = [0, 0, 0, 0, 0, 0]  # Lista que contendrá entre sus 6 valores el 1 que equivale a la bala
        Masquerade = ['X', 'X', 'X', 'X', 'X', 'X']

        while i < Dif:
            Buena = random.randint(0, 5)  # Variable para asignar bala al azar en 1 de los 6 espacios
            if Revolver[Buena] == 1:
                i -= 1
            Revolver[Buena] = 1  # En la posición que va del 0 al 5 (1 al 6), se almacenará un 1 en lugar de un 0
            
            i += 1

        Turn = 0  # Indica el número de la cabina del Turno actual. Si es [0], equivale a la primera cabina. No debería ser mayor a 5
        
        while Rounds > -1:  # Condicional para que pueda bajar hasta 0 sin alterar el programa
            Masquerade[Turn] = 'O'  # Cambia el valor en la posición Turn a 'O'
            print(f"Cylinder Size:{Masquerade},  {Rounds} Rounds Left\n\nCurrent Chamber: {Masquerade[Turn]}")
            shot = str(input("                                                         ¿Pass or Shoot?\n                                                      1.Pass          2.Shoot\n                                                               "))
            if (shot == '1') or (shot == 'Pass') or (shot == 'pass'):  # Se omite el espacio actual, se pasa al siguiente
                print("                                                             Next Round:")
                Masquerade[Turn] = 'X'  # Restaura el valor anterior a 'X'
                Turn += 1  # Se suma 1 al Turno, osea que se pasa al cartucho siguiente
            if (shot == '2') or (shot == 'Shoot') or (shot == 'shoot'):  # Se dispara la bala. 2 Posibles resultados
                if Revolver[Turn] == 0:  # Si la ranura esta vacía, sin bala.
                    print("                                                         You're Save. Next Round:")
                    Rounds -= 1  # Se reduce número de turnos, 1 espacio menos para ganar
                if Revolver[Turn] == 1:  # Si la ranura contiene la bala
                    print("                                                             Dead")
                    print(f"You had {Rounds} Rounds left")  # Se imprime cuantas ranuras faltaban para ganar
                    break
                Revolver.pop(Turn)  # Se elimina la ranura. Se mantiene en mismo lugar
                Masquerade.pop(Turn)
            if (Turn > (len(Revolver)-1)):  # Cuando el valor del número de ranuras, por cuestiones de suma, excede la longitud de la ranura
                Turn = 0  # Se regresa el valor a 0, puesto que es el inicio de las balas restantes 
            if Rounds <= 0:  # Si las Rondas llegan a 0, se gana
                print("                                                         Congratulations, You saved your life")
                break
        choice = str(input("                                                         ¿Another Shot?\n                                                         Say YES or NO\n                                                         "))
        if (choice == 'NO') or (choice == 'no'):  # Se escoge si volver a jugar o no
            break

Russian_Roulette()
