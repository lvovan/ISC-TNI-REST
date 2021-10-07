from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Personne(BaseModel):
    nom: str
    age: int

app = FastAPI()

personnes = []

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/personnes")
async def all():
    return personnes

@app.get("/personnes/{nom}")
async def get_personne(nom):
    for p in personnes:
        if p.nom == nom:
            return p
    
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/personnes")
async def create_personne(p: Personne):
    wasFound = False
    for x in personnes:
        if x.nom == p.nom:
            wasFound = True

    if wasFound == False:
        personnes.append(p)
    return f"La liste a maintenant {len(personnes)} objet(s) de type Personne"

## Ajoutez l'opération Delete
