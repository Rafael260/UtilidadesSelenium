import sys
sys.path.append('..')
import utilidades
from BasePage import *
from LoginPage import *

class HomePage(BasePage):

	def __init__(self,browser, nomeScript):
		super(HomePage,self).__init__(browser,nomeScript)

	def sair_do_sistema(self):
		utilidades.sair(self.browser)
		#return LoginPage(self.browser)
		pass
		#As subclasses sabem o tipo especifico de LoginPage para retornar

	def coletar_versao_do_sistema(self):
		return utilidades.get_versao_sistema(self.browser)