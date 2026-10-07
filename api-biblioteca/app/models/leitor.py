from app.models.pessoa import Pessoa

class Leitor(Pessoa):
    LIMITE_EMPRESTIMOS = 3
    PERMISSAO_CADASTRAR_LIVRO = False

    def mostrar(self) -> dict:
        dados = super().mostrar()
        dados["perfil"] = "leitor" # adiciona um item ao dicionário que é retornado da classe mãe, com "perfil" sendo a chave e "leitor" o valor, como um atributo fantasma que identificasse a diferença 
        return dados