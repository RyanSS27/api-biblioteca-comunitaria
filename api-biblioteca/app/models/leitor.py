from app.models.pessoa import Pessoa

class Leitor(Pessoa):
    LIMITE_EMPRESTIMOS = 3
    PODE_CADASTRAR_LIVRO = False

    def mostrar(self) -> dict:
        dados = super().mostrar()
        dados["perfil"] = "leitor"
        return dados