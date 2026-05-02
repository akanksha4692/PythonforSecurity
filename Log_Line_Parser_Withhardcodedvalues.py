log = "2026-04-29 10:22:01 | ALERT | SRC=10.0.0.1 DST=8.8.8.8 USER=admin"

#Split the log at the delimiter
parts=log.split("|")

#Clean the log by trimming the spaces
for p in range(len(parts)):
    parts[p]=parts[p].strip()  

# Can also use append to create a new list and not modify existing list

#Create a dictionary with basic fields

results={}
results["timestamp"]=parts[0]
results["severity"]=parts[1]
#results["source_ip"]=parts[2]: Dont add

#add only key,value pairs to the dictionary that are clean. Dont add the values that need to be split up

details=parts[2].split()
print(details)
['SRC=10.0.0.1', 'DST=8.8.8.8', 'USER=admin']

for i in details:
    (key,value)=i.split("=")
    results[key]=value


#Rename mapping keys
mapping={'SRC':'Source_ip', 'DST':'Destination_ip', 'USER':'USERNAME'}

clean_result={}

for key, value in results.items():
    if key in mapping:
        clean_result[mapping[key]] = value
    else:
        clean_result[key] = value

print(clean_result)







