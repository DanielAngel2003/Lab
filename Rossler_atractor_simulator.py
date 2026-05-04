
'''
Diario del Programador 03/05/26:

17:35 - Aunque odio admitirlo, he procrastinado esto. Pero
ahora que lo recuerdo, lo voy a hacer y tomaré inspiración de algo
que ví en un video.
Para nuestra materia de Biología, se nos pidió que vieramos la simulación
del 'Atractor de Rossler'. ¿Sé que es? No, ni idea. Primera vez que lo oigo.
Pero lo descubriré y revisaré fuentes externas.
'''

### Al parecer, este código me permite visualizar el atractro de rossler
### con la librería turtle.

### Turtle parece ser una librería de 
import turtle


# Visualizador, Pantalla
window = turtle.Screen()
turtle.setup(675, 1200)
turtle.setworldcoordinates(-20, -20, 20, 20)
turtle.bgcolor('black')

# Creación del lapicero
t = turtle.Turtle(shape='circle')
t.shapesize(0.6, 0.6, 0.6)
t.color('#ac82fe')
t.width(1.5)

turtle.tracer(10, 0)

# Definir parámetros. La práctica 4.66 indica:
### a=0.36, b=0.4, c=4.5

a, b, c = 0.1, 0.1, 18.0
#a, b, c = 0.36, 0.4, 4.5

# Cambio en la posición del lapiz
dt = 0.01

# Condiciones iniciales. La práctica 4.66 indica:

x, y, z = 0.1, 0.1, 0.1
#x, y, z = 0, -3, 0

### main loop for pencil
if __name__ == '__main__':
    for i in range(100_000):
        ###Definir la tasa de cambio, las formulas pre definidas
        # x'=-y-z
        dx = -y - z

        #y'=x+ay
        dy = x + a*y

        #z' = bx-cz+xz
        dz = b*x + z * (x-c)

        ### Actualización de la posición
        x += dt * dx
        y += dt * dy
        z += dt * dz

        t.goto(x, (z+y)/4)

    turtle.done()

