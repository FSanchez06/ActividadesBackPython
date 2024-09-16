import pymongo
conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["sena"]
instructores = bd["instructores"]
instructores.insert_one({"nombre": "Marcos Pinto","area": "Carpinteria"})

import pymongo
conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["sena"]
instructores = bd["instructores"]
instructores.delete_one({"nombre": "Marcos Pinto"})