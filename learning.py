import pymongo
import hashlib,codecs
from pymongo import MongoClient
client=MongoClient()
print ('this computer has the following mongo databases %s'%client.database_names())
db=client.test
print ('the selected DB has the following connections %s'%db.collection_names())
print ("DON'T USE THIS SCRIPT WITH REAL PASSOWRD")
user=input('enter your user name')
P=input ('enter your password')
hash1=hashlib.sha512(codecs.encode(P,'ascii'))
hash2=(hash1.hexdigest())
db.test.insert({'user':user ,'pass':hash2})
# +++++++++++++the previous section reads user data , hashes them inserts them to object
a=db.test.find({'user':'ahmad'})
for i in  a:
    print (i)
"""
db.test1.find({$or: [{ID : 1},{ username : "ahmad"}]}) #find with `or` condition, can be used with `and`

db.test1.update ({username:'ahmad'},{username:'K'}) #update based on a certain criteria , ({target},{new value})

db.test1.update ({username:'K'},{hash:'a4325234fdb21'}) replace a field with another , usually used by mistake
#bp35



"""
