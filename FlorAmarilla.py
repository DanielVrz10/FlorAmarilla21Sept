from turtle import *
import colorsys

# AGREGAR EL TEXTO EN LA CABECERA
# OPCIONAL
header_text = "FELIZ 21 SEPTIEMBRE # POR DANIVRZ10"
color("white")  # COLOR DEL TEXTO
penup()
goto(-180, 250)  # POSICIÓN DEL TEXTO
pendown()
write(header_text, align="left", font=("Arial", 15, "normal"))

speed(20)
bgcolor("black")
h = 0

# MAQUETADO DEL DIBUJO DEL TALLO VERDE DEL GIRASOL 
penup()
goto(0, -100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

# MAQUETADO DEL DIBUJO DEL GIRASOL
penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")  # Todos los pétalos son amarillos
        h += 0.005
        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)
# DIBUJO EL CENTRO DE COLOR CAFE
penup()
goto(-20, 0)
pendown()
color("brown")
begin_fill()
circle(44)  # AJUSTE DEL TAMAÑO DEL RADIO DEL CENTRO
end_fill()
done()
