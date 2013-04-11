from lettuce import *

@before.all
column_0 = [1,2,3,4]
column_1 = []
column_2 = []

@step('I have column (\d+)')
def have_a_column(step, column):
    world.column = int(column)

@step('the column has a disk')
def column_has_a_disk(step):
	assert any(world.column)

def disk_is_smaller(step):
	if wold.column0[-1] < wold.column1[-1]:
		move(column0, column1)
	
def move(column0, column1):
	column1.append(column0.pop())