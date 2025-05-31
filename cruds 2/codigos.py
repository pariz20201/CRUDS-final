import barcode
from barcode.writer import ImageWriter

# Lista con los códigos y nombres para generar códigos de barra
productos = [
    ("7501020526066", "Leche_Lala_1L"),
    ("7501000122332", "Pan_Bimbo_Blanco"),
    ("7894900027013", "CocaCola_2L"),
    ("7501071301452", "Arroz_Verde_Valle_1kg"),
    ("7501379120137", "Frijol_Negro_900g"),
    ("8422410000722", "Manzana_Roja_kg"),
    ("8411030015469", "Pechuga_de_Pollo_kg"),
    ("7501026005381", "Jabon_Zote_Blanco"),
]

for codigo, nombre in productos:
    ean = barcode.get('ean13', codigo, writer=ImageWriter())
    nombre_archivo = f"{nombre}.png"
    ean.save(nombre_archivo)
    print(f"Código de barras generado para {nombre}: {nombre_archivo}")