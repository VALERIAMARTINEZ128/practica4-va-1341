import cv2
# valeria yaretzi NC = 1341
import cv2

# 1. Leer imagen
imagen = cv2.imread("alcon.jpg")

if imagen is None:
    print("ERROR: No se pudo cargar alcon.jpg")
    exit()

print("Imagen cargada correctamente.")
print("Dimensiones:", imagen.shape)

# 2. Mostrar imagen original
cv2.imshow("Imagen original", imagen)

# 3. Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# 4. Mostrar imagen en escala de grises
cv2.imshow("Imagen en escala de grises", gris)

# 5. Guardar copia
cv2.imwrite("alcon_copia.jpg", imagen)

# 6. Guardar imagen procesada
cv2.imwrite("alcon_gris.jpg", gris)

print("Copia guardada: alcon_copia.jpg")
print("Imagen gris guardada: alcon_gris.jpg")

# 7. Mostrar durante 3 segundos
cv2.waitKey(3000)

# 8. Cerrar ventanas
cv2.destroyAllWindows()

print("Practica terminada correctamente.")

print("valeria yaretzi NC = 1341")
