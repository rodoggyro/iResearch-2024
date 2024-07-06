import pandas as pd
import matplotlib.pyplot as plt
import os

from bs4 import BeautifulSoup

from nltk.tokenize import word_tokenize

os.chdir('ATCO2-ASRdataset-v1_beta\DATA')

infoFiles = [f for f in os.listdir() if f.endswith('.info')]
audioFiles = [f for f in os.listdir() if f.endswith('.wav')]
xmlFiles = [f for f in os.listdir() if f.endswith('.xml')]

total = 0
numText = 0

for i in xmlFiles:
	with open (i, 'r', encoding='utf-8') as file:
		data = file.read()

		Bs_data = BeautifulSoup(data, "xml")
		b_unique = Bs_data.find_all('text')
		for j in b_unique:
			total += len(word_tokenize(j.text))
			numText += 1

print(total/numText)

numFiles     = [0, 0, 0, 0, 0, 0, 0]
airportNames = ['Prague', 'Brno', 'Sion', 'Bern', 'Zurich', 'Stefanik', 'Sydney']
# Prague, Brno, Sion, Bern, Zurich, Stefanik (Bratislava, Slovakia), Sydney

for i in infoFiles:
	with open (i, 'r') as file:
		for line in file:
			if 'Praha Ruzyne' in line:
				numFiles[0] += 1
			elif 'Brno' in line:
				numFiles[1] += 1
			elif 'Sion' in line:
				numFiles[2] += 1
			elif 'Bern' in line:
				numFiles[3] += 1
			elif 'Zurich' in line:
				numFiles[4] += 1
			elif 'Bratislava' in line:
				numFiles[5] += 1
			elif 'Sydney' in line:
				numFiles[6] += 1

labels = ['non_english', 'english']
values = [0, 0]

for i in range(len(xmlFiles)):
	with open (xmlFiles[i], 'r', encoding='utf-8') as file:
		data = file.read()

		Bs_data = BeautifulSoup(data, "xml")
		b_unique = Bs_data.find_all('tags')

		for j in b_unique:
			if j.find('non_english').text == '0':
				values[1] += 1
			else:
				values[0] += 1

# plt.pie(values, labels=labels, autopct='%1.1f%%')
# plt.show()

# print(len(infoFiles))

# print(numFiles)
	
# plt.pie(numFiles, labels=airportNames, autopct='%1.1f%%')
# plt.show()

# min max average word counts