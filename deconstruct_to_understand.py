# This is a worked example on how to go line by line through a file and only print line that contain a specified string
# fhand = open("text.txt")
# for line in fhand:
# 	line = line.rstrip()
# 	if line.find('@utc.ac.za') == -1:
# 		continue
# 	print(line)


#  this is the same example de constructed into its elements
fhand = open("text.txt")
print("check what open('text.txt') returned: ", fhand)
for line in fhand:
	print("*********************************************************************************************************")
	print('a new loop itteration begins')
	print("*********************************************************************************************************")
	print('check how the text looks like before rstrip(): '+ line)
	line = line.rstrip()
	print('check how the text looks like after rstrip(): '+ line)

	print("check what line.find('@utc.ac.za') returnes: ", line.find('@utc.ac.za'))
	print("check what line.find('@utc.ac.za') == -1 returnes: ", line.find('@utc.ac.za') ==-1)
	if line.find('@utc.ac.za') == -1: # try replacing line.find('@utc.ac.za') with True or False and see what gets executed using the print statments below
		print("line.find('@utc.ac.za') == -1, continue will be executed next")
		continue
	print("line.find('@utc.ac.za != -1, continue was not executed the rest of the loop will")
	print(line)
	print("the itteration was fully exevuted (no continue)\n")