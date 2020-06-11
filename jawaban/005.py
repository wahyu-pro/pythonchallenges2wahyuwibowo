# Python3 code to find frequency of each word 
# function for calculating the frequency 
def freq(str): 

	# break the string into list of words 
	str_list = str.split() 

	# gives set of unique words 
	unique_words = set(str_list) 
	strlist = list(unique_words)

	word = ["aku", "ingin", "dapat"]
	for words in strlist : 
		if words in word:
			print( words , str_list.count(words)) 
		else:
			pass

# driver code 
if __name__ == "__main__": 
	
	str ="""
		Aku ingin begini
		Aku ingin begitu
		Ingin ini itu banyak sekali

		Semua semua semua
		Dapat dikabulkan
		Dapat dikabulkan
		Dengan kantong ajaib

		Aku ingin terbang bebas
		Di angkasa
		Hei… baling baling bambu

		La... la... la...
		Aku sayang sekali
		Doraemon

		La... la... la...
		Aku sayang sekali
	""".lower()
	
	# calling the freq function 
	freq(str) 



