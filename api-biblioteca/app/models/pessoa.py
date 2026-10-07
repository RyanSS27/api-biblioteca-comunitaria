import re

class Pessoa:
    LIMITE_EMPRESTIMOS = 0
    PODE_CADASTRAR_LIVRO = false
    
    def __init__(self, id: int, nome: str, email: str):
        self._id = id
        self._nome = ""
        self._email = ""
        
        
    def alterar_nome(self, nome: str):
        if not isinstance(nome, str) or not nome.strip() or len(nome.strip()) < 3:
            raise ValueError("O nome deve ser um texto válido, não vazio, com pelo menos 3 caracteres.")
        
        self._nome = nome.strip()


    def alterar_email(self, email: str):
        padrao_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        
        if not isinstance(email, str) or not email.strip() or not re.match(padrao_email, email.strip()):
            raise ValueError("O email deve ser um texto não vazio em um formato válido (ex: nome@dominio.com).")
        
        self._email = email.strip()

    def mostrar(self) -> dict:
        return {
            "id": self._id,
            "nome": self._nome,
            "email": self._email,
            "limite_emprestimos": self.LIMITE_EMPRESTIMOS,
            "pode_cadastrar_livro": self.PODE_CADASTRAR_LIVRO
        }

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self._id}, nome='{self._nome}')"