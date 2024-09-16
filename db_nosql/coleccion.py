import pymongo
conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["sena"]
instructores = bd["instructores"]
for inst in instructores.find({"regional": "Tolima"}, {"_id": 0, "nombre": 1}):
    print (inst)