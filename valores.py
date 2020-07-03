from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import requests
import csv
import pandas as pd
import string


ticks = ['AALR3',
         'AFLT3',
         'AGRO3',
         'ALSO3',
         'ALUP11',
         'ALUP3',
         'ALUP4',
         'AMAR3',
         'APER3',
         'AZUL4',
         'BALM3',
         'BALM4',
         'BBAS3',
         'BBDC3',
         'BBDC4',
         'BBRK3',
         'BBSE3',
         'BDLL3',
         'BDLL4',
         'BEEF3',
         'BIDI11',
         'BIDI3',
         'BIDI4',
         'BIOM3',
         'BMGB4',
         'BPAN4',
         'BPAR3',
         'BRAP3',
         'BRAP4',
         'BRDT3',
         'BRFS3',
         'BRKM3',
         'BRKM5',
         'BRKM6',
         'BRML3',
         'BRPR3',
         'BRSR3',
         'BRSR5',
         'BRSR6',
         'BSEV3',
         'BSLI3',
         'BSLI4',
         'BTTL3',
         'CAML3',
         'CARD3',
         'CASN3',
         'CASN4',
         'CCRO3',
         'CEAB3',
         'CEBR3',
         'CEBR5',
         'CEBR6',
         'CEED3',
         'CEED4',
         'CEGR3',
         'CEPE3',
         'CEPE5',
         'CEPE6',
         'CESP3',
         'CESP5',
         'CESP6',
         'CGAS3',
         'CGAS5',
         'CGRA3',
         'CGRA4',
         'CLSC3',
         'CLSC4',
         'CMIG3',
         'CMIG4',
         'COCE3',
         'COCE5',
         'COCE6',
         'COGN3',
         'CPFE3',
         'CPLE3',
         'CPLE5',
         'CPLE6',
         'CPRE3',
         'CRFB3',
         'CSNA3',
         'CTKA3',
         'CTKA4',
         'CTNM3',
         'CTNM4',
         'CVCB3',
         'CYRE3',
         'DIRR3',
         'DMMO3',
         'EALT3',
         'EALT4',
         'EEEL3',
         'EEEL4',
         'EGIE3',
         'ENAT3',
         'ENEV3',
         'ESTR3',
         'ESTR4',
         'ETER3',
         'EUCA3',
         'EUCA4',
         'EVEN3',
         'EZTC3',
         'FESA3',
         'FLRY3',
         'GBIO33',
         'GEPA3',
         'GEPA4',
         'GFSA3',
         'GOAU4',
         'GOLL4',
         'GRND3',
         'GSHP3',
         'HBOR3',
         'HOOT4',
         'HYPE3',
         'IGBR3',
         'IGTA3',
         'INEP3',
         'INEP4',
         'IRBR3',
         'ITSA4',
         'ITUB3',
         'ITUB4',
         'JBSS3',
         'JHSF3',
         'KLBN11',
         'KLBN3',
         'KLBN4',
         'LAME3',
         'LAME4',
         'LCAM3',
         'LEVE3',
         'LINX3',
         'LIQO3',
         'LLIS3',
         'LOGG3',
         'LPSB3',
         'LREN3',
         'LUPA3',
         'LWSA3',
         'MDIA3',
         'MDNE3',
         'MGLU3',
         'MMXM11',
         'MMXM3',
         'MNDL3',
         'MOVI3',
         'MRFG3',
         'MRVE3',
         'MTRE3',
         'MULT3',
         'MYPK3',
         'NEOE3',
         'NTCO3',
         'ODPV3',
         'OIBR3',
         'OIBR4',
         'OSXB3',
         'PARD3',
         'PCAR3',
         'PDGR3',
         'PETR3',
         'PETR4',
         'PMAM3',
         'PNVL3',
         'PNVL4',
         'POMO3',
         'POMO4',
         'POSI3',
         'PRIO3',
         'PSSA3',
         'QUAL3',
         'RADL3',
         'RAIL3',
         'RANI3',
         'RANI4',
         'RAPT3',
         'RAPT4',
         'RDNI3',
         'RENT3',
         'RLOG3',
         'RNEW11',
         'RNEW3',
         'RNEW4',
         'RPMG3',
         'RSID3',
         'SANB11',
         'SANB3',
         'SANB4',
         'SAPR11',
         'SAPR3',
         'SAPR4',
         'SBSP3',
         'SCAR3',
         'SEER3',
         'SHUL3',
         'SHUL4',
         'SLED3',
         'SLED4',
         'SMLS3',
         'SMTO3',
         'STBP3',
         'SUZB3',
         'TAEE11',
         'TAEE3',
         'TAEE4',
         'TASA3',
         'TASA4',
         'TCSA3',
         'TELB3',
         'TELB4',
         'TIET11',
         'TIET3',
         'TIET4',
         'TIMP3',
         'TOTS3',
         'TPIS3',
         'TRPL3',
         'TRPL4',
         'UGPA3',
         'UNIP3',
         'UNIP5',
         'UNIP6',
         'USIM3',
         'USIM5',
         'USIM6',
         'VALE3',
         'VIVA3',
         'VIVT3',
         'VIVT4',
         'VLID3',
         'VVAR3',
         'WEGE3',
         'WHRL3',
         'WHRL4',
         'YDUQ3'
         ]


ticks2 = ['AALR3']


select = False


nomes = []


ebit = False


