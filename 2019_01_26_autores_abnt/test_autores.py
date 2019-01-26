from autores import formata_nome

def test_formata_1():
    assert formata_nome('Joao Carlos Alves') == 'ALVES, Joao C' 

def test_formata_2():
	assert formata_nome('Paulo Coelho') == 'COELHO, Paulo'

def test_formata_3():
    assert formata_nome('Mateus Oliveira Alves Coelho') == 'COELHO, Mateus O A'

def test_formata_4():
    assert formata_nome('Guimaraes') == 'GUIMARAES'

def test_formata_5():
    assert formata_nome('Joao Silva Neto') == 'SILVA NETO, Joao'

def test_formata_6():
    assert formata_nome('Joao Neto') == 'NETO, Joao'

def test_formata_7():
    assert formata_nome('Celso de Araujo') == 'ARAUJO, Celso de'
