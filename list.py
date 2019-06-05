# movies I saw in 2018
movie_count = [3,5,10,7,4]

print("======================")
#print("movie_count[2] > 4", movie_count[2] > 4)
#print("movie_count[2]", movie_count[2])

for i in range(0,len(movie_count)):
	if movie_count[i] > 4:
		print("You watched a lot of movies!")
	else:
		print("You watched few movies...")