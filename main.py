from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Personne(BaseModel):
    nom: str
    age: int

app = FastAPI()

personnes = []

@app.get("/personnes")
async def root():
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

@app.delete("/personnes/{nom}")
async def delete_personne(nom):
    personneASupprimer = None
    for p in personnes:
        if p.nom == nom:
            personneASupprimer = p
    
    if personneASupprimer == None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    personnes.remove(personneASupprimer)
    return f"L'objet Personne dont le nom est '{nom}' a été supprimée de la liste"
