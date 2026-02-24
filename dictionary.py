info = {
    "name" : "harsh" ,
    "sirname" : "dudharejiya",
    "cgpa" : "9.7",
    "subject" : ["python","java","js","c",],
    "topic" : ("list","tupple")
    }
print(info)
info["name"] = "chutki"
info["villge"] = "lunghiya"
print(info)


# nested dictionary



student = {
    "name" : "harsh",
    "score" :{
       "phy" : 85,
       "chem" : 63,
       "math" : 80
    }
    
}
print(student)
print(student["score"]["chem"])
print(student.keys())
print(student.values())

print(list(student.keys()))
student.update({"city" : "delhi"})
print(student)