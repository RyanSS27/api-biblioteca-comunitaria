from app.data.emprestimos_mock import EMPRESTIMOS

class Emprestimo:
    def __init__(self, id: int, id_livro: int, id_pessoa: int):
        self._id = id
        self._id_livro = 0
        self._id_pessoa = 0
        
        self.alterar_id_livro(id_livro)
        self.alterar_id_pessoa(id_pessoa)

    def alterar_id_livro(self, id_livro: int):
        if not isinstance(id_livro, int) or id_livro <= 0:
            raise ValueError("O ID do livro deve ser um número inteiro positivo.")
        self._id_livro = id_livro

    def alterar_id_pessoa(self, id_pessoa: int):
        if not isinstance(id_pessoa, int) or id_pessoa <= 0:
            raise ValueError("O ID da pessoa deve ser um número inteiro positivo.")
        self._id_pessoa = id_pessoa

    def mostrar(self) -> dict:
        return {
            "id": self._id,
            "id_livro": self._id_livro,
            "id_pessoa": self._id_pessoa
        }

    def __repr__(self) -> str:
        return f"Emprestimo(id={self._id}, id_livro={self._id_livro}, id_pessoa={self._id_pessoa})"


def carregar_emprestimos() -> list[Emprestimo]:
    return [Emprestimo(id=e["id"], id_livro=e["id_livro"], id_pessoa=e["id_pessoa"]) for e in EMPRESTIMOS]