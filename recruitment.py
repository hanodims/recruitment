def main():
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {
	"name" : "",
	"age" : 0,
	"experience" : 0,
	"skills" : []
	}
	for x in skills:
		print("%s-"%(skills.index(x)+1),x)
	print("Welcome to the special recruitment program, please answer the following questions:")
	name1 = input("What's your name? ")
	cv["name"] = name1
	age1 = input("How old are you? ")
	cv["age"] = age1
	exp = input("How many years experience do you have? ")
	cv["experience"] = exp
	skl1=  input("Choose a skill from above by entering its number: ")
	skl1 = skills[int(skl1)-1]
	cv["skills"].append(skl1)
	skl2 = input("Choose another skill from above by entering its number: ")
	skl2 = skills[int(skl2)-1]
	cv["skills"].append(skl2)

	if int(cv["age"])>25 and int(cv["age"])<40 and int(cv["experience"])>5 and skills[5] in (cv["skills"]):
		print("You have been accepted, %s" % cv["name"])
	else: print("You have been rejected, %s" % cv["name"])

if __name__ == '__main__':
	main()