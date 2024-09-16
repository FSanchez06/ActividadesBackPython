import pymongo
conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["sena"]
instructores = bd["instructores"]
resultado = instructores.find({"$or": [{"regional": "Antioquia"}, {"regional": "Cundinamarca"}]}, {"_id": 0, "nombre": 1, "area": 1}).sort("nombre")
for inst in resultado:
  print (inst)