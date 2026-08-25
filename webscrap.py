import requests
from bs4 import BeautifulSoup

def extraer_texto(url):
    # Realizamos la peticion al servidor de la pagina
    respuesta = requests.get(url)
    
    # Validamos que el servidor respondio 
    if respuesta.status_code == 200:
        # Usamos 'html.parser' para poder navegar por sus etiquetas
        sopa = BeautifulSoup(respuesta.text, 'html.parser')
        # Filtramos especificamente los parrafos de la noticia
        parrafos = sopa.find_all('p')
        
        texto_completo = ""
        for p in parrafos:
            # Concatenamos el texto limpiando las etiquetas HTML, dejando un espacio
            texto_completo = texto_completo + p.text + " "
            
        return texto_completo
    
    return ""

def procesar_texto(texto):
    # Convertimos el string en una lista indexada de palabras individuales
    texto_separado = texto.split()
    texto_size = len(texto_separado)
    
    # Lista para identificar las entidades deseadas
    dias_semana = ["domingo", "lunes", "martes", "miercoles","miércoles", "jueves", "viernes", "sabado","sábado"]
    palabras_clave_lugar = ["avenida", "calle", "colonia", "bulevar", "blvd", "fraccionamiento", "ejido"]
    
    # --- BASE DE DATOS EXTERNA (SEPOMEX) ---
    catalogo_oficial = []
    try:
        # Abrimos el archivo csv que contiene el catalogo oficial de colonias de Ensenada
        with open("colonias.csv", "r", encoding="utf-8") as archivo_csv:
            for linea in archivo_csv:
                # Limpiamos espacios y convertimos a minusculas para estandarizar
                catalogo_oficial.append(linea.strip().lower())
    except FileNotFoundError:
        print("No se encontro el archivo")
    
    
    diccionario_fechas = {}
    diccionario_lugares = {}

    # Iteramos sobre cada palabra basandonos en su posicion
    for i in range(0, texto_size):
        palabra_actual = texto_separado[i].lower()
        palabra_actual = palabra_actual.replace(",", "")
        palabra_actual = palabra_actual.replace(".", "")
        
        # --- BUSQUEDA DE FECHAS ---
        if palabra_actual in dias_semana:
            if i + 1 < texto_size:
                siguiente_palabra = texto_separado[i+1].replace(",", "").replace(".", "")
                
                # Comprobamos si la cadena de texto es un numero
                if siguiente_palabra.isdigit():
                    numero_dia = int(siguiente_palabra)
                    # El numero debe pertenecer a un dia logico del mes (1 a 31)
                    if numero_dia >= 1 and numero_dia <= 31:
                        diccionario_fechas[palabra_actual] = numero_dia
        
        # --- BUSQUEDA DE LUGARES Y VALIDACION  ---
        if palabra_actual in palabras_clave_lugar:
            if i + 1 < texto_size:
                nombre_lugar = texto_separado[i+1].lower().replace(",", "").replace(".", "")
                
                # Logica de validacion:
                # Revisamos si la palabra encontrada parte de un nombre oficial 
                es_valida = False
                for colonia_oficial in catalogo_oficial:
                    if nombre_lugar in colonia_oficial:
                        es_valida = True
                        break # Si encontramos una coincidencia, detenemos la busqueda
                
                # Solo guardamos el dato en el diccionario si existe en el csv
                if es_valida:
                    diccionario_lugares[palabra_actual] = nombre_lugar

    return diccionario_fechas, diccionario_lugares