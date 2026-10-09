from app.models.pessoa import Pessoa

class Bibliotecario(Pessoa):
    LIMITE_EMPRESTIMOS = 10
    PODE_CADASTRAR_LIVRO = True

    def mostrar(self) -> dict:
        dados = super().mostrar()
        dados["perfil"] = "bibliotecario"
        return dados