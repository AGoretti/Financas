from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import requests
import csv


ticks = ['AALR3',
         'AFLT3',
         'AGRO3',
         'ALSO3',
         'ALUP1',
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
         'BIDI1',
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
         'DMMO1',
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
         'GOLL1',
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
         'KLBN1',
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
         'MMXM1',
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
         ]

ticks2 = ['AALR3']

select = False

nomes = []

ebit = False

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

cabeca = 'Tick', 'Cotacao', 'N.acoes', 'Ebit'


with open('valores.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(cabeca)


for tick in ticks:

    cont = 0

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

        if cont == 6:
            select = True
            cont = cont + 1

        if select == True:
            select = False
            ticksValores.append(td.text)

        if 'Cotação' in td.text:
            select = True
        if 'Nro. Ações' in td.text:
            select = True

        if 'EBIT' in td.text:
            cont = cont + 1

    with open('valores.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ticksValores)
