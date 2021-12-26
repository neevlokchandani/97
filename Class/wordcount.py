intro=input('enter your intoduction :- ')
print(intro)
characterCount = 0
wordCount = 1
for letter in intro:
	characterCount=characterCount+1
	if(letter==" "):
		wordCount=wordCount+1
print(wordCount)
print(characterCount)
