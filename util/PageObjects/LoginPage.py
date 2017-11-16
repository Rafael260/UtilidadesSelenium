import sys
sys.path.append('..')
sys.path.append('...')
import utilidades
from BasePage import *
from HomePage import *

class LoginPage(BasePage):

	def __init__(self,browser, nomeScript):
		super(LoginPage,self).__init__(browser,nomeScript)

	def fazer_login(self,usuario,senha):
		utilidades.logar(self.browser,self.nomeScript,usuario,senha)
		pass
		#nos login pages especificos, chamará essa função e retornará o HomePage do sistema especifico
