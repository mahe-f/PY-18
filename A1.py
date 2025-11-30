#get rid of duplicates

student={
     "id1":{"Name":["Maahekaan"], "Class":9,"Age":15},
     "id2":{"Name":["Wafia"], "Class":9,"Age":15},
     "id3":{"Name":["Hania"], "Class":9,"Age":15},
     "id4":{"Name":["Mishal"], "Class":9,"Age":14},
     "id5":{"Name":["Maahekaan"], "Class":9,"Age":15}
}

result={}
for key, value in student.items():
    if value not in result.values():
        result[key]=value
print(result)
