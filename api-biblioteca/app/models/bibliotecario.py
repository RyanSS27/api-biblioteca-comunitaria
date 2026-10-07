from app.models.pessoa import Pessoa

class Bibliotecario(Pessoa):
    LIMITE_EMPRESTIMOS = 10
    PERMISSAO_CADASTRAR_LIVRO = True

    def mostrar(self) -> dict:
        dados = super().mostrar()
        dados["perfil"] = "bibliotecario" # adiciona um item ao dicionário que é retornado da classe mãe, com "perfil" sendo a chave e "bibliotecario" o valor, como um atributo fantasma que identificasse a diferença 
        return dados