import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import seaborn as sns
import datetime
from datetime import datetime
import time
import matplotlib.pyplot as plt
import yfinance as yf
# %matplotlib inline

teste = ['AALR3.SA',
         'AFLT3.SA',
         'AGRO3.SA',
         'ALSO3.SA',
         'ALUP11.SA',
         'ALUP3.SA',
         'ALUP4.SA',
         'AMAR3.SA',
         'APER3.SA',
         'AZUL4.SA',
         'BALM3.SA',
         'BALM4.SA',
         'BBAS3.SA',
         'BBDC3.SA',
         'BBDC4.SA',
         'BBRK3.SA',
         'BBSE3.SA',
         'BDLL3.SA',
         'BDLL4.SA',
         'BEEF3.SA',
         'BIDI11.SA',
         'BIDI3.SA',
         'BIDI4.SA',
         'BIOM3.SA',
         'BMGB4.SA',
         'BPAN4.SA',
         'BPAR3.SA',
         'BRAP3.SA',
         'BRAP4.SA',
         'BRDT3.SA',
         'BRFS3.SA',
         'BRKM3.SA',
         'BRKM5.SA',
         'BRKM6.SA',
         'BRML3.SA',
         'BRPR3.SA',
         'BRSR3.SA',
         'BRSR5.SA',
         'BRSR6.SA',
         'BSEV3.SA',
         'BSLI3.SA',
         'BSLI4.SA',
         'BTTL3.SA',
         'CAML3.SA',
         'CARD3.SA',
         'CASN3.SA',
         'CASN4.SA',
         'CCRO3.SA',
         'CEAB3.SA',
         'CEBR3.SA',
         'CEBR5.SA',
         'CEBR6.SA',
         'CEED3.SA',
         'CEED4.SA',
         'CEGR3.SA',
         'CEPE3.SA',
         'CEPE5.SA',
         'CEPE6.SA',
         'CESP3.SA',
         'CESP5.SA',
         'CESP6.SA',
         'CGAS3.SA',
         'CGAS5.SA',
         'CGRA3.SA',
         'CGRA4.SA',
         'CLSC3.SA',
         'CLSC4.SA',
         'CMIG3.SA',
         'CMIG4.SA',
         'COCE3.SA',
         'COCE5.SA',
         'COCE6.SA',
         'COGN3.SA',
         'CPFE3.SA',
         'CPLE3.SA',
         'CPLE5.SA',
         'CPLE6.SA',
         'CPRE3.SA',
         'CRFB3.SA',
         'CSNA3.SA',
         'CTKA3.SA',
         'CTKA4.SA',
         'CTNM3.SA',
         'CTNM4.SA',
         'CVCB3.SA',
         'CYRE3.SA',
         'DIRR3.SA',
         'DMMO3.SA',
         'EALT3.SA',
         'EALT4.SA',
         'EEEL3.SA',
         'EEEL4.SA',
         'EGIE3.SA',
         'ENAT3.SA',
         'ENEV3.SA',
         'ESTR3.SA',
         'ESTR4.SA',
         'ETER3.SA',
         'EUCA3.SA',
         'EUCA4.SA',
         'EVEN3.SA',
         'EZTC3.SA',
         'FESA3.SA',
         'FLRY3.SA',
         'GBIO33.SA',
         'GEPA3.SA',
         'GEPA4.SA',
         'GFSA3.SA',
         'GOAU4.SA',
         'GOLL4.SA',
         'GRND3.SA',
         'GSHP3.SA',
         'HBOR3.SA',
         'HOOT4.SA',
         'HYPE3.SA',
         'IGBR3.SA',
         'IGTA3.SA',
         'INEP3.SA',
         'INEP4.SA',
         'IRBR3.SA',
         'ITSA4.SA',
         'ITUB3.SA',
         'ITUB4.SA',
         'JBSS3.SA',
         'JHSF3.SA',
         'KLBN11.SA',
         'KLBN3.SA',
         'KLBN4.SA',
         'LAME3.SA',
         'LAME4.SA',
         'LCAM3.SA',
         'LEVE3.SA',
         'LINX3.SA',
         'LIQO3.SA',
         'LLIS3.SA',
         'LOGG3.SA',
         'LPSB3.SA',
         'LREN3.SA',
         'LUPA3.SA',
         'LWSA3.SA',
         'MDIA3.SA',
         'MDNE3.SA',
         'MGLU3.SA',
         'MMXM11.SA',
         'MMXM3.SA',
         'MNDL3.SA',
         'MOVI3.SA',
         'MRFG3.SA',
         'MRVE3.SA',
         'MTRE3.SA',
         'MULT3.SA',
         'MYPK3.SA',
         'NEOE3.SA',
         'NTCO3.SA',
         'ODPV3.SA',
         'OIBR3.SA',
         'OIBR4.SA',
         'OSXB3.SA',
         'PARD3.SA',
         'PCAR3.SA',
         'PDGR3.SA',
         'PETR3.SA',
         'PETR4.SA',
         'PMAM3.SA',
         'PNVL3.SA',
         'PNVL4.SA',
         'POMO3.SA',
         'POMO4.SA',
         'POSI3.SA',
         'PRIO3.SA',
         'PSSA3.SA',
         'QUAL3.SA',
         'RADL3.SA',
         'RAIL3.SA',
         'RANI3.SA',
         'RANI4.SA',
         'RAPT3.SA',
         'RAPT4.SA',
         'RDNI3.SA',
         'RENT3.SA',
         'RLOG3.SA',
         'RNEW11.SA',
         'RNEW3.SA',
         'RNEW4.SA',
         'RPMG3.SA',
         'RSID3.SA',
         'SANB11.SA',
         'SANB3.SA',
         'SANB4.SA',
         'SAPR11.SA',
         'SAPR3.SA',
         'SAPR4.SA',
         'SBSP3.SA',
         'SCAR3.SA',
         'SEER3.SA',
         'SHUL3.SA',
         'SHUL4.SA',
         'SLED3.SA',
         'SLED4.SA',
         'SMLS3.SA',
         'SMTO3.SA',
         'STBP3.SA',
         'SUZB3.SA',
         'TAEE11.SA',
         'TAEE3.SA',
         'TAEE4.SA',
         'TASA3.SA',
         'TASA4.SA',
         'TCSA3.SA',
         'TELB3.SA',
         'TELB4.SA',
         'TIET11.SA',
         'TIET3.SA',
         'TIET4.SA',
         'TIMP3.SA',
         'TOTS3.SA',
         'TPIS3.SA',
         'TRPL3.SA',
         'TRPL4.SA',
         'UGPA3.SA',
         'UNIP3.SA',
         'UNIP5.SA',
         'UNIP6.SA',
         'USIM3.SA',
         'USIM5.SA',
         'USIM6.SA',
         'VALE3.SA',
         'VIVA3.SA',
         'VIVT3.SA',
         'VIVT4.SA',
         'VLID3.SA',
         'VVAR3.SA',
         'WEGE3.SA',
         'WHRL3.SA',
         'WHRL4.SA',
         'YDUQ3.SA'
         ]


