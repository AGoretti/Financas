
teste=['abcb4.SA',
'tiet11.SA',
'aalr3.SA',
'alpa4.SA',
'alup11.SA',
'abev3.SA',
'anim3.SA',
'arzz3.SA',
'azul4.SA',
'btow3.SA',
'b3sa3.SA',
'bidi4.SA',
'bpan4.SA',
'brsr6.SA',
'bbse3.SA',
'gbio33.SA',
'bkbr3.SA',
'brml3.SA',
'brpr3.SA',
'bbdc3.SA',
'bbdc4.SA',
'brap4.SA',
'bbas3.SA',
'brkm5.SA',
'brfs3.SA',
'bpac11.SA',
'caml3.SA',
'crfb3.SA',
'ccro3.SA',
'cmig3.SA',
'cmig4.SA',
'cnto3.SA',
'cesp6.SA',
'hgtx3.SA',
'ciel3.SA',
'csmg3.SA',
'cple3.SA',
'cple6.SA',
'csan3.SA',
'rlog3.SA',
'cpfe3.SA',
'cvcb3.SA',
'cyre3.SA',
'dirr3.SA',
'dtex3.SA',
'ecor3.SA',
'elet3.SA',
'elet6.SA',
'embr3.SA',
'enat3.SA',
'enbr3.SA',
'engi11.SA',
'enev3.SA',
'egie3.SA',
'eqtl3.SA',
'bovb11.SA',
'even3.SA',
'eztc3.SA',
'fesa4.SA',
'alzr11.SA',
'bbpo11.SA',
'bcff11.SA',
'brcr11.SA',
'hgcr11.SA',
'hglg11.SA',
'gtwr11.SA',
'ggrc11.SA',
'hgbs11.SA',
'hgre11.SA',
'hfof11.SA',
'irdm11.SA',
'jsre11.SA',
'knri11.SA',
'knip11.SA',
'kncr11.SA',
'mall11.SA',
'mxrf11.SA',
'mgff11.SA',
'rbrf11.SA',
'rbrr11.SA',
'saag11.SA',
'sdil11.SA',
'tbof11.SA',
'tgar11.SA',
'ubsr11.SA',
'visc11.SA',
'vilg11.SA',
'xpin11.SA',
'xplg11.SA',
'xpml11.SA',
'fnam11.SA',
'fnor11.SA',
'flry3.SA',
'gfsa3.SA',
'ggbr4.SA',
'goau4.SA',
'goll4.SA',
'grnd3.SA',
'guar3.SA',
'hapv3.SA',
'hbor3.SA',
'hype3.SA',
'igta3.SA',
'pard3.SA',
'meal3.SA',
'romi3.SA',
'gndi3.SA',
'mypk3.SA',
'irbr3.SA',
'ivvb11.SA',
'bova11.SA',
'smal11.SA',
'bovv11.SA',
'divo11.SA',
'pibb11.SA',
'itsa3.SA',
'itsa4.SA',
'itub3.SA',
'itub4.SA',
'jbss3.SA',
'jpsa3.SA',
'jhsf3.SA',
'jslg3.SA',
'klbn4.SA',
'klbn11.SA',
'cogn3.SA',
'ligt3.SA',
'linx3.SA',
'rent3.SA',
'lcam3.SA',
'logg3.SA',
'logn3.SA',
'lame3.SA',
'lame4.SA',
'amar3.SA',
'lren3.SA',
'lpsb3.SA',
'mdia3.SA',
'mglu3.SA',
'pomo4.SA',
'mrfg3.SA',
'leve3.SA',
'mils3.SA',
'beef3.SA',
'movi3.SA',
'mrve3.SA',
'mult3.SA',
'natu3.SA',
'neoe3.SA',
'odpv3.SA',
'oibr3.SA',
'oibr4.SA',
'omge3.SA',
'pcar4.SA',
'pmam3.SA',
'petr3.SA',
'petr4.SA',
'brdt3.SA',
'prio3.SA',
'pine4.SA',
'pssa3.SA',
'ptbl3.SA',
'pfrm3.SA',
'qual3.SA',
'radl3.SA',
'rapt4.SA',
'rail3.SA',
'sbsp3.SA',
'sapr4.SA',
'sapr11.SA',
'sanb11.SA',
'stbp3.SA',
'smto3.SA',
'seer3.SA',
'csna3.SA',
'sqia3.SA',
'slce3.SA',
'smls3.SA',
'sgps3.SA',
'sula11.SA',
'suzb3.SA',
'taee11.SA',
'tcsa3.SA',
'tgma3.SA',
'vivt3.SA',
'vivt4.SA',
'tend3.SA',
'timp3.SA',
'tots3.SA',
'trpl4.SA',
'tris3.SA',
'tupy3.SA',
'ugpa3.SA',
'ucas3.SA',
'unip6.SA',
'usim5.SA',
'vale3.SA',
'vlid3.SA',
'vvar3.SA',
'vulc3.SA',
'wege3.SA',
'wizs3.SA']
import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import seaborn as sns
import datetime
from datetime import datetime
import time








