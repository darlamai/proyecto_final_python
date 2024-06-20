import pandas as pd
from src.scrapping import scrapper
from src.analisis import clean_fybeca, clean_cruz_azul
from src.decorators.decorators import timeit,logit 


@logit
@timeit
def get_dataframe(url1, url2):
    texto_extraido1 = scrapper.extraer_fybeca(url1)
    texto_extraido2 = scrapper.extraer_cruz_azul(url2)
    data_fybeca = pd.DataFrame(texto_extraido1)
    data_fybeca["Farmacia"] = "Fybeca"
    data_cruz_azul = pd.DataFrame(texto_extraido2)
    data_cruz_azul = clean_cruz_azul(data_cruz_azul)
    data_cruz_azul["Farmacia"] = "Cruz Azul"
    data_fybeca = clean_fybeca("Producto", data_fybeca)
    data_final = pd.concat([data_fybeca, data_cruz_azul])
    return data_final


url1='https://www.fybeca.com/nutricion-y-vitaminas/vitaminas-y-minerales/?srule=nombre-za&start=0&sz=36&maxsize=36'

url2='https://farmaciascruzazul.ec/vitaminas-y-suplementos?viewmode=&orderby=5&pagesize=54&price=1.00-136.00'
df=get_dataframe(url1,url2)
df.to_csv("data/raw/products.csv",index=False)

