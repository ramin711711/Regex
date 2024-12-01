import re 
greating = "Hello! How is is your day going?"
re.search("is",greating).group() #1

re.findall("is",greating) #2
len(re.findall("is",greating))

re.split('is',greating) #3

re.sub("is", "life", greating, count = 1) #4


# string = "I love living in the US."
# re.findall("[a-wA-W]",string)