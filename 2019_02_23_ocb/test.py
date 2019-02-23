from ocb import parse_input, parse_number

INPUT_123456789 = """
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
"""

INPUT_1 = """
   
  |
  |
"""

INPUT_111111111 = """
                           
  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |
"""

INPUT_2 = """
  _
  _|
 |_
"""

def test_input_123456789():
    assert parse_input(INPUT_123456789) == '123456789'

def test_input_1():
    assert parse_number(INPUT_1) == '1'

def test_input_111111111():
    assert parse_input(INPUT_111111111) == '111111111'
