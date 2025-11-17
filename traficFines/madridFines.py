# Ivonne Mendoza
# ivonne@imendoza.io


import requests
from bs4 import BeautifulSoup
import pandas as pd
from cacheURL import CacheURL

# Constantes
RAIZ = "https://datos.madrid.es/"
MADRID_FINES_URL = "sites/v/index.jsp?vgnextoid=fb9a498a6bdb9410VgnVCM1000000b205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD"

class MadridError(Exception):
    """ Implementacion de errores para la clase MadridFines """
    pass

# Funcion fuera de la clase MadridFines
def get_url(year:int, month:int) -> str:
    """
    Obtiene un link de descarga de la pagina del ayuntamiento segun anio y mes especificado
    Args:
        year: anio buscado
        month: mes buscado
    Return:
        Una url con el link de descarga correspondiente al archivo csv de ese anio y mes especificado
    Raises:
        MadridError
        Si hay errores al obtener la url (codigo diferente a 200)
        Si hay fechas que no existen en el link url
    """

    # Concatena para formar una url
    url = f'{RAIZ}{MADRID_FINES_URL}'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f'Error al obtener la URL: {response.status_code}')
    soup = BeautifulSoup(response.text, 'html.parser')
    # Obtiene todos los tags de la url que contengan 'li'
    listas = soup.find_all('li')

    #todo agregar validacion de year y month
    # Crea diccionario que traduce el numero del mes a un string adecuado, el formato de fecha del sitio es 2025 Junio
    dict_months = {1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 5: 'Mayo', 6: 'Junio', 7: 'Julio', \
                   8:'Agosto', 9:'Septiembre',10:'Octubre', 11:'Noviembre', 12:'Diciembre'}

    # Crea un string acorde al formato que pide la url
    date_string = f'{year} {dict_months[month]}'

    # Recorre todos los tags li y busca los links asociados de href
    for li in listas:
        titulo = li.find('p', class_='info-title')
        if titulo and date_string in titulo.text:
            h_ref = li.find('a', class_='asociada-link').get('href')
            url_file = f'{RAIZ}{h_ref}'
            return url_file
    raise MadridError(f"No se encontro archivo para la fecha {date_string}")


class MadridFines:
    """
    Implementacion de la clase MadridFines
    Attributes:
    Methods:
    """
    pass


 # Probar get_url() con python3 -c "import sys; sys.path.insert(0, 'traficFines'); from madridFines import get_url; print(get_url(2025, 5))"