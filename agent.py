import copy

#enter your current state here....
states  =  ['1','7','2','4',
			'9','5','3','8',
			'13','0','10','12',
			'14','6','11','15']

goal_state=['1','2','3','4',
			'5','6','7','8',
			'9','10','11','12',
			'13','14','15','0']

def check(state):														# Check if the state is a
	return (goal_state == state)										# goal state and returns a boolean value


def h1 (state):
	
	ans = 0
	
	for element in state:
		
		if state.index (element) != goal_state.index (element):
			ans = ans + 1
	
	return ans

def h2 (state):
	
	ans = 0
	
	for element in state:
		
		now = state.index(element)
		goal = goal_state.index(element)
		
		if now != goal:
			
			xshift = abs( now % 4 - goal % 4 )
			yshift = abs( now / 4 - goal / 4 )
			ans = ans + yshift + xshift
	
	return ans

def h (state):
	h11 = h1(state)
	h22 = h2(state)
	
	if h11 > h22:
		return h11
	
	else:
		return h22

def actions(state):														# What are the possible
																		# actions in the state?
	action = []
	blank_pos = state.index ('0')
	
	if (blank_pos>3):
		action += 'u'
	
	if (blank_pos<12):
		action += 'd'
	
	if (blank_pos%4):
		action += 'l'
	
	if ((blank_pos%4)!=3):
		action += 'r'
	
	return action

def result ( state,action):
	
	blank_pos = state.index ('0')
	
	if action == 'u':
		(state[blank_pos],state[blank_pos-4])=(state[blank_pos-4],'0')
	
	if action=='d':
		(state[blank_pos],state[blank_pos+4])=(state[blank_pos+4],'0')
	
	if action=='l':
		(state[blank_pos],state[blank_pos-1])=(state[blank_pos-1],'0')
	
	if action=='r':
		(state[blank_pos],state[blank_pos+1])=(state[blank_pos+1],'0')
	
	return state


def removechoice(frontier):
	lowestcost=-1
	for element in frontier:											# element has cost path state so far
		if element['cost'] == None:
			element['cost'] = len(element['path']) + h(element['state'])#elementh path has length also
		if ((lowestcost < 0) or (element['cost']<lowestcost)):
			lowestcost = element['cost']
			lowestCostElement = element
	frontier.pop(frontier.index(lowestCostElement))
	return lowestCostElement

def solver(initial_state):
	frontier=[]
	explored=[]
	start_node={}
	start_node['state']=initial_state
	start_node['path']=[]
	start_node['cost']=None
	frontier.append(start_node)
	explored.append(start_node['state'])
	while (1):
		next_node = removechoice(frontier)
		if check(next_node['state']):
			return next_node['path']		
		action=actions(next_node['state'])
		for element in action:
			cp_next_node= copy.deepcopy(next_node)
			new_state=result(cp_next_node['state'],element)
			if new_state not in explored:
				new_node={}
				explored.append(new_state)
				new_node['state']=new_state
				new_node['path']=copy.deepcopy(next_node['path'])
				new_node['path'].append(element)
				new_node['cost']=None
				frontier.append(new_node)

print solver(states)
