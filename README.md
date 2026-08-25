# pythongetnews

## Descripción 
Este repositorio contiene un script automatizado en Python diseñado para extraer, procesar y almacenar información de páginas de noticias locales de Ensenada. 

El programa funciona como un proceso básico de ETL:
* **Extrae** el texto de las notas periodísticas.
* **Transforma** los datos identificando días de la semana (con fechas válidas del 1 al 31) y nombres de vialidades, validándolos contra un registro oficial.
* **Carga** la información final en una base de datos MySQL.

## Requisitos y Versión
* **Versión de Python:** Python 3.13
* **Librerías utilizadas:** `requests`, `beautifulsoup4`, `mysql-connector-python` y librerías estándar nativas.

## Estructura del Código

El trabajo está dividido en tres archivos para mantener buenas prácticas de desarrollo:
* `webscrap.py`: Descarga la página con `requests`, extrae los párrafos con `BeautifulSoup` y limpia el texto.
* `database.py`: Gestiona la conexión y la inserción de datos en MySQL.
* `main.py`: Coordina el flujo de información entre la extracción y la base de datos.

## Decisiones Técnicas Destacadas

**Validación con Catastro Oficial:** Para evitar guardar datos incorrectos, los lugares encontrados se cruzan contra un catálogo oficial de SEPOMEX (`colonias.csv`). #Nota: Como Ensenada esta en constante crecimiento algunas calles, avenidas o colonias no estan registradas oficialmente y no serán encontradas (pero se pueden agregar manualmente en el csv para futuras extracciones).

**Búsqueda Flexible:** Se utilizó el operador `in` en lugar de una igualdad (`==`) al validar contra el catastro. Esto evita que se pierdan datos si la noticia usa nombres cortos.

## ¿Cómo ejecutar?
Para correr este programa, sigue estos pasos:
1. Clona este repositorio en tu computadora.
2. Asegúrate de tener tu servidor MySQL local encendido.
3. Abre tu terminal, navega hasta la carpeta del proyecto (`pythongetnews`) y asegúrate de tener tu entorno virtual activado.
4. Ejecuta con "python main.py".