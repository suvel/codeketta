def f(x):
    return {
        "monday": "no",
        "tuesday": "no",
        "wednesday": "no",
        "thursday": "no",
        "friday": "no",
        "saturday":"yes",
        "sunday": "yes"
        
    }.get(x,"not a valid day") 
i=raw_input()
j=f(i.lower())
print(j)
