class Automator(object):
	
	VALORES={
		1:'um',
		2:'dois',
		3:'tres',
		4:'quatro',
		5:'cinco',
		6:'seis',
		7:'sete',
		8:'oito',
		9:'nove'
		}
		
	VALORES_DEZENA={
		10:'dez',
		20:'vinte',
		30:'trinta',
		40:'quarenta',
		50:'cinquenta',
		60:'sessenta',
		70:'setenta',
		80:'oitenta',
		90:'noventa'
		}
		
	VALORES_CENTENA={
		100:'cem',
		200:'duzentos',
		300:'trezentos',
		400:'quatrocentos',
		500:'quinhentos',
		600:'seiscentos',
		700:'setecentos', 
		800:'oitocentos',
		900:'novecentos'
		} 
	
	def __init__(self):
		self.valor = 0
		
	def translate(self, valor):
		if valor in Automator.VALORES:
			return Automator.VALORES[valor]
		
		