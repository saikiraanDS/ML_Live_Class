
import pymongo

client = pymongo.MongoClient("mongodb+srv://saikiraan:<pw1212hz2>@cluster0.oaois.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"saikiraan",
    "email" : "saikiraan@ineuron.ai",
    "surname" : "kiraan"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )




