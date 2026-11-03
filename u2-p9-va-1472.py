# jose solis nc 1472
import matplotlib.pyplot as plt

materias = ['ML', 'VA', 'LN', 'Matematicas', 'CN']
calificaciones = [90, 85, 95, 80, 88]

plt.pie(calificaciones, labels=materias, autopct='%1.1f%%')
plt.title("NC 1472")
plt.xlabel("Materias")
plt.ylabel("Calificaciones")

plt.show()

print("Jose Solis Porras NC 1472")