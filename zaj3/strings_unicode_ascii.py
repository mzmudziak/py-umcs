# coding=utf-8

# text has to be encoded

text = u'Some text in Unicode ężćźół'
textStr = text.encode('utf8')
textUnicode = textStr.decode('utf8')

# encoded in utf8 will be different size
print(text, textStr, textUnicode)
print(len(text), len(textStr), len(textUnicode))

# basestring - check if something is a string
# all strings inherit basestring, so u can use 'isinstance'
text = "some text"
number = 5
print(isinstance(text, basestring))
print(isinstance(number, basestring))

# strip and center, string methods
text = u'     TEST   '

print(text.strip())
print(text.strip().center(30))

# this will print 'test' because the text is prepended by whitespace
print(text.capitalize())

# this will print 'Test' capitalizing the first letter
print(text.strip().capitalize())

# check if one string is in other string
text = u'    TEST    test   '
print('has test?', 'test' in text)








