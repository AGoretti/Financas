import requests
from bs4 import BeautifulSoup

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

pagina = "http://bvmf.bmfbovespa.com.br/cias-listadas/empresas-listadas/ResumoDemonstrativosFinanceiros.aspx?codigoCvm=20575&idioma=pt-br"

listaTabelas = []

resultPagina = requests.get(pagina, headers=header, verify=False)

print(resultPagina.status_code)

# print(resultPagina.headers)

srcMain = resultPagina.content
# print(srcMain)

soup = BeautifulSoup(srcMain, 'lxml')

links = soup.find_all('a')
# print(links)


for link in links:
    if "Trimestrais" in link.text:
        # print(link)
        # print(link.attrs['href'][36:156])
        listaTabelas.append(link.attrs['href'][36:156])

for link in listaTabelas:
    paginaTabela = link
    # print(paginaTabela)
    resultPaginaTabela = requests.get(
        paginaTabela, headers=header, verify=False)

    print(resultPagina.status_code)

    srcTabela = resultPaginaTabela.content

    soup = BeautifulSoup(srcTabela, 'lxml')

    tds = soup.find_all("tr")

    print(srcMain)

    for td in tds:
        if "Resultado Antes do Resultado Financeiro e dos Tributos" in td.text:
            print(td[1].text)
