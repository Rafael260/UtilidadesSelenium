# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time, os, sys
from util import utilidades

usuario = sys.argv[1]
senha = sys.argv[2]

driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url = "http://t-pristina:8080/grh"
nomeScript = os.path.basename(__file__)
utilidades.inicializar_diretorio_prints(nomeScript)

utilidades.acessar(driver,base_url)
utilidades.logar(driver,nomeScript, usuario, senha)
parametros = utilidades.get_parametros_script(nomeScript)

#driver.get(base_url+ "/f/pages/servidor/servidor.xhtml")
utilidades.acessar(driver,base_url + "/f/pages/servidor/servidor.xhtml")

utilidades.clicar(driver,By.ID,"btnList")
matriculaTeste = parametros['matricula']
utilidades.digitar(driver, By.ID, "frmSearch:matriculaPesquisa_input", matriculaTeste)
utilidades.tirar_print(driver,nomeScript,"Pesquisando servidor")
tentativasAutoComplete = 3
while(tentativasAutoComplete > 0):
	try:
		utilidades.esperar_elemento(driver,By.CSS_SELECTOR,"span.ui-autocomplete-query",10)
		break
	except TimeoutException:
	    print("Não conseguiu encontrar a opção de autocomplete da matrícula")
	    tentativasAutoComplete -= 1
	    if(tentativasAutoComplete == 0):
	    	sys.exit(-1)
	    else:
	    	utilidades.digitar(driver, By.ID, "frmSearch:matriculaPesquisa_input", matriculaTeste)

utilidades.clicar(driver,By.CSS_SELECTOR,"span.ui-autocomplete-query")
utilidades.tirar_print(driver,nomeScript,"Digitou a matrícula e vai clicar em pesquisar")
utilidades.clicar(driver,By.ID,"frmSearch:btnSearch")
utilidades.clicar(driver,By.ID,"frmSearchList:dtTable:0:btnView")
try:
	utilidades.clicar(driver,By.ID,"frmSearchList:dtTable:0:btnView")
except:
	print("Deu problema ao tentar clicar de novo em Consultar")

try:
	utilidades.esperar_elemento(driver,By.ID,"frmSave:panelFormServidor",60)
except TimeoutException:
    print("Não encontrou o form do servidor")
    sys.exit(-1)

utilidades.tirar_print(driver,nomeScript,"Exibindo informações do servidor")
utilidades.clicar(driver, By.LINK_TEXT, "Dados Funcionais")
try:
	utilidades.esperar_elemento(driver,By.ID, "frmSave:tabViewFormServidor:matricula",60)
except TimeoutException:
	print("Não encontrou as informações funcionais do servidor")
	sys.exit(-1)

time.sleep(1)
utilidades.tirar_print(driver,nomeScript,"Visualizando dados funcionais do servidor")

textoCategoriaFuncional = utilidades.encontrar_elemento(driver, By.ID, "frmSave:tabViewFormServidor:categoriaFuncional_label").text
print("categoria esperada: "+ parametros['nomeacaoEsperada'])

if(textoCategoriaFuncional != parametros['nomeacaoEsperada']):
    print("Nomeação diferente do esperado: "+ textoCategoriaFuncional)
else:
    print("Nomeação conforme esperado:" + textoCategoriaFuncional)

time.sleep(2)    
utilidades.tirar_print(driver,nomeScript, "Categoria funcional verificada")
utilidades.salvar_documento_interacao(nomeScript)
driver.close()