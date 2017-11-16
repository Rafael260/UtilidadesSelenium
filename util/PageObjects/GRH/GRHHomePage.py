import sys
sys.path.append('..')
sys.path.append('...')
from HomePage import *
from GRHLoginPage import *
from GRHServidorPage import *
import utilidades

class GRHHomePage(HomePage):
	def __init__(self,browser, nomeScript):
		super(GRHHomePage,self).__init__(browser,nomeScript)

	def sair_do_sistema(self):
		super(GRHHomePage,self).sair_do_sistema()
		return GRHLoginPage(self.browser)

	def acessar_pagina_servidor(self,base_url):
		utilidades.tirar_print(self.browser,self.nomeScript,"Acessou pagina inicial e vai para a pagina de servidor")
		utilidades.acessar(self.browser,base_url + "/f/pages/servidor/servidor.xhtml")
		return GRHServidorPage(self.browser)