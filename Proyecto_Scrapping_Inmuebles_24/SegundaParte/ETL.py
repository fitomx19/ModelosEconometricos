import pandas as pd

def ETL_ARCHIVO(nombre_archivo, nombre_productos, presentaciones, fecha):
    df = pd.read_csv(nombre_archivo, sep=',' , encoding='utf-8')
    df.columns = ['PRODUCTO','PRESENTACIÓN','MARCA','CATEGORÍA','CATÁLOGO','PRECIO','FECHAREGISTRO','CADENACOMERCIAL','GIRO','NOMBRECOMERCIAL','DIRECCIÓN','ESTADO','MUNICIPIO','LATITUD','LONGITUD']
    if(len(nombre_productos) != len(presentaciones)):
        print("Error, no coinciden los tamaños de los arreglos")
        return 0
    df_final = pd.DataFrame()
    for i in range(len(nombre_productos)):
        df_temporal = df[(df['PRODUCTO'] == nombre_productos[i]) & (df['ESTADO'] == 'CIUDAD DE MÉXICO') & (df['PRESENTACIÓN'] == presentaciones[i])]
        df_temporal = df_temporal[['NOMBRECOMERCIAL','PRECIO','FECHAREGISTRO','PRESENTACIÓN','MARCA','LATITUD','LONGITUD','PRODUCTO']]
        # Concatenar los datos de cada producto al DataFrame final
        df_final = pd.concat([df_final, df_temporal])
    df_final = df_final.drop_duplicates(subset=['NOMBRECOMERCIAL','PRECIO','FECHAREGISTRO','PRESENTACIÓN','MARCA','LATITUD','LONGITUD','PRODUCTO'])
    df_final = df_final[df_final['FECHAREGISTRO'].isin([fecha])]
    df_final = convertir(df_final)
    
    return df_final
    
def convertir(df2):

    df = df2.copy()  # Crea una copia del DataFrame para evitar el warning
    df['NOMBRECOMERCIAL'] = df['NOMBRECOMERCIAL'].astype(str)
    df['FECHAREGISTRO'] = df['FECHAREGISTRO'].astype(str)
    df['PRESENTACIÓN'] = df['PRESENTACIÓN'].astype(str)
    df['MARCA'] = df['MARCA'].astype(str)
    df['PRODUCTO'] = df['PRODUCTO'].astype(str)
    df['PRECIO'] = df['PRECIO'].astype(float)
    df['LATITUD'] = df['LATITUD'].astype(float)
    df['LONGITUD'] = df['LONGITUD'].astype(float)

    return df


""" def find_cheapest_store(datasets):
    store_prices = {}
    store_counts = {}
    
    for dataset in datasets:
        for index, entry in dataset.iterrows():
            store = entry['NOMBRECOMERCIAL']
            price = entry['PRECIO']
            if store in store_prices:
                store_prices[store] += price
                store_counts[store] += 1
            else:
                store_prices[store] = price
                store_counts[store] = 1
    
    num_datasets = len(datasets)
    valid_stores = {k: v for k, v in store_counts.items() if v == num_datasets}
    
    cheapest_store = min(valid_stores.keys(), key=lambda k: store_prices[k])
    
    return cheapest_store, store_prices[cheapest_store]


def list_all_store_prices(datasets):
    store_prices = {}
    store_counts = {}
    
    for dataset in datasets:
        for index, entry in dataset.iterrows():
            store = entry['NOMBRECOMERCIAL']
            price = entry['PRECIO']
            if store in store_prices:
                store_prices[store] += price
                store_counts[store] += 1
            else:
                store_prices[store] = price
                store_counts[store] = 1
                
    return store_prices, store_counts

 
 """