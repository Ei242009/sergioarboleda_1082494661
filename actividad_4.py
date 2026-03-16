import re

def validar_cedula(cedula):
    if isinstance(cedula, str) and cedula.isdigit() and 8 <= len(cedula) <= 10:
        return True
    return False

def validar_email(email):
    # Simple check: has @ and ends with .com
    if '@' in email and email.endswith('.com'):
        return True
    return False

def validar_calificaciones(calificaciones):
    if isinstance(calificaciones, list):
        for cal in calificaciones:
            if not (0 <= cal <= 5):
                return False
        return True
    return False

def calcular_promedio(calificaciones):
    if calificaciones:
        return round(sum(calificaciones) / len(calificaciones), 2)
    return 0.0

def clasificar_desempeño(promedio):
    if promedio >= 4.5:
        return "Excelente"
    elif promedio >= 4.0:
        return "Muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= 3.0:
        return "Satisfactorio"
    else:
        return "Necesita mejorar"

def crear_estudiante(cedula, nombre, email, calificaciones):
    if not validar_cedula(cedula):
        return None
    if not validar_email(email):
        return None
    if not validar_calificaciones(calificaciones):
        return None
    promedio = calcular_promedio(calificaciones)
    return {
        "cedula": cedula,
        "nombre": nombre,
        "email": email,
        "promedio": promedio,
        "desempeño": clasificar_desempeño(promedio)
    }

def listar_estudiantes(lista_estudiantes):
    print("Cédula    | Nombre        | Promedio | Desempeño")
    print("-" * 50)
    for est in lista_estudiantes:
        print(f"{est['cedula']:<10} | {est['nombre']:<13} | {est['promedio']:<8} | {est['desempeño']}")

def main():
    estudiantes = []
    while True:
        print("\nMenú:")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Buscar estudiante por cédula")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            cal_str = input("Calificaciones (separadas por coma): ")
            try:
                calificaciones = [float(x.strip()) for x in cal_str.split(',')]
            except ValueError:
                print("Calificaciones inválidas")
                continue
            estudiante = crear_estudiante(cedula, nombre, email, calificaciones)
            if estudiante:
                # Check if cedula already exists
                if any(e['cedula'] == cedula for e in estudiantes):
                    print("Estudiante con esa cédula ya existe")
                else:
                    estudiantes.append(estudiante)
                    print(f"Estudiante agregado exitosamente. Promedio: {estudiante['promedio']} | Desempeño: {estudiante['desempeño']}")
            else:
                print("Datos inválidos")
        
        elif opcion == "2":
            if estudiantes:
                listar_estudiantes(estudiantes)
            else:
                print("No hay estudiantes registrados")
        
        elif opcion == "3":
            cedula_buscar = input("Cédula a buscar: ")
            encontrado = next((e for e in estudiantes if e['cedula'] == cedula_buscar), None)
            if encontrado:
                print(f"{encontrado['nombre']} | Promedio: {encontrado['promedio']} | Desempeño: {encontrado['desempeño']}")
            else:
                print("Estudiante no encontrado")
        
        elif opcion == "4":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
