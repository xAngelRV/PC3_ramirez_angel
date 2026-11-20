from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


@app.get("/sumar")
def sumar(a: int, b: int):
    return {"resultado": a + b}


class Numeros(BaseModel):
    valores: List[float]


@app.post("/promedio")
def promedio(datos: Numeros):
    if not datos.valores:
        raise HTTPException(status_code=400, detail="Lista vacía")
    return {"promedio": sum(datos.valores) / len(datos.valores)}


@app.get("/health")
def health():
    return {"status": "ok"}
