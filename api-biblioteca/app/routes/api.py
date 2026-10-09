from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.controllers.livro_controller import LivroController
from app.controllers.pessoa_controller import PessoaController
from app.controllers.emprestimo_controller import EmprestimoController

router = APIRouter(prefix="/api")

# Instanciando estado da aplicação (Controllers)
livro_ctrl = LivroController()
pessoa_ctrl = PessoaController()
emprestimo_ctrl = EmprestimoController()

# --- SCHEMAS (Pydantic) ---
class EmprestimoRequest(BaseModel):
    id_livro: int
    id_pessoa: int

class LoginRequest(BaseModel):
    email: str

class LivroRequest(BaseModel):
    titulo: str
    ano_publicacao: int
    id_pessoa_logada: int

# --- ROTAS DE LIVROS ---

@router.get("/livros")
def listar_livros():
    return livro_ctrl.listar_livros()

@router.get("/livros/disponiveis")
def listar_livros_disponiveis():
    ids_emprestados = emprestimo_ctrl.obter_ids_livros_emprestados()
    return livro_ctrl.listar_livros_disponiveis(ids_emprestados)

@router.get("/livros/{id}")
def buscar_livro(id: int):
    livro = livro_ctrl.buscar_livro(id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return livro

@router.post("/livros", status_code=201)
def cadastrar_livro(req: LivroRequest):
    pessoa = pessoa_ctrl.buscar_pessoa(req.id_pessoa_logada)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    
    # POLIMORFISMO: Avaliando permissão sem usar "if" verificando a classe
    if not pessoa.get("pode_cadastrar_livro"):
        raise HTTPException(status_code=403, detail="Você não tem permissão para cadastrar livros.")
    
    try:
        return livro_ctrl.cadastrar_livro(req.titulo, req.ano_publicacao)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

# --- ROTAS DE PESSOAS / LOGIN ---

@router.post("/login")
def login(req: LoginRequest):
    pessoa = pessoa_ctrl.login(req.email)
    if not pessoa:
        raise HTTPException(status_code=404, detail="E-mail não encontrado.")
    return pessoa

@router.get("/pessoas/{id}/emprestimos")
def listar_emprestimos_pessoa(id: int):
    pessoa = pessoa_ctrl.buscar_pessoa(id)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada.")
    return emprestimo_ctrl.listar_emprestimos_por_pessoa(id)

# --- ROTAS DE EMPRÉSTIMOS ---

@router.post("/emprestimos", status_code=201)
def registrar_emprestimo(req: EmprestimoRequest):
    livro = livro_ctrl.buscar_livro(req.id_livro)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
        
    pessoa = pessoa_ctrl.buscar_pessoa(req.id_pessoa)
    if not pessoa:
        raise HTTPException(status_code=404, detail="Pessoa não encontrada.")

    try:
        return emprestimo_ctrl.registrar_emprestimo(req.id_livro, req.id_pessoa, pessoa)
    except ValueError as e:
        # Aqui usei para traduzir ValueError baseado no contexto (409 para conflito de estado, 422 para regra de negócio)
        if "CONFLITO" in str(e):
            raise HTTPException(status_code=409, detail=str(e).replace("CONFLITO: ", ""))
        raise HTTPException(status_code=422, detail=str(e))