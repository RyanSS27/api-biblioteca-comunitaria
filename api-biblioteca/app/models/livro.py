from datetime import datetime
from app.data.livros_mock import LIVROS

class Livro:
    def __init__(self, id: int, titulo: str, ano_publicacao: int):
        self._id = id
        self._titulo = ""
        self._ano_publicacao = 0
        
        self.alterar_titulo(titulo)
        self.alterar_ano_publicacao(ano_publicacao)
        
    
    def alterar_titulo(self, titulo: str):
            if not isinstance(titulo, str) or not titulo.strip():
                raise ValueError("O título do livro não pode estar vazio.")
            self._titulo = titulo.strip()

    def alterar_ano_publicacao(self, ano: int):
        if not isinstance(ano, int):
            raise ValueError("O ano de publicação deve ser um número inteiro.")
            
        ano_atual = datetime.now().year
        if ano > ano_atual:
            raise ValueError(f"O ano de publicação não pode ser maior que o ano atual ({ano_atual}).")
            
        self._ano_publicacao = ano

    def mostrar(self) -> dict:
        return {
            "id": self._id,
            "titulo": self._titulo,
            "ano_publicacao": self._ano_publicacao
        }

    def __repr__(self) -> str:
        return f"Livro(id={self._id}, titulo='{self._titulo}')"


def carregar_livros() -> list[Livro]:
    return [Livro(id=l["id"], titulo=l["titulo"], ano_publicacao=l["ano_publicacao"]) for l in LIVROS]