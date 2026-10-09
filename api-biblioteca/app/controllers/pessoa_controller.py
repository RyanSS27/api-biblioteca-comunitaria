from app.models.pessoa import carregar_pessoas

class PessoaController:
    def __init__(self):
        self.pessoas = carregar_pessoas()

    def _para_dicionario(self, pessoa) -> dict:
        return pessoa.mostrar() if pessoa else None

    def buscar_pessoa(self, id_pessoa: int) -> dict | None:
        for pessoa in self.pessoas:
            if pessoa.mostrar()["id"] == id_pessoa:
                return self._para_dicionario(pessoa)
        return None

    def login(self, email: str) -> dict | None:
        for pessoa in self.pessoas:
            if pessoa.mostrar()["email"] == email:
                return self._para_dicionario(pessoa)
        return None