df2 = pd.DataFrame()
df2['ACAO'] = 'teste'
df2['RS'] = 'teste'


venda = 0
compra = 0
count = 0


def trendline(index, data, order=1):
    coeffs = np.polyfit(index, data, order)
    #print (coeffs)
    slope = coeffs[-2]
    return float(slope)


def request():
    PG = wb.DataReader(Acao, data_source="yahoo", start=Periodo)
    return (PG)


for ticks in teste:
    print(ticks)
    Acao = ticks
    fim = '2020-06-26'
    Periodo = '2020-04-02'
    while True:
        try:
            PG = request()
           # print(type(PG))
        except Exception as e:
            continue
        break

    df = pd.DataFrame(PG)
    rsi_period = 14
    chg = df['Adj Close'].diff(1)
    gain = chg.mask(chg < 0, 0)
    loss = chg.mask(chg > 0, 0)
    avg_gain = gain.ewm(com=rsi_period-1, min_periods=rsi_period).mean()
    avg_loss = loss.ewm(com=rsi_period-1, min_periods=rsi_period).mean()
    rs = abs(avg_gain/avg_loss)
    rsi = 100-(100/(1+rs))
    df['RSI'] = rsi


# Separando Close para as Médias e criando as médias
    close = df[['Adj Close']]

    ma_3 = close.rolling(window=3).mean()
    ma_3.columns = ['MA 3']

    ma_8 = close.rolling(window=8).mean()
    ma_8.columns = ['MA 8']

    ma_20 = close.rolling(window=20).mean()
    ma_20.columns = ['MA 20']

    min52 = close.rolling(window=250).min()
    max52 = close.rolling(window=250).max()

    df['MA 8'] = ma_8
    df['MA 20'] = ma_20
    df['MA 3'] = ma_3
    df['RSI'] = rsi
    df['min52'] = min52
    df['max52'] = max52
    df['Normal 20'] = (df['MA 20']/df['MA 8'])-1
    df['Normal 3'] = (df['MA 3']/df['MA 8'])-1
    df['Normal 8'] = (df['MA 8']/df['MA 8'])-1

