expression="((A-(B+c))*D)"
result_string=""
stackofoperators=[]
l=len(expression)-1
symbols=['+','-','*','/','%']
i=0
while i<=l:
  if expression[i]=='(' or expression[i] in symbols:
    stackofoperators.append(expression[i])
  elif expression[i]==')' :
      
      if len(stackofoperators) >=1:
          x=stackofoperators.pop()
          stackofoperators.pop()
      if x=='(':
        continue
      else:
        result_string+=x
  else:
    result_string+=expression[i]
  i+=1
print(result_string)