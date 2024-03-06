str1="hello"
str2="world"
print(str1*3)
print(str1+str2)
print(str1[4])
print(str1[4:2])
print(str1[2:4])
print(str1[2:len(str1)])

print('w' in str1)
print('wo' not in str2)
print(r"hello \n world")
print("the str 1: %s"%(str1))
#value error 
#atribute error 
a="hello world hi"
b=a.replace('h','H')
print(b)
str1="python 123 is a programming language"
l=len(str1)
iv1=str1.find("python")
iv2=str1.find("p",-32)
iv3=str1.find("java")
iv4=str1.find("i",8,25)
print(iv1,iv2,iv3,iv4)
print(l)

idv1=str1.index("python")
idv2=str1.index("a")
idv3=str1.index("l")
#idv4=str1.index("java") value error
str2="python123"
str3="python"
print(idv1)
print(str2.isalnum())
print(str3.isalpha())