with open('valoresF.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    file.close()

with open('valores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    file.close()

with open('ValoresFinal.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    file.close()


header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}


cabeca = 'Tick', 'Cotacao', 'Setor', 'Vol. Med', 'Valor Mercado', 'Valor Firma', 'N.acoes', 'P/L', 'LPA', 'P/VP', 'VPA',  'P/EBIT', 'Marg. Bruta',  'PSR', 'Marg. EBIT', 'Marg. Líquida', 'ROIC', 'Div. Yield', 'ROE',  'EV / EBITDA', 'EV / EBIT', 'Cres. Rec (5a)', 'Ativo', 'Dív. Bruta', 'Disponibilidades', 'Dív. Líquida', 'Ativo Circulante', 'Patrim. Líq', 'Receita Líquida 12', 'Receita Líquida 3',  'Ebit 12', 'Ebit 3', 'Lucro Líquido 12', 'Lucro Líquido 3'


cabecaF = 'Tick', 'Cotacao', 'Setor', 'Vol. Med', 'Valor Mercado', 'Valor Firma', 'N.acoes', 'P/L', 'LPA', 'P/VP', 'VPA',  'P/EBIT', 'Marg. Bruta',  'PSR', 'Marg. EBIT', 'Marg. Líquida', 'ROIC', 'Div. Yield', 'ROE',  'EV / EBITDA', 'EV / EBIT', 'Cres. Rec (5a)', 'Ativo', 'Patrim. Líq', 'Lucro Líquido 12', 'Lucro Líquido 3'


with open('valores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cabeca)


with open('valoresF.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cabecaF)


for tick in ticks:

    contebit = 0

    contativo = 0

    ticksValores = []

    ticksValores.append(tick)

    pagina = 'https://www.fundamentus.com.br/detalhes.php?papel=' + tick

    # print(pagina)

    resultPagina = requests.get(pagina, headers=header, verify=True)

    print(tick)
    print(resultPagina.status_code)

    srcMain = resultPagina.content

    soup = BeautifulSoup(srcMain, 'lxml')

    tds = soup.find_all('td')

    for td in tds:

        if contebit == 6:
            select = True
            contebit = contebit + 1

        if contebit == 8:
            select = True
            contebit = contebit + 1

        if contativo == 4:
            select = True
            contativo = contativo + 1

        if select == True:
            select = False
            temp = td.text
            if temp.startswith('\n'):
                temp = temp[-5:]
            ticksValores.append(temp)

        if 'Cotação' in td.text:
            select = True
        if 'Nro. Ações' in td.text:
            select = True
        if 'Setor' in td.text:
            select = True
        if 'Vol' in td.text:
            select = True
        if 'mercado' in td.text:
            select = True
        if 'firma' in td.text:
            select = True
        if 'P/L' in td.text:
            select = True
        if 'P/VP' in td.text:
            select = True
        if 'P/EBIT' in td.text:
            select = True
        if 'PSR' in td.text:
            select = True
        if 'Yield' in td.text:
            select = True
        if 'EV / EBIT' in td.text:
            select = True
        if '(5a)' in td.text:
            select = True
        if 'LPA' in td.text:
            select = True
        if 'VPA' in td.text:
            select = True
        if 'Marg. Bruta' in td.text:
            select = True
        if 'Marg. EBIT' in td.text:
            select = True
        if 'Marg. Líquida' in td.text:
            select = True
        if 'ROIC' in td.text:
            select = True
        if 'ROE' in td.text:
            select = True
        if 'Dív. Bruta' in td.text:
            select = True
        if 'Disponibilidades' in td.text:
            select = True
        if 'Dív. Líquida' in td.text:
            select = True
        if 'Ativo Circulante' in td.text:
            select = True
        if 'Patrim. Líq' in td.text:
            select = True
        if 'Receita Líquida' in td.text:
            select = True
        if 'Lucro Líquido' in td.text:
            select = True

        if 'EBIT' in td.text:
            contebit = contebit + 1

        if 'Ativo' in td.text:
            contativo = contativo + 1

    print(ticksValores)

    try:
        if (ticksValores[2] == 'Financeiros') and (ticksValores[0] != 'ITSA4'):
            with open('valoresF.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(ticksValores)
        else:
            with open('valores.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(ticksValores)

    except Exception as e:
        print('pagina nao achada')
        pass


df1 = pd.read_csv('valores.csv', encoding='latin1')
df2 = pd.read_csv('valoresF.csv', encoding='latin1')
frames = [df1, df2]
result = pd.concat(frames)
for coluna in result.columns:
    result[coluna] = result[coluna].str.replace('-', '')
    result[coluna] = result[coluna].str.replace('    ', '')


for coluna in ['Vol. Med', 'Valor Mercado', 'Valor Firma', 'N.acoes', 'Ativo', 'Dív. Bruta', 'Disponibilidades', 'Dív. Líquida', 'Ativo Circulante', 'Patrim. Líq', 'Receita Líquida 12', 'Receita Líquida 3',  'Ebit 12', 'Ebit 3', 'Lucro Líquido 12', 'Lucro Líquido 3']:

    result[coluna] = result[coluna].str.replace('.', '')


for coluna in ['Marg. Bruta', 'Marg. EBIT', 'Marg. Líquida', 'ROIC', 'Div. Yield', 'ROE', 'Cotacao', 'P/L', 'VPA', 'P/VP', 'PSR']:
    result[coluna] = result[coluna].str.replace(',', '.')

    result[coluna] = result[coluna].str.rstrip('%')
for coluna in ['P/EBIT', 'EV / EBITDA', 'EV / EBIT']:
    result[coluna] = result[coluna].str.replace(',', '.')

result.to_csv('ValoresFinal.csv')
for coluna in result.columns:
    try:
        result2[coluna] = pd.to_numeric(result[coluna])
    except:
        continue
