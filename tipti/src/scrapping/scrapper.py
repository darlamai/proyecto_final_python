import requests
from bs4 import BeautifulSoup
import pandas as pd



def obtener_pagina(url):
    """
    Obtenemos el contenido de la pagina
    """
    response=requests.get(url)
    if response.status_code==200:
        return response.content
    else:
        raise Exception("No se pudo obtener los datos de: {url}")
    


def extraer_fybeca(url):
    """
    Extraemos el texto de los elementos con la clase específica.
    """
    contenido = obtener_pagina(url)
    soup = BeautifulSoup(contenido, 'html.parser')
    elementos = soup.find_all('div', class_='tile-body px-3 pt-3 pb-0 d-flex flex-column pb-2')
    
    # Lista para almacenar los textos extraídos
    textos = []

    # Iteramos sobre cada elemento encontrado
    for elemento in elementos:
        # Intentamos extraer el texto de las etiquetas <a> y <span> dentro del div
        try:
            producto = elemento.find('a', class_='product-brand text-uppercase m-0')
            if not producto:
                producto=elemento.find('div', class_='pdp-link')
            producto_texto = producto.get_text(strip=True) if producto else None
            
            descripcion = elemento.find('a', class_='link')
            descripcion_texto = descripcion.get_text(strip=True) if descripcion else None
            
            precio = elemento.find('div', class_='large-price w-100 d-flex mb-1')
         
            if not precio:
                precio = elemento.find('div', class_='large-price d-flex') 
                
            precio_texto = precio.get_text(strip=True) if precio else None
            
            if precio:
                precio_texto=precio_texto.replace('(Oferta)', '').strip()
                precio_texto=precio_texto.replace("$",'')
                precio_texto=precio_texto.replace("\n",'')
            else:
                None
            
            # Agregamos el texto extraído a la lista
            textos.append({
                'Producto': producto_texto,
                'Descripcion': descripcion_texto,
                'Precio': float(precio_texto)
            })
        except AttributeError:
            # En caso de que algún atributo no exista, llenamos con None
            textos.append({
                'Producto': None,
                'Descripcion': None,
                'Precio': None
            })
    
    return textos





def extraer_cruz_azul(url):
    """
    Extraemos el texto de los elementos con la clase específica.
    """
    contenido = obtener_pagina(url)
    soup = BeautifulSoup(contenido, 'html.parser')
    elementos = soup.find_all('div', class_='ps-section__product')
    
    # Lista para almacenar los textos extraídos
    textos = []

    # Iteramos sobre cada elemento encontrado
    for elemento in elementos:
        # Intentamos extraer el texto de las etiquetas <a> y <span> dentro del div
        try:
            descripcion = elemento.find('h5', class_='ps-product__title')
            descripcion_texto = descripcion.get_text(strip=True) if descripcion else None
            
            
            precio = elemento.find('span', class_='ps-product__price sale')
            precio_texto=precio.get_text(strip=True) if precio else None
            
            if precio:
                precio_texto=precio_texto.replace('$', '').strip()
            else:
                None
         
            
            # Agregamos el texto extraído a la lista
            textos.append({
                'Descripcion': descripcion_texto,
                'Precio': float(precio_texto)
            })
        except AttributeError:
            # En caso de que algún atributo no exista, llenamos con None
            textos.append({
                'Descripcion': None,
                'Precio': None
            })
    
    return textos





#textos_extraidos=extraer_cruz_azul(url)

# Mostrar los textos extraídos
#for texto in textos_extraidos:
#    print(texto)
    
    
    



#https://www.farmaciasmedicity.com/nutricion-y-vitaminas/multivitaminicos/vitaminas?initialMap=c&initialQuery=nutricion-y-vitaminas&map=category-1,category-2,category-2&order=OrderByNameASC&page=4
#https://www.fybeca.com/nutricion-y-vitaminas/vitaminas-y-minerales/?srule=nombre-za&start=0&sz=24&maxsize=54    
   

###https://www.farmaciasmedicity.com/nutricion-y-vitaminas/multivitaminicos/vitaminas?initialMap=c&initialQuery=nutricion-y-vitaminas&map=category-1,category-2,category-2&order=OrderByNameASC&page=2




####print(obtener_pagina(base_url))