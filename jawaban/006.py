import random, string

class Str:
    @staticmethod
    def lower(arg):
        print(arg.lower())

    @staticmethod
    def upper(arg):
        print(arg.upper())

    @staticmethod
    def capitalize(arg):
        print(arg.title())

    @staticmethod
    def reverse(arg):
        rev = arg [::-1]
        print(rev)
    
    @staticmethod
    def contains(arg1, arg2):
        text = arg1
        word = arg2
        if (word in text):
            print("true")
        else:
            print("false")

    @staticmethod
    def random(arg = 16): 
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=arg))
        print(x)
    
    @staticmethod
    def count(arg):
        str1 = arg
        total = 0       
        for i in str1:
            total = total + 1
        print(total)

    @staticmethod
    def countWords(arg):
        text = len(arg.split())
        print(str(text))

    @staticmethod
    def trim(arg1, arg2 = 100, arg3 = '...'):
        text = arg1 
        print(text[0:arg2], arg3)

    @staticmethod
    def trimWords(arg1, arg2 = 30, arg3 = '...'):
        text = arg1.split()
        twords = list(text[0:arg2])
        str1 = ' '.join(twords)
        print(str1, arg3)



Str.lower("MAKAN")
Str.upper("malam")
Str.capitalize("saya ingin makan")
Str.reverse("kasur")
Str.contains("saya ingin makan sate", "makan")
Str.random(6)
Str.count("lorem ipsum")
Str.countWords("lorem ipsum")

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
Str.trim(text)
Str.trimWords(text, 30)



