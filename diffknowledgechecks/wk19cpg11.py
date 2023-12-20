clients = [
   {
       "username": "hldop",
        "age": 25,
        "friends": ["Jack", "Jill", "Jola"]
   },

   {
       "username": "frid02",
        "age": 30,
        "friends": ["John", "Peter", "James"]
   },

   {
       "username": "Gbelk03",
        "age": 36,
        "friends": ["Neyo", "Derek", "Dan"]
   },

]

# print(client["username"], client["age"])

 #print(f"Hello, my name is {client['username']}, and I am {client['age']} years old")

    
counter = 0
while (counter < len(clients)):
    #print(clients[counter])
    client = clients[counter]
    print(client["username"], client["age"], client["friends"])
    counter = counter + 1