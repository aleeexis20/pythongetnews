from webscrap import extraer_texto, procesar_texto
from database import guardar_datos, consultar_vialidades

# Link noticia de preferencia de Ensenada BC
url_noticia = "https://ensenadahoy.com/noticias/ver/68FF" 

print("--- DESCARGANDO TEXTO DE LA WEB ---")
# Extraemos el texto
texto_real = extraer_texto(url_noticia)

print("\n--- BUSCANDO FECHAS Y LUGARES ---")
# Pasamos el texto extraido a la funcion procesar_texto para obtener diccionarios de fechas y lugares
diccionario_fechas, diccionario_lugares = procesar_texto(texto_real)

print("Fechas encontradas:", diccionario_fechas)
print("Lugares encontrados:", diccionario_lugares)

print("\n--- GUARDAR EN BASE DE DATOS ---")
# Guarda todo lo encontrado
if diccionario_fechas or diccionario_lugares:
    guardar_datos(diccionario_fechas, diccionario_lugares)
else:
    print("No se encontraron fechas ni vialidades en la noticia de hoy para guardar.")

print("\n--- CONSULTAR BASE DE DATOS ---")
datos_guardados = consultar_vialidades()

print("Datos encontrados y guardados en MySQL:")
for fila in datos_guardados:
    print(fila)