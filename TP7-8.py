'''Un cliente ha solicitado un programa que le permita ingresar
los mililitros de lluvia caídos diariamente en una semana,
para que el programa le informe en pantalla el promedio de precipitación
de esa semana. El cliente también desea
saber cuál fue el día en que más llovió en la semana.
A modo ilustrativo, un reporte generado por el programa debería verse como
sigue, luego de haber leído las precipitaciones de los 7 días de la semana:
El promedio de precipitaciones fue de XX mls. diarios.
El día de más precipitaciones fue el xxxxxx (nombre del día).'''


semana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
# semana_completa = False


def relevo_precipitaciones():

    precipitaciones = []

    for x in range(1, 8):
        x = int(input("Ingrese los mL de hoy: "))
        precipitaciones.append(x)

    mayor_precipitacion = max(precipitaciones)

    dia_max_precipitaciones = precipitaciones.index(max(precipitaciones))

    return f"El día de mayor precipitación fue el {semana[dia_max_precipitaciones]} con {mayor_precipitacion} mL."


print(relevo_precipitaciones())
