import argparse

def parsing():
    # Esto es para definir la función y es lo que va a orientar al usuario de lo que debe de ingresar para que le de un resultado.
    parser = argparse.ArgumentParser(description='Elige si estas buscando estación de BiciMAD o BiciPARK, cercana a tu ubicación')
    parser.add_argument('--bicimad', action='store_true', help="Quiero ir a una estación de BiciMAD")
    parser.add_argument('--bicipark', action='store_true', help="Quiero ir a una estación de BiciPARK")
    parser.add_argument('--todas', action='store_true', help="Quiero toda la lista de estaciones")
    parser.add_argument('--lugar', type = str, help="Quiero ir a un lugar específico")

    # Aquí estas almacenando los argumentos  que tengan el metodo parser que estoy nombrando arriba 
    args = parser.parse_args()
    # Esto es necesario  para poder llamar a la función en los otros modulos. 
    return args
