
agenda = {
    "Cristhian": "0991234567",
    "Ana": "0987654321"
}

# Agregar un nuevo contacto
agenda["Luis"] = "0971122334"
print("Se agrego a Luis a la agenda.")

# Buscar un contacto
contacto_buscar = "Cristhian"
if contacto_buscar in agenda:
    print("El numero de", contacto_buscar, "es:", agenda[contacto_buscar])
else:
    print("No se encontro el contacto.")

# Eliminar un contacto
agenda.pop("Cristhian")
print("Se elimino a Cristhian de la agenda.")

# Mostrar todos los contactos actualizados
print("\nLista de contactos actualizada:")
for nombre in agenda:
    print(nombre, ":", agenda[nombre])