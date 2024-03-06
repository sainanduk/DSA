try:
    with open('/Users/sainandu/Downloads/vishwak.txt','r') as file:
        content=file.read()
        print("inside file")
        for i in content:
            print(i,end=" ")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print("an error occured ",e)