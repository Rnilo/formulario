import random
import csv
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
                "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
sueldos = []

def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("Sueldos asignados correctamente.")

def clasificar_sueldos():
    clasificaciones = []
    for sueldo in sueldos:
        if sueldo < 1000000:
            clasificaciones.append("Bajo")
        elif sueldo <= 2000000:
            clasificaciones.append("Medio")
        else:
            clasificaciones.append("Alto")
    
    for trabajador, sueldo, clasificacion in zip(trabajadores, sueldos, clasificaciones):
        print(f"{trabajador}: ${sueldo} - {clasificacion}")

def ver_estadisticas():
    if not sueldos:
        print("Primero debe asignar los sueldos.")
        return
    
    sueldo_mas_alto = int(round(max(sueldos)))
    
    sueldo_mas_bajo = int(round(min(sueldos)))
    promedio_sueldos = int(round(sum(sueldos) / len(sueldos)))
    promedio_sueldos = int(round(promedio_sueldos))
    media_geometrica = int(round(math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))))
    media_geometrica = int(round(media_geometrica))
    
    print(f"Sueldo más alto: ${sueldo_mas_alto}")
    print(f"Sueldo más bajo: ${sueldo_mas_bajo}")
    print(f"Promedio de sueldos: ${promedio_sueldos}")
    print(f"Media geométrica de sueldos: ${media_geometrica}")

def reporte_sueldos():
    reporte = []
    for trabajador, sueldo in zip(trabajadores, sueldos):
        descuento_salud = int(round(sueldo * 0.07))
        descuento_afp = int(round(sueldo * 0.12))
        sueldo_liquido = int(round(sueldo - descuento_salud - descuento_afp))
        reporte.append((trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido))
    
    for fila in reporte:
        print(f"nombre      ","sueldo      ","descuento_salud","descuento_afp","sueldo_liquido")
        print(f"{fila[0]:<20} ${fila[1]:<10} ${fila[2]:<10} ${fila[3]:<10} ${fila[4]:<10}")
    
    with open("reporte_sueldos.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for fila in reporte:
            writer.writerow(fila)
    
    print("Reporte de sueldos exportado a 'reporte_sueldos.csv'.")
