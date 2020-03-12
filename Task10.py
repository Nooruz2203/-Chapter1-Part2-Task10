string = 'mystring'
print(type(string))
print('mystring'[3])
print('mystring'[2:])
print('mystring'[0:5])
print('mystring'[0:6])
def even_values_string(string):
	  result = "" 
	  for i in range(len(string)):
	    if i % 2 == 0:
	      result = result + string[i]
	  return result
print(even_values_string('mystring'))
def odd_values_string(string):
	  result = "" 
	  for i in range(len(string)):
	    if i % 2 == 1:
	      result = result + string[i]
	  return result
print(odd_values_string('mystring'))

print(string[::-1])
print(string[8:0:-2])
# print(len(string))
