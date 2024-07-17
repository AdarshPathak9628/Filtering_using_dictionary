det={"e1":{"eid":101,"name":"aman","sal":45000,"desing":"manager","address":"delhi"},
    "e2":{"eid":102,"name":"adarsh","sal":55000,"desing":"programmer","address":"lucknow"},
    "e3":{"eid":103,"name":"pathak","sal":65000,"desing":"tester","address":"prayagraj"},
    "e4":{"eid":104,"name":"singh","sal":30000,"desing":"programmer","address":"noida"},
    "e5":{"eid":105,"name":"pandit","sal":60000,"desing":"programmer","address":"lucknow"}}

# using index 

for i in det:
    if(det[i]["address"]=="lucknow"):
        print(det[i]["name"])

# using value function

for key, value in det.items():
    if value["address"] == "lucknow":
        print(value["name"])
