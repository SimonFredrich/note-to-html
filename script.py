txt_file = open("note.txt", "r")
read_file = txt_file.read()
print(read_file)

line_text = read_file.replace('--- ', '')

print(line_text)

html_file = open("index.html", "w")
html_file.write("<!DOCTYPE html>")
html_file.write("<html>")
html_file.write("<body>")

html_file.write("<h1>"+line_text+"</h1>")

html_file.write("</body>")
html_file.write("</html>")

