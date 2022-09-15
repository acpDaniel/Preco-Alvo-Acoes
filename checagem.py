import pandas as pd
import sqlalchemy
import numpy as np
import smtplib
from email.message import EmailMessage
import schedule
import time


def checar():

    engine = sqlalchemy.create_engine(
        'dialect+driver://username:password@host:port/database')
    df = pd.read_sql_query(
        "select aa.ticker from acoes_alvo as aa inner join acoes_monitoradas on aa.ticker = acoes_monitoradas.ticker and aa.valor >= acoes_monitoradas.valor  ", engine)

    ticker = np.array(df['ticker'])
    i = 0
    agrupamento = ' '.join(ticker)

    if not agrupamento:
        return
    else:
        EMAIL_ADDRESS = '#MY-EMAIL#'
        EMAIL_PASSWORD = '#PASSWORD#'
        msg = EmailMessage()
        msg['Subject'] = 'AVISO COTACOESs'
        msg['From'] = '#MY-EMAIL#'
        msg['To'] = '#YOUR-EMAIL'
        msg.set_content('As acoes com valores desejaveis são: ' + agrupamento)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


checar()
