"""
Programa que pide nombre, edad y calificación de 5 estudiantes.

Validaciones:
- Edad entre 5 y 100
- Calificación entre 0 y 5

Al final muestra:
- Estudiante con la calificación más alta
- Estudiante con la calificación más baja
- Calificación promedio de todos

Conceptos usados: bucles, condicionales, validación, acumuladores
"""

NUM_ESTUDIANTES = 5

def pedir_nombre(i):
	while True:
		nombre = input(f"Ingrese nombre del estudiante {i+1}: ").strip()
		if nombre:
			return nombre
		print("Nombre no puede estar vacío. Intente de nuevo.")

def pedir_edad():
	while True:
		valor = input("Edad (5-100): ").strip()
		try:
			edad = int(valor)
		except ValueError:
			print("Entrada inválida. Ingrese un número entero para la edad.")
			continue
		if 5 <= edad <= 100:
			return edad
		print("Edad inválida. Debe estar entre 5 y 100.")

def pedir_calificacion():
	while True:
		valor = input("Calificación (0-5): ").strip().replace(',', '.')
		try:
			cal = float(valor)
		except ValueError:
			print("Entrada inválida. Ingrese un número (ej: 4.5).")
			continue
		if 0 <= cal <= 5:
			return cal
		print("Calificación inválida. Debe estar entre 0 y 5.")

def main():
	estudiantes = []
	suma = 0.0

	for i in range(NUM_ESTUDIANTES):
		print(f"\n--- Estudiante {i+1} ---")
		nombre = pedir_nombre(i)
		edad = pedir_edad()
		calificacion = pedir_calificacion()
		estudiantes.append({"nombre": nombre, "edad": edad, "calificacion": calificacion})
		suma += calificacion

	mayor = max(estudiantes, key=lambda e: e['calificacion'])
	menor = min(estudiantes, key=lambda e: e['calificacion'])
	promedio = suma / NUM_ESTUDIANTES

	print("\nResultados:")
	print(f"Estudiante con calificación más alta: {mayor['nombre']} - Edad: {mayor['edad']} - Calificación: {mayor['calificacion']:.2f}")
	print(f"Estudiante con calificación más baja: {menor['nombre']} - Edad: {menor['edad']} - Calificación: {menor['calificacion']:.2f}")
	print(f"Calificación promedio: {promedio:.2f}")

if __name__ == '__main__':
	main()

