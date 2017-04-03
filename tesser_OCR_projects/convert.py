from PIL import Image
from pytesser import *
from sys import argv
script, input_file = argv
 
image_file = input_file
im = Image.open(input_file)
text = image_to_string(im)
text = image_file_to_string(image_file)
text = image_file_to_string(image_file, graceful_errors=True)
# using array-------------
#get = text.split()
#new = []
#new = get
#----------------------------------
print "=====output=======\n"

#------------------using find() -----------

i = text.find(':')+2
d = text.find('Name')-1
print text[i:d]
n = text.find(':',i)+2
m = text.find('Date')-1
print text[n:m]
d = text.find(':',n)+2
b = text.find('Cauntw')-1
print text[d:b]
c = text.find(':',d)+2
t = text.find('Email')-1
print text[c:t]
e = text.find(':',c)+2
x = text.find('Mobile')-1
print text[e:x]
z = text.find(':',e)+2
y = len(text)
print text [z:y]

#=========================================


