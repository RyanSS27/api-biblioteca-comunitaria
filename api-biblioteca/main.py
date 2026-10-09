from fastapi import FastAPI
from app.routes.api import router

app = FastAPI(title="Biblioteca Comunitária API")

# Registra todas as rotas que criamos
app.include_router(router)