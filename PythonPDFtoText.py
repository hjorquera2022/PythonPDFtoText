import PyPDF2

def extraer_contenido_pdf(nombre_archivo):
    contenido = ""
    with open(nombre_archivo, "rb") as archivo_pdf:
        lector = PyPDF2.PdfFileReader(archivo_pdf)
        num_paginas = lector.numPages

        for pagina in range(num_paginas):
            texto = lector.getPage(pagina).extractText()
            contenido += texto

    return contenido

def guardar_contenido_en_archivo(contenido, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo_txt:
        archivo_txt.write(contenido)

# Nombre del archivo PDF de entrada y archivo de texto de salida
nombre_archivo_pdf = "C:\\Users\\hjorquera\\Desktop\\TEMP\\LECTURAS\\Marco Aurelio.pdf"
nombre_archivo_txt = "C:\\Users\\hjorquera\\Desktop\\TEMP\\LECTURAS\\Marco Aurelio.pdf.txt"

# Extraer contenido del PDF
contenido = extraer_contenido_pdf(nombre_archivo_pdf)

# Guardar contenido en un archivo de texto
guardar_contenido_en_archivo(contenido, nombre_archivo_txt)

print("El contenido del archivo PDF se ha guardado en", nombre_archivo_txt)
