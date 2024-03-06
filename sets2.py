n=input("enter string").split()
res={words.capitalize() if words[0]=="h" else words for words in n }
print(res)