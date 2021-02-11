import csv
test = [
	['Python', 'Guido van Rossum'],
	['Scala', 'Martin Odersky'],
	['PHP', 'Rasmus Lerdorf'],
	['Ruby', 'Yukihiro Matsumoto'],
	['C', 'Dennis Ritchie']
	]
with open('test.csv', 'wt', newline='') as frecord:
	csvrecord = csv.writer(frecord)
	csvrecord.writerows(test)
