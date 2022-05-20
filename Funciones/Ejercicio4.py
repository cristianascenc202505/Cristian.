def crearCategorias(narrativaCat, dramaticoCat, liricoCat):
    return {'narrativa' : list(narrativa), 'dramatico':list(dramatico), 'lirico':list(lirico)}

def mostrarGenerosLiterarios():
    print(f' El diccionario de Categorías Literarias es: {categorias}')
    
narrativa = ('La Vorágine', 'Don Quijote de la mancha', 'Con la soga al cuello')
dramatico = ('El hechizo del agua', 'Primero es ella', 'Hasta que salga el sol')
lirico =('Los Heraldos negros', 'Los versos del capitan', 'Cantar del Mio Cid')

categorias = crearCategorias(narrativa, dramatico, lirico)
mostrarGenerosLiterarios()