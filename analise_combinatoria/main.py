from selenium import webdriver
from random import choice
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chromium.options import ChromiumOptions

#define o caminho do executável do navegador(nesse caso o chromium pq o chrome n estava funcionando :( )
options = ChromiumOptions()
options.binary_location = '/usr/bin/chromium-browser'

#faz com que a janela continue aberta depois de rodar o script 
options.add_experimental_option("detach",True)

#define o caminho do webdriver que vai ser utilizado(depende do navegador que está sendo utilizado)
servico = ChromiumService('/usr/bin/chromedriver')
navegador = webdriver.ChromiumEdge(service=servico,options=options)

#acessa a página 
navegador.get("http://localhost/analise_combinatoria/insta.html")

#acessa a div onde estão os elementos que serão utilizados(pelo id 'container') 
container = navegador.find_element('xpath', '//*[@id="container"]')

#as letras que vão ser utilizadas para a criação das senhas
letras = ['a','t','s','c']

senhas = []
tentativas = 0

#loop que vai durar enquanto o bot não logar na página
while container.get_attribute('innerHTML') != "logado":

    #variável que armazena a senha utilizada no teste
    senha = ''

    #enquanto a variável senha não possuir 4 digitos, adicione mais uma letra aleatoriamente :)
    while len(senha) < 4:
        letra = choice(letras)
        senha += letra

    #se essa senha não estiver na lista
    if senha not in senhas:
        tentativas += 1

        #adiciona a senha à lista
        senhas.append(senha)

        #procura pelo campo de nome de usuário e insere o nome saorikido ;-;
        navegador.find_element('xpath', '//*[@id="username"]').send_keys("saorikido")

        #procura pelo campo de senha e insere a senha que está criada aleatoriamente
        navegador.find_element('xpath', '//*[@id="password"]').send_keys(senha)

        #clica no botão de logar :)
        navegador.find_element('xpath', '//*[@id="container"]/div[1]/div[3]/button').click()
    
        print(f'combinação n° {tentativas} : {senha}')

print(f'n° de combinações posíveis com as 4 letras:256 \nn° de combinações para chegar na senha:{tentativas}')