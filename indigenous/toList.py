with open("data/entries.json", "r") as database:
	objects = database.read().split("}\n{\n")
	with open("JSONList.txt", "w") as out:
		joined = "},\n{\n".join(objects)
		print(joined)