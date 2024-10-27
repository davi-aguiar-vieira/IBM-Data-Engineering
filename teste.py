import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'


table = pd.read_html(url)
df = table[1]

# Seleciona apenas as colunas "Average Rank", "Film" e "Year"
df = df[["Average Rank", "Film", "Year"]]

# Salva o DataFrame em um arquivo CSV
# Seleciona apenas as 50 primeiras linhas do DataFrame


# Salva o DataFrame em um arquivo CSV
df = df.iloc[:51]
df.to_csv('teste.csv', index=False)