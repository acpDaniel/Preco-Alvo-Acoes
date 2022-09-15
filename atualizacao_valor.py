import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import schedule
import time


def atualizar():
    con = mysql.connector.connect(
        host="localhost", database="bolsa", user="root", password="#PASSWORD#")
    arquivo_excel = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQDkgppUCZ6Fi2MvDYM17hOl2wzWXLLnAiPxDoCzhM0T1nF6ITxBR408r0iZx8pH_2eQqLHT8zrxNnd/pub?output=xlsx'
    df1 = pd.read_excel(arquivo_excel)
    cotacoes = np.array(df1['cotacao atual'])
    cursor = con.cursor()
    i = 0
    while i < len(cotacoes):
        comando_SQL = "update acoes_monitoradas set valor=" + \
            str(cotacoes[i]) + " where id = "+str(i)+";"
        cursor.execute(comando_SQL)
        con.commit()
        i += 1

    con.close()


atualizar()
