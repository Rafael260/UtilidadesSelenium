import sys
sys.path.append('..')
sys.path.append('...')
from BasePage import *
from GRHHomePage import *
from selenium.webdriver.common.by import By
import utilidades

class GRHServidorPage(BasePage):
	def __init__(self, browser,nomeScript):
		super(GRHServidorPage,self).__init__(browser,nomeScript)

	def acessar_busca_servidor(self):
		utilidades.clicar(self.browser,By.ID,"btnList")

	def buscar_servidor(self, matricula):
		utilidades.digitar(self.browser, By.ID, "frmSearch:matriculaPesquisa_input", matricula)
		utilidades.tirar_print(self.browser,nomeScript,"Pesquisando servidor")
		tentativasAutoComplete = 3
		while(tentativasAutoComplete > 0):
			try:
				utilidades.esperar_elemento(self.browser,By.CSS_SELECTOR,"span.ui-autocomplete-query",10)
				break
			except TimeoutException:
	    		print("Não conseguiu encontrar a opção de autocomplete da matrícula")
	    		tentativasAutoComplete -= 1
	    		if(tentativasAutoComplete == 0):
	    			sys.exit(-1)
	    		else:
	    			utilidades.digitar(self.browser, By.ID, "frmSearch:matriculaPesquisa_input", matriculaTeste)

		utilidades.clicar(self.browser,By.CSS_SELECTOR,"span.ui-autocomplete-query")
		utilidades.tirar_print(self.browser,nomeScript,"Digitou a matrícula e vai clicar em pesquisar")
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

    def abrir_dados_funcionais(self):
    	utilidades.clicar(driver, By.LINK_TEXT, "Dados Funcionais")
    	try:
			utilidades.esperar_elemento(driver,By.ID, "frmSave:tabViewFormServidor:matricula",60)
		except TimeoutException:
			print("Não encontrou as informações funcionais do servidor")
			sys.exit(-1)
		time.sleep(1)
		utilidades.tirar_print(driver,nomeScript,"Visualizando dados funcionais do servidor")

    def verificar_nomeacao_servidor(self,cargoEsperado):
    	textoCategoriaFuncional = utilidades.encontrar_elemento(driver, By.ID, "frmSave:tabViewFormServidor:categoriaFuncional_label").text
		print("categoria esperada: "+ cargoEsperado)
		if(textoCategoriaFuncional != cargoEsperado):
    		print("Nomeação diferente do esperado: "+ textoCategoriaFuncional)
		else:
    		print("Nomeação conforme esperado:" + textoCategoriaFuncional)
		time.sleep(2)    
		utilidades.tirar_print(driver,nomeScript, "Categoria funcional verificada")