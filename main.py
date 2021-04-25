import pandas as pd
#from typing import optional
from fastapi import FastAPI
import uvicorn
import json
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

app = FastAPI()

@app.get("/")
def show_item():
    data = pd.read_csv('data test2.csv')
    desawisata = pd.DataFrame(data)
    pd.DataFrame(desawisata)

    desabycat = data.loc[:,['nama_desa_wisata', 'jenis_kategori']]
    A = pd.DataFrame(desabycat)

    return A.to_string()

@app.get("/{nama_desa_wisata}")
def show_item(nama_desa_wisata: str):
    data = pd.read_csv('data test2.csv')
    desawisata = pd.DataFrame(data)
    #pd.DataFrame(desawisata)

    desabycat = data.loc[:,['nama_desa_wisata', 'jenis_kategori']]
    A = pd.DataFrame(desabycat)

    B = pd.DataFrame()
    for i in range(len(A)):
         B = B.append({'nama_desa_wisata':A[i]['nama_desa_wisata'],'jenis_kategori':A[i]['jenis_kategori']}, ignore_index=True)

    desachoosen = desawisata[desawisata['nama_desa_wisata'].str.lower()==nama_desa_wisata.lower()]

    return A.to_string("nama desa:"+desachoosen['nama_desa_wisata'].iloc[0].to_string)

if __name__== "__main__":
	uvicorn.run(app,host="127.0.0.1",port=int(os.environ.get('PORT',5000)), log_level="info")