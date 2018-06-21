import os 

STDLIBLOC = ""


max_files = 100 
count = 0

with open("input2.txt", "a", encoding = "utf-8") as f:
	for path, directories, files in os.walk(STDLIBLOC):
		for file in files:
			count +=1
			if count > max_files:
				break
			elif ".py" in file:
				try:
					with open(os.path.join(path, file), "r") as data_f:
						contents = data_f.read()
					f.write(contents)
					f.write('\n')
				except Exception as e:
					print(str(e))