#ax = plt.gca()
#df.plot(kind='line',y='Normal 8', color='black', ax=ax,title=Acao)
#df.plot(kind='line',y='Normal 20', color='brown', ax=ax)
#df.plot(kind='line',y='Normal 3', color='green', ax=ax)
# plt.show()

#ax = plt.gca()
#df.plot(kind='line',y='Adj Close', color='black', ax=ax, title=Acao)

# plt.show()

    superior = 10
    inferior = superior*(-1)

    del df['High']
    del df['Close']
    del df['Low']
    del df['Open']
    count = count+1
    flag = 0
    testefinal = superior
# print(Acao)
    if df['Normal 20'].iloc[-1] > inferior and df['Normal 20'].iloc[-1] < superior:
        if df['Normal 3'].iloc[-1] > inferior and df['Normal 3'].iloc[-1] < superior:
            if df['Normal 3'].iloc[-1] > df['Normal 3'].iloc[-3] and df['Normal 20'].iloc[-1] < df['Normal 20'].iloc[-2]:
                if df['Normal 3'].iloc[-1] > (testefinal*-1) and df['Normal 20'].iloc[-1] < testefinal:
                    compra = compra+1
                    if flag == 1:
                        print(df.index[-1])
                        print(Acao)
                        print("Compra")
                        ax = plt.gca()
                        df.plot(kind='line', y='Normal 8',
                                color='black', ax=ax, title=Acao)
                        df.plot(kind='line', y='Normal 20',
                                color='brown', ax=ax)
                        df.plot(kind='line', y='Normal 3',
                                color='green', ax=ax)
                    # plt.show()

    if df['Normal 20'].iloc[-1] > inferior and df['Normal 20'].iloc[-1] < superior:
        if df['Normal 3'].iloc[-1] > inferior and df['Normal 3'].iloc[-1] < superior:
            if df['Normal 3'].iloc[-1] < df['Normal 3'].iloc[-3] and df['Normal 20'].iloc[-1] > df['Normal 20'].iloc[-2]:
                if df['Normal 3'].iloc[-1] < testefinal and df['Normal 20'].iloc[-1] > (testefinal*-1):
                    venda = venda+1
                    if flag == 1:
                        print(df.index[-1])
                        print(Acao)
                        print('Venda')
                        ax = plt.gca()
                        df.plot(kind='line', y='Normal 8',
                                color='black', ax=ax, title=Acao)
                        df.plot(kind='line', y='Normal 20',
                                color='brown', ax=ax)
                        df.plot(kind='line', y='Normal 3',
                                color='green', ax=ax)
                        # plt.show()


print(fim)
print("Total: "+str(count))
print("Venda: "+str(venda)+"; "+str(venda*100/count)+"%")
print("Compra: "+str(compra)+"; "+str(compra*100/count)+"%")
print("Compra-Venda: "+str(compra-venda))
print("Razão Compra/Venda: "+str(compra/venda))
