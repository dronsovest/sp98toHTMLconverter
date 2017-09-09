import header
import players

information = input("Введите названите турнира, номер тура или другую информацию для отображения в загаловке таблицы: ")

htmlData = "<table width=" + "450" + "><caption>" + information + "</caption>"
oldFile = open("Data.txt", encoding="cp1251")


for line in oldFile:
	htmlData = htmlData + "<tr><td>" 
	for item in line:
		if item == "|":
			htmlData = htmlData + "</td><td>" 
		elif item == "\n":
			continue
		else:
			htmlData = htmlData + item
	htmlData = htmlData + "</td></tr>"

htmlData = htmlData + "</table>"
for key in players.players:
	htmlData = htmlData.replace(key, players.players[key])
for key in header.headers:
	htmlData = htmlData.replace(key, header.headers[key])
f = open('result.txt', 'w')
f.write(htmlData);
f.close()
