import pandas as pd
import numpy as np
import cufflinks as cf
import plotly as py
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_finance import candlestick_ohlc
import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as plticker
from matplotlib.dates import DateFormatter

teste=['ABEV3.SA',
'AZUL4.SA',
'B3SA3.SA',
'BBAS3.SA',
'BBDC3.SA',
'BBDC4.SA',
'BBSE3.SA',
'BRAP4.SA',
'BRDT3.SA',
'BRFS3.SA',
'BRKM5.SA',
'BRML3.SA',
'BTOW3.SA',
'CCRO3.SA',
'CIEL3.SA',
'CMIG4.SA',
'CSAN3.SA',
'CVCB3.SA',
'CYRE3.SA',
'ECOR3.SA',
'EGIE3.SA',
'ELET3.SA',
'ELET6.SA',
'EMBR3.SA',
'ENBR3.SA',
'EQTL3.SA',
'FLRY3.SA',
'GGBR4.SA',
'GOAU4.SA',
'GOLL4.SA',
'HYPE3.SA',
'IGTA3.SA',
'IRBR3.SA',
'ITSA4.SA',
'ITUB4.SA',
'JBSS3.SA',
'KLBN11.SA',
'KROT3.SA',
'LAME4.SA',
'LREN3.SA',
'MGLU3.SA',
'MRFG3.SA',
'MRVE3.SA',
'MULT3.SA',
'NATU3.SA',
'PCAR4.SA',
'PETR3.SA',
'PETR4.SA',
'QUAL3.SA',
'RADL3.SA',
'RAIL3.SA',
'RENT3.SA',
'SANB11.SA',
'SBSP3.SA',
'SMLS3.SA',
'SUZB3.SA',
'TAEE11.SA',
'TIMP3.SA',
'UGPA3.SA',
'USIM5.SA',
'VALE3.SA',
'VIVT4.SA',
'VVAR3.SA',
'WEGE3.SA']



%matplotlib inline

cf.go_offline()

Acao='jhsf3.sa'
Periodo="2010-01-01"
PG = wb.DataReader(Acao,data_source="yahoo",start=Periodo)
df=pd.DataFrame(PG)
#qf=cf.QuantFig(df,title=Acao,legend='top',name='GS')
#qf.add_sma([9,21,50,200],width=2,color=['green','lightgreen', 'yellow','blue'],legendgroup=True)
#qf.add_rsi(periods=14, rsi_upper=70, rsi_lower=30, showbands=True, color='deeppink')
#qf.add_volume()
#qf.add_macd()
#qf.iplot()

Janela_media_50=9
Janela_media_100=21
Janela_media_200=200
media150=150
media50=50

rsi_period=14
chg=df['Close'].diff(1)
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
ma_50=close.rolling(window=Janela_media_50).mean()
ma_50.columns=['MA 9']
#MA21
ma_100=close.rolling(window=Janela_media_100).mean()
ma_100.columns=['MA 21']
#MA200
ma_200=close.rolling(window=Janela_media_200).mean()
ma_200.columns=['MA 200']
ema_short = df['Close'].ewm(span=9, adjust=False).mean()
#ma_50['EMA 50']=0
#print (ma_50)
ema_9=ema_short = df['Close'].ewm(span=9, adjust=False).mean()
ema_21=ema_short = df['Close'].ewm(span=21, adjust=False).mean()
ema_50=ema_short = df['Close'].ewm(span=50, adjust=False).mean()
#Organização dos candles


min52=close.rolling(window=52).min()
max52=close.rolling(window=52).max()


df['MA9']=ma_50
df['MA21']=ma_100
df['MA200']=ma_200
df['EMA9']=ema_9
df['EMA21']=ema_21
df['EMA50']=ema_50
df['MA50']=ma50
df['MA150']=ma150
df['RSI']=rsi
df['min52']=min52
df['max52']=max52

del df['High']
del df['Adj Close']
del df['Low']
del df['Open']
returns_acao=close.pct_change()
returns_acao = returns_acao.iloc[1:]
#returns_acao.plot(y='Close')
#print (returns_acao)

#sns.distplot(returns_acao) 

#sns.heatmap(df.corr(), annot=True)

#print (df['RSI'])


print (Acao)
for index, row in df.iterrows():
    
    if row['Close']>row['MA150'] and row['Close']>row['MA200']:
        if row['MA150']>row['MA200']:
            if row['MA50']>row['MA150'] and row['MA50']>row['MA200']:
                if row['Close']>row['MA50']:
                    
                    if row['Close']>1.3*row['min52']:
                        
                        if row['Close']>0.75*row['max52']:
                            
                                
                            print(index)
                            print (row['Close'])