from src.scrapping import scrapper
import pandas as pd

from ..decorators.decorators import timeit,logit


@logit
@timeit
def clean_fybeca(nombre_columna,df):
    # Definir los reemplazos que deseas realizar
    reemplazos = {
        'CEBIO': 'CEBIÓN',
        '102 Vitamina C+Zn Comp.Efer Caja X 1Tub': 'VITAMINA C+ZN',
        'Calcid Kids Frasco 180Ml': 'CALCID',
        'Biomole C 12.5 G / 50 Ml X 50  Ml Iny': 'BIOMOLE',
        'Devisal Vitamina D3 Cap Blanda C/1':'DEVISAL',
        'Decaforte Jarabe 120 Ml':'DECAFORTE',
        '102 Vitamina C+Zn Comp.Efer Caja X 3Tub':'VITAMINA C+ZN'
    }

    # Aplicar el reemplazo utilizando el método replace
    df[nombre_columna] = df[nombre_columna].replace(reemplazos)
    
    return df


@logit
@timeit
def clean_cruz_azul(df):
    lista_productos=['VITAMINA C+ZN','VITAMINA C+ZN','ACIDO FOLICO','ACIDO FOLICO','ACTIVA-ME','ALOE VERA','ALZANOX','ANALGESICO','ANALGESICO','ANTIARRUGAS','APETICAL','APETITOL','ARAMANOSAR','ARKOCAPIL','ARKOLAGEN',
                     'DESODORANTE AXE','BAGOHEPAT','BEE FARMA','BEE FARMA','BEE FARMA','BEE FARMA','BELLAVIT','BEROCCA','BEROCCA','BIDICA','BIO BOTANICA','BIOSIL','BIOSIL','BIOSIL','BIOSIL','BIOSIL','BIOSIL',
                     'BIRM','BIRM','BIRM','BIRM','BIRM FAMILIAR','BIRM KIDS','BIRM','BROCALCIO','CALCIBON','CALCIBON','CALCIBON','CALCID','CALCIO','CALCIO','CALCIO','CALCIVIT','CAL-COL','CALOIDAL','CALTRACID','FIGURINCLA','MIXAVIS',
                     'PHARMATON MEN']
    df["Producto"]=lista_productos
    return df




    












