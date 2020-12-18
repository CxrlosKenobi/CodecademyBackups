#Text Preprocessing
##Codecademy Data Scientist path

##Noise removal
import re
text = "<p> This is a paragraph</p>"

result = re.sub(r'<.?p>', '', text)

print(result)
