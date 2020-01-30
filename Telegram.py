
teste=['VVAR3.SA',
      'PRIO3.SA',
      'SQIA3.SA',
      'TASA4.SA',
      'MRFG3.SA',
      'CYRE3.SA',
      'LOGN3.SA',
      'JSLG3.SA',
      'JHSF3.SA']
import pandas as pd
import numpy as np
import requests
import schedule
from pandas_datareader import data as wb
import seaborn as sns
import datetime
from datetime import datetime
import time


def telegram_bot_sendtext(bot_message):
    
    bot_token = '907770672:AAFVsnaVQsRxZceuR11YIBO0yk-XUxwKe6A'
    bot_chatID = '531406905'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message








    response = requests.get(send_text)








    return response.json()






df2=pd.DataFrame()
df2['ACAO']='teste'
df2['RS']='teste'
def testa():
    telegram_bot_sendtext(str(datetime.now()))


def trendline(index,data, order=1):
    coeffs = np.polyfit(index, data, order)
    #print (coeffs)
    slope = coeffs[-2]
    return float(slope)




ind_9=0
ind_21=0
telegram_bot_sendtext(str(datetime.now()))  


for ticks in teste:
    Acao=ticks
    Periodo='2019-01-01'
    PG = wb.DataReader(Acao,data_source="yahoo",start=Periodo)
    df=pd.DataFrame(PG)
    
    Janela_media_50=9
    Janela_media_100=21
    Janela_media_200=200
    media150=150
    media50=50
    rsi_period=14
    chg=df['Adj Close'].diff(1)
    gain=chg.mask(chg<0,0)
    loss=chg.mask(chg>0,0)
    avg_gain=gain.ewm(com=rsi_period-1,min_periods=rsi_period).mean()
    avg_loss=loss.ewm(com=rsi_period-1,min_periods=rsi_period).mean()
    rs=abs(avg_gain/avg_loss)
    rsi=100-(100/(1+rs))
    df['RSI']=rsi


#Separando Close para as Médias e criando as médias
    close=df[['Close']]
#MA9
    ma150=close.rolling(window=media150).mean()
    ma150.columns=['MA 150']
#MA9
    ma50=close.rolling(window=media50).mean()
    ma50.columns=['MA 50']
#MA9
    ma_50=close.rolling(window=9).mean()
    ma_50.columns=['MA 9']
#MA21
    ma_100=close.rolling(window=Janela_media_100).mean()
    ma_100.columns=['MA 21']
#MA200
    ma_200=close.rolling(window=Janela_media_200).mean()
    ma_200.columns=['MA 200']
    
#ma_50['EMA 50']=0
#print (ma_50)
    ema_9=df['Close'].ewm(span=9,min_periods=0,adjust=False,ignore_na=False).mean()
    ema_21=df['Close'].ewm(span=21,min_periods=0,adjust=False,ignore_na=False).mean()
    ema_50=df['Close'].ewm(span=50, adjust=False).mean()
    ema_12=df['Close'].ewm(span=12, adjust=False).mean()
    ema_26=df['Close'].ewm(span=26, adjust=False).mean()
#Organização dos candles


    min52=close.rolling(window=250).min()
    max52=close.rolling(window=250).max()




    df['MA9']=ma_50
    df['MA21']=ma_100
    df['MA200']=ma_200
    df['EMA9']=ema_9
    df['EMA12']=ema_12
    df['EMA21']=ema_21
    df['EMA26']=ema_26 
    df['EMA50']=ema_50
    df['MA50']=ma50
    df['MA150']=ma150
    df['RSI']=rsi
    df['min52']=min52
    df['max52']=max52


    del df['High']


    del df['Low']
    del df['Open']


    data = df['MA200'].iloc[-30:].tolist()
    df_unix_sec = pd.to_datetime(df.index[-30:]).astype(int)/ 10**9
    index = df_unix_sec.tolist()
    #print (index)


    #print('teste')


      
    if df['Close'].iloc[-1]<df['EMA9'].iloc[-1]:
        ind_9=ind_9+1
        telegram_bot_sendtext('~~~~~~~~~~~~~~~~')
        telegram_bot_sendtext(Acao)
        telegram_bot_sendtext("ALERTA EMA 9:")
        telegram_bot_sendtext(str(df['EMA9'].iloc[-1]))
        telegram_bot_sendtext('Preço atual:')
        telegram_bot_sendtext(str(df['Close'].iloc[-1]))
        telegram_bot_sendtext('~~~~~~~~~~~~~~~~')
    if df['Close'].iloc[-1]<df['EMA21'].iloc[-1]:
        ind_21=ind_21+1
        telegram_bot_sendtext('~~~~~~~~~~~~~~~~')
        telegram_bot_sendtext(Acao)
        telegram_bot_sendtext("ALERTA EMA 21:")
        telegram_bot_sendtext(str(df['EMA21'].iloc[-1]))
        telegram_bot_sendtext('Preço atual:')
        telegram_bot_sendtext(str(df['Close'].iloc[-1]))
        telegram_bot_sendtext('~~~~~~~~~~~~~~~~')


                                
                            #print(df.index[-1])
#print (round(df['Close'].iloc[-1],2))
                            #print (str(round(returns_acao['Close'].iloc[-1]*100,2))+"%")




telegram_bot_sendtext('~~~~~~~~~~~~~~~~')
telegram_bot_sendtext('RESUMO')
telegram_bot_sendtext('Abaixo EMA 9: ')
telegram_bot_sendtext(str(ind_9))
telegram_bot_sendtext('Abaixo EMA 21: ')
telegram_bot_sendtext(str(ind_21))
telegram_bot_sendtext('~~~~~~~~~~~~~~~~')


df.tail()






#writer=pd.ExcelWriter('Minervini.xlsx')
#df2.to_excel(writer,'Minervini',index=False,engine="xlsxwriter")
#writer.save()