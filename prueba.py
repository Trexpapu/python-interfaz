from spellchecker import SpellChecker

# Cargar el corrector ortográfico
spell = SpellChecker(language="es")

# Cadena de texto mal escrita
texto_mal_escrito = input("Ingrese palabra: ")

# Tokenizar el texto en palabras individuales
palabras = texto_mal_escrito.split()

# Obtener sugerencias de corrección para cada palabra
correcciones = {}
for palabra in palabras:
    correccion = spell.correction(palabra)
    if correccion != palabra:
        correcciones[palabra] = correccion

# Reemplazar las palabras corregidas en la oración original
oracion_corregida = " ".join(correcciones.get(palabra, palabra) for palabra in palabras)
print(oracion_corregida)
