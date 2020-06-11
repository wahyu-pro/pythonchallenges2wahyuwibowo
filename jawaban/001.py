# function which return reverse of a string 
def isPalindrome(s): 
	return s == s[::-1] 

s = input("Masukan kalimat palindrome : ")
ans = isPalindrome(s.replace(" ","").lower()) 

if ans: 
	print(s, "adalah kalimat palindrome") 
else: 
	print(s, "bukan kalimat palindrome") 
