# dictionary example w/ "key value pairs"
# keys on the left, values on the right
addresses = {
	"Petar":"Richmond",
	"Cherry":"Richmond",
	"Cary":"Silver Spring",
	"Avi":"Gaithersburg"
}

print("================")
#print(addresses)

#for k in addresses.keys():
#	print(k)
#for v in addresses.values():
#	print(v)
for k in addresses.keys():
	print(k,"is in",addresses.get(k),end=".\n")
	#print(k + " is in " + addresses.get(k) + ".")
	
	
	
	
	
	
	
	
	
	