df2=pd.DataFrame()
df2['ACAO']='teste'
df2['RS']='teste'
















def trendline(index,data, order=1):
    coeffs = np.polyfit(index, data, order)
    #print (coeffs)
    slope = coeffs[-2]
    return float(slope)
































for ticks in teste:
    Acao=ticks
    Periodo='2016-01-01'
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
    close=df[['Adj Close']]
#MA9
    ma150=close.rolling(window=media150).mean()
    ma150.columns=['MA 150']
#MA9
    ma50=close.rolling(window=media50).mean()
    ma50.columns=['MA 50']
#MA9
    ma_50=close.rolling(window=Janela_media_50).mean()
    ma_50.columns=['MA 9']
#MA21
    ma_100=close.rolling(window=Janela_media_100).mean()
    ma_100.columns=['MA 21']
#MA200
    ma_200=close.rolling(window=Janela_media_200).mean()
    ma_200.columns=['MA 200']
    ema_short = df['Adj Close'].ewm(span=9, adjust=False).mean()
#ma_50['EMA 50']=0
#print (ma_50)
    ema_
9=ema_short = df['Adj Close'].ewm(span=9, adjust=False).mean()
    ema_21=ema_short = df['Adj Close'].ewm(span=21, adjust=False).mean()
    ema_50=ema_short = df['Adj Close'].ewm(span=50, adjust=False).mean()
    ema_12=ema_short = df['Adj Close'].ewm(span=12, adjust=False).mean()
    ema_26=ema_short = df['Adj Close'].ewm(span=26, adjust=False).mean()
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
    del df['Close']
    del df['Low']
    del df['Open']
    








    data = df['MA200'].iloc[-30:].tolist()
    df_unix_sec = pd.to_datetime(df.index[-30:]).astype(int)/ 10**9
    index = df_unix_sec.tolist()
    #print (index)








    








    #print('teste')
  
        
    if df['Adj Close'].iloc[-1]>df['MA150'].iloc[-1] and df['Adj Close'].iloc[-1]>df['MA200'].iloc[-1]:
        if df['MA150'].iloc[-1]>df['MA200'].iloc[-1]:
            if df['MA50'].iloc[-1]>df['MA150'].iloc[-1] and df['MA50'].iloc[-1]>df['MA200'].iloc[-1]:
                if df['Adj Close'].iloc[-1]>df['MA50'].iloc[-1]:
                    
                    if df['Adj Close'].iloc[-1]>1.3*df['min52'].iloc[-1]:
                        resultent=trendline(index,data)
                        
                        if df['Adj Close'].iloc[-1]>0.75*df['max52'].iloc[-1]:
                            if resultent>0:
                                q1=((df['Adj Close'].iloc[-150]-df['Adj Close'].iloc[-200])/df['Adj Close'].iloc[-200])*100
                                q2=((df['Adj Close'].iloc[-100]-df['Adj Close'].iloc[-150])/df['Adj Close'].iloc[-150])*100
                                q3=((df['Adj Close'].iloc[-50]-df['Adj Close'].iloc[-100])/df['Adj Close'].iloc[-100])*100
                                q4=((df['Adj Close'].iloc[-1]-df['Adj Close'].iloc[-50])/df['Adj Close'].iloc[-50])*100
                                RS=(q1+q2+q3+2*q4)/5
                                new_row={'ACAO' : Acao, 'RS' : RS}
                                df2=df2.append(new_row, ignore_index=True)
                                #print (Acao)
                                
                            #print(df.index[-1])
                            #print (round(df['Close'].iloc[-1],2))
                            #print (str(round(returns_acao['Close'].iloc[-1]*100,2))+"%")
result=df2.sort_values('RS',ascending=False)
pd.set_option('display.max_rows', 10000)
print (result)




#writer=pd.ExcelWriter('Minervini.xlsx')
#df2.to_excel(writer,'Minervini',index=False,engine="xlsxwriter")
#writer.save()