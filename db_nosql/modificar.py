import pymongo
conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["sena"]
instructores = bd["instructores"]
instructores.update_many({"area": "Contenido digital"}, {"$set": {"area": "Contenidos Digitales"}})