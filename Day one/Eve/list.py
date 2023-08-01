#lists,tuples,dictionaries,sets


#LISTS
#Type
x="m"
print(type(x))

#ordered but allow duplicates
afternoon=["trev", "peters", "blessers", "trev", "peters"]
print((afternoon))

#length
print(len(afternoon))

#type
print(type(afternoon))


#constuctor
thislist = ["haler", "samir", "mboowa"]
print(thislist)

#HOW TO ACCESS THE VALUES
print(thislist[0])
print(thislist[-1])
print(thislist[-2])

#ACCESSING A RANGE OF VALUES
print(thislist[0:2])
print(thislist[:2])
print(thislist[-2:])

#add list items using append function
thislist.append("germner")
print(thislist)

#add list items using insert function  
thislist.insert(0, "hun")
print(thislist)

#add list items using extend function
thislist.extend(["hun", "germner"])
print(thislist)

#add list items using remove function
thislist.remove("hun")
print(thislist)

#add list items using pop function //mboowa
thislist.pop(2)
print(thislist)



