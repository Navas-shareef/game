import game
import pytest


def test_present_cells():
	list=[['-','-','*'],['*','-','-'],['-','*','-']]
	row=1
	column=1
	neigbours=[]
	assert game.present_cells(list,row,column,neigbours)==['*','-']

def test_upper_cells():
	list=[['-','-','*'],['*','-','-'],['-','*','-']]
	row=1
	column=1
	neigbours=[]
	assert game.upper_cells(list,row,column,neigbours)==['-','-','*']

def test_down_cells():
	list=[['-','*'],['*','-','-'],['-','*','-']]
	row=1
	column=0
	neigbours=[]
	assert game.down_cells(list,row,column,neigbours)==['-','*']

def test_livecell_rule():
	list=[['-','*','-'],['*','-','-'],['-','*','-']]
	row=1
	column=0
	neigbours=['-','-','*','-','*',]
	assert game.livecell_rule(list,row,column,neigbours)==[['-','*','-'],['*','-','-'],['-','*','-']]

# live cell with 1 or greaterthan 3 live neighbourcells
def test_else_livecell_rule():
	list=[['-','*','-'],['*','*','-'],['*','*','-']]
	row=1
	column=0
	neigbours=['*','-','*','*','*',]
	assert game.livecell_rule(list,row,column,neigbours)==[['-','*','-'],['-','*','-'],['*','*','-']]

def test_deadcell_rule():
	list=[['-','*','-'],['*','-','*'],['-','-','-']]
	row=1
	column=1
	neigbours=['*','*','*','-','-','-','-','-']
	assert game.deadcell_rule(list,row,column,neigbours)==[['-','*','-'],['*','*','*'],['-','-','-']]

def test_else_deadcell_rule():
	list=[['-','*','-'],['*','-','-'],['-','-','-']]
	row=1
	column=1
	neigbours=['*','-','*','-','-','-','-','-']
	assert game.deadcell_rule(list,row,column,neigbours)==[['-','*','-'],['*','-','-'],['-','-','-']]
