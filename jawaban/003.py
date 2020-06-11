import json
import operator

# baca file json 
fread = open("format.json", "r")
# ubah json menjadi objek
toObject = json.loads(fread.read()) 
# urutkan berdasarkan harga
toObject.sort(key=operator.itemgetter('price'))

print(toObject)


