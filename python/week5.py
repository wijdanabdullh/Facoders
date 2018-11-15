s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
name=input("enter student's name: ")
if name ==st1[0]:
    name=st1[0]
    result=sum(st1[1:])
elif name==st2[0]:
    name=st2[0]
    result=sum(st2[1:])
elif name==st3[0]:
    name=st3[0]
    result=sum(st3[1:])
else:
    name='student is not recording'
    result=0
print(name,result)
