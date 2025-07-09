from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hola, mundo "}


@app.get("/saludo/{nombre}")
def saludar(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}
