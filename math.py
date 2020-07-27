import time
# Function to find precedence 
# of operators. 
def precedence(op): 
	
	if op == '+' or op == '-': 
		return 1
	if op == '*' or op == '/': 
		return 2
	return 0

# Function to perform arithmetic 
# operations. 
def applyOp(a, b, op): 
	
	if op == '+': return a + b 
	if op == '-': return a - b 
	if op == '*': return a * b 
	if op == '/': return a // b 

# Function that returns value of 
# expression after evaluation. 
def evaluate(tokens): 
	
	# stack to store integer values. 
	values = [] 
	
	# stack to store operators. 
	ops = [] 
	i = 0
	print(tokens)
	time.sleep(1)
	while i < len(tokens): 
		
		# Current token is a whitespace, 
		# skip it. 
		if tokens[i] == ' ': 
			i += 1
			continue
		
		# Current token is an opening 
		# brace, push it to 'ops' 
		elif tokens[i] == '(': 
			ops.append(tokens[i]) 
		
		# Current token is a number, push 
		# it to stack for numbers. 
		elif tokens[i].isdigit(): 
			val = 0
			
			# There may be more than one 
			# digits in the number. 
			while (i < len(tokens) and
				tokens[i].isdigit()): 
			
				val = (val * 10) + int(tokens[i]) 
				i += 1
			
			values.append(val) 
		
		# Closing brace encountered, 
		# solve entire brace. 
		elif tokens[i] == ')': 
			
			while len(ops) != 0 and ops[-1] != '(': 
			
				val2 = values.pop() 
				val1 = values.pop() 
				op = ops.pop() 
				
				values.append(applyOp(val1, val2, op)) 
				
			# pop opening brace. 
			ops.pop() 
			j = len(ops)
			k = len(values)
			
			while (j >= 1):
				if (j == 1):
					if (ops[-j] != "("):
						print(str(values[-2]) + ' ' + ops[-1] + ' ' + str(values[-1]), end=' ')
					else:
						print('(' + str(values[-1]), end=' ')
					
				elif (ops[-j] == '('):
					print('(', end=' ')
				else:
					print(str(values[-k]) + ' ' + ops[-j], end=' ')
					k -= 1
				
				j -= 1
			if (len(ops) == 0):
				print(values[-1], end=' ')
			print(tokens[i+1:])
			time.sleep(1)
		
		# Current token is an operator. 
		else: 
		
			# While top of 'ops' has same or 
			# greater precedence to current 
			# token, which is an operator. 
			# Apply operator on top of 'ops' 
			# to top two elements in values stack. 
			
			while (len(ops) != 0 and
				precedence(ops[-1]) >= precedence(tokens[i])): 
						
				val2 = values.pop() 
				val1 = values.pop() 
				op = ops.pop() 
				
				values.append(applyOp(val1, val2, op)) 
				j = len(ops)
				k = len(values)
				
				while (j >= 1):
					if (j == 1):
						if (ops[-j] != "("):
							print(str(values[-2]) + ' ' + ops[-1] + ' ' + str(values[-1]), end=' ')
						else:
							print('(' + str(values[-1]), end=' ')
					
					elif (ops[-j] == '('):
						print('(', end=' ')
					else:
						print(str(values[-k]) + ' ' + ops[-j], end=' ')
						k -= 1
				
					j -= 1
				if (len(ops) == 0):
					print(values[-1], end=' ')
				print(tokens[i:])
				time.sleep(1)
			# Push current token to 'ops'. 
			ops.append(tokens[i]) 
			
		i += 1
	
	# Entire expression has been parsed 
	# at this point, apply remaining ops 
	# to remaining values. 
	
	while len(ops) != 0: 
		
		val2 = values.pop() 
		val1 = values.pop() 
		op = ops.pop() 
				
		values.append(applyOp(val1, val2, op)) 
		
		if (len(ops) != 0):
			print(str(values[-2]) + ' ' + ops[-1] + ' ' + str(values[-1]), end=' ')
		else:
			print(values[-1], end=' ')
		print(tokens[i:])
		time.sleep(1)
	# Top of 'values' contains result, 
	# return it. 
	return values[-1] 

# Driver Code 
if __name__ == "__main__": 
	
	expr = input("enter the equation...")
	evaluate(expr)

