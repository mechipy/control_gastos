MESES = {
    "1": "data/enero.txt",
    "2": "data/febrero.txt",
    "3": "data/marzo.txt",
    "4": "data/abril.txt",
    "5": "data/mayo.txt",
    "6": "data/junio.txt",
    "7": "data/julio.txt",
    "8": "data/agosto.txt",
    "9": "data/septiembre.txt",
    "10": "data/octubre.txt",
    "11": "data/noviembre.txt",
    "12": "data/diciembre.txt"}


def devolver_opcion():
    print("""
    ***************************
    *    CONTROL DE GASTOS    *
    *************************** """)

    opcion = input("""
    1. Agregar Gasto
    2. Agregar Saldo
    3. Consultar Gastos
    4. Consultar Saldo
    5. Salir
    Elija una opción [1-5]: """)
    return opcion
