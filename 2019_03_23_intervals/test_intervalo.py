from intervalos import intervalo

def test_isolado_no_fim():
	_input = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150]	
	assert intervalo(_input) == [[100,105], [110,111], [113,115], [150]]

def test_sem_isolado():
	_input = [100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115]	
	assert intervalo(_input) == [[100,105], [110,111], [113,115]]

def test_isolado_no_meio():
	_input = [100, 101, 102, 103, 104, 105, 110, 113, 114, 115]	
	assert intervalo(_input) == [[100,105], [110], [113,115]]

def test_isolado_no_comeco():
	_input = [9, 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115]	
	assert intervalo(_input) == [[9], [100,105], [110, 111], [113,115]]


def test_forever_alones():
	_input = [1, 3, 5, 7]
	assert intervalo(_input) == [[1], [3], [5], [7]]
