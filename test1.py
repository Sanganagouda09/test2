import pymongo as py

client = py.MongoClient("mongodb+srv://sangu:sangu@cluster0.uehnbqb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"Sangu",
    "email":"sangu@gmail.com",
    "surname":"Luiz"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)