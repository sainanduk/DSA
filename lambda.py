x="HaPPYcoDE"
for i,a in enumerate(x):
    if a.isupper():
        print(i)
print((lambda x:[i for i,a in enumerate(x) if a.isupper()])(x))
