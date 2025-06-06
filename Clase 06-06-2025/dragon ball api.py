personajes = {
  "items": [
    {
      "id": 6,
      "name": "Zarbon",
      "ki": "20.000",
      "maxKi": "30.000",
      "race": "Frieza Race",
      "gender": "Male",
      "description": "Zarbon es uno de los secuaces de Freezer y un luchador poderoso.",
      "image": "https://dragonball-api.com/characters/zarbon.webp",
      "affiliation": "Army of Frieza",
      "deletedAt": None
    },
    {
      "id": 7,
      "name": "Dodoria",
      "ki": "18.000",
      "maxKi": "20.000",
      "race": "Frieza Race",
      "gender": "Male",
      "description": "Dodoria es otro secuaz de Freezer conocido por su brutalidad.",
      "image": "https://dragonball-api.com/characters/dodoria.webp",
      "affiliation": "Army of Frieza",
      "deletedAt": None
    },
    {
      "id": 8,
      "name": "Ginyu",
      "ki": "9.000",
      "maxKi": "25.000",
      "race": "Frieza Race",
      "gender": "Male",
      "description": "Ginyu es el líder del la élite de mercenarios de mayor prestigio del Ejército de Freeza, la cual lleva el nombre de Fuerzas Especiales Ginew en su honor[9].",
      "image": "https://dragonball-api.com/characters/ginyu.webp",
      "affiliation": "Army of Frieza",
      "deletedAt": None
    },
    {
      "id": 9,
      "name": "Celula",
      "ki": "250.000.000",
      "maxKi": "5 Billion",
      "race": "Android",
      "gender": "Male",
      "description": "Cell conocido como Célula en España, es un bioandroide creado por la computadora del Dr. Gero, quien vino del futuro de la línea 3 con la intención de vengarse de Goku por haber acabado con el Ejército del Listón Rojo, y con ello el sueño de todo villano: dominar el mundo. Es el antagonista principal del Arco de los Androides y Cell.",
      "image": "https://dragonball-api.com/characters/celula.webp",
      "affiliation": "Freelancer",
      "deletedAt": None
    },
    {
      "id": 10,
      "name": "Gohan",
      "ki": "45.000.000",
      "maxKi": "40 septillion",
      "race": "Saiyan",
      "gender": "Male",
      "description": "Son Gohanda en su tiempo en España, o simplemente Gohan en Hispanoamérica, es uno de los personajes principales de los arcos argumentales de Dragon Ball Z, Dragon Ball Super y Dragon Ball GT. Es un mestizo entre saiyano y humano terrícola. Es el primer hijo de Son Goku y Chi-Chi, hermano mayor de Son Goten, esposo de Videl y padre de Pan.",
      "image": "https://dragonball-api.com/characters/gohan.webp",
      "affiliation": "Z Fighter",
      "deletedAt": None
    }
  ],
  "meta": {
    "totalItems": 58,
    "itemCount": 5,
    "itemsPerPage": 5,
    "totalPages": 12,
    "currentPage": 2
  },
  "links": {
    "first": "https://dragonball-api.com/api/characters?limit=5",
    "previous": "https://dragonball-api.com/api/characters?page=1&limit=5",
    "next": "https://dragonball-api.com/api/characters?page=3&limit=5",
    "last": "https://dragonball-api.com/api/characters?page=12&limit=5"
  }
}


print(personajes["items"][1]["name"])


for i in personajes["items"]:
    print(i["name"], i["ki"])