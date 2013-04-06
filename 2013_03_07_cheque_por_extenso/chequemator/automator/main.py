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

    VALORES_11_19={
        11:'onze',
        12:'doze',
        13:'treze',
        14:'quatorze',
        15:'quinze',
        16:'dezesseis',
        17:'dezessete',
        18:'dezoito',
        19:'dezenove'
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

    def parse(valor):
        valor_string = str(valor)
        
        if len(valor) > 1:
            s_p = valor[:1]
            s_m = valor
        
        return valor

    def translate(self, valor):
        prase(valor)
        result = ''

        if int(s_p) in Automator.VALORES_CENTENA:
            result += Automator.VALORES_CENTENA[int(s_p)]
            result += ' e '

        if int(s_m) in Automator.VALORES_DEZENA:
            result += Automator.VALORES_DEZENA[int(s_m)]
            result += ' e '

        if int(s_m) in Automator.VALORES_DEZENA:
            result += Automator.VALORES_DEZENA[int(s_m)]
            result += ' e '

        if int(s_u) in Automator.VALORES:
            result += Automator.VALORES[int(s_u)]

        return result