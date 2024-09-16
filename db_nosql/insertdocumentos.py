import pymongo
conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["sena"]
instructores = bd["instructores"]
instructores.insert_one({"nombre": "Alberto Oviedo", "area": "Contenido digital", "regional": "Huila"})

conexion = pymongo.MongoClient("mongodb://localhost:27017")
bd = conexion["sena"]
instructores = bd["instructores"]
nuevos = [
           {"nombre": "Edwin Perez", "area": "Contenido digital", "regional": "Cundinamarca"},
           {"nombre": "Evelio Chaparro", "area": "Desarrollo de Software", "regional": "Cundinamarca"},
           {"nombre": "Edgar Cruz", "area": "Desarrollo de Software", "regional": "Cundinamarca"},
           {"nombre": "Juan de Jesus Lizcano", "area": "Desarrollo de Software", "regional": "Santander"},
           {"nombre": "Edison Durango", "area": "Electrónica", "regional": "Valle"},
           {"nombre": "Emiro de Jesus Gamez", "area": "Desarrollo de Software", "regional": "Guajira"},
           {"nombre": "Mauricio Paez", "area": "Desarrollo de Software", "regional": "Cesar"},
           {"nombre": "Martha Rodriguez", "area": "Instrumentación", "regional": "Antioquia"},
           {"nombre": "Renato Caballero", "area": "Desarrollo de Software", "regional": "Antioquia"},
           {"nombre": "Adriana Arce", "area": "Desarrollo de Software", "regional": "Risaralda"},
           {"nombre": "Alfonso Abello", "area": "Infraestructura", "regional": "Cesar"},
           {"nombre": "Lorena Fierro", "area": "Desarrollo de Software", "regional": "Caquetá"}
         ]
instructores.insert_many(nuevos)