import json

aprendices = [
              {"nombre": "Juan",
               "grupo": "25091",
               "competencias": {"etica": "A","Ingles":"A"}
              },
              {"nombre": "Pedro",
               "grupo": "25093",
               "competencias": {"etica": "A","Ingles":"D"}
              },
              {"nombre": "Lina",
               "grupo": "25091",
               "competencias": {"etica": "D","Ingles":"A"}
              }
             ]

with open("aprendices.json","w") as archivo_json:
    json.dump(aprendices,archivo_json, indent=4)