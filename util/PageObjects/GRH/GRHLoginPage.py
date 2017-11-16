import sys
sys.path.append('..')
sys.path.append('...')
from LoginPage import *
from GRHHomePage import *

class GRHLoginPage(LoginPage):
	def __init__(self,browser,nomeScript):
		super(GRHLoginPage,self).__init__(browser,nomeScript)

	def fazer_login(self,usuario,senha):
		#Deve chamar o comportamento padrao de fazer login
		super(GRHLoginPage,self).fazer_login(usuario,senha)
		#o que muda eh apenas o tipo de objeto de retorno no padrao page object
		return GRHHomePage(self.browser)