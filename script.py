htmlData = "<table width=" + "450" + "><caption>Рукодельный швейцарский классический турнир</caption>"
oldFile = open("Test Trump.txt")


for line in oldFile:
	htmlData = htmlData + "<tr><td>" 
	for item in line:
		if item == "|":
			htmlData = htmlData + "</td><td>" 
		elif item == '\n':
			continue
		else:
			htmlData = htmlData + item
	htmlData = htmlData + "</td></tr>"

htmlData = htmlData + "</table>"
f = open('result.txt', 'w')
f.write(htmlData);
f.close()
