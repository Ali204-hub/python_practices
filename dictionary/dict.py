# d={"ali":23,"meesam":33,"hasnain":44,"hassan":55}
# # print(s)
# # d.update({"ali":44})
# # print(d)
# d["ali"]=100  #updating
# d["itrat"]=400 #creating
# del d["hasnain"] #deleting

# print(d)

# s={1:"ali",2:"mahi",3:"ali",4:"cato"}
# # for i in s.values():
# #     print(i)
# for i in s:
#     print(i)

# differnce between deep copy and shallow copy so let's understand it
f={1:"ali",2:"mahi",3:"ali",4:"cato"}
# d=f  #this is deep copy concept because when perfom any changes in d it also appears in f dict
d=f.copy() # this is shallow copy which will not appear in the other dict like 'f'
d[1]="muhammad"
print(d)



 