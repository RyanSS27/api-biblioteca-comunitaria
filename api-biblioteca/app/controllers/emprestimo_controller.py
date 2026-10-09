from app.models.emprestimo import Emprestimo, carregar_emprestimos

class EmprestimoController:
    def __init__(self):
        self.emprestimos = carregar_emprestimos()

    def _para_dicionario(self, emprestimo: Emprestimo) -> dict:
        return emprestimo.mostrar() if emprestimo else None

    def listar_emprestimos_por_pessoa(self, id_pessoa: int) -> list[dict]:
        encontrados = [e for e in self.emprestimos if e.mostrar()["id_pessoa"] == id_pessoa]
        return [self._para_dicionario(e) for e in encontrados]

    def obter_ids_livros_emprestados(self) -> list[int]:
        return [e.mostrar()["id_livro"] for e in self.emprestimos]

    def registrar_emprestimo(self, id_livro: int, id_pessoa: int, pessoa_dados: dict) -> dict:

        if id_livro in self.obter_ids_livros_emprestados():
            raise ValueError("CONFLITO: Este livro já está emprestado no momento.")

        qtd_atual = len(self.listar_emprestimos_por_pessoa(id_pessoa))
        
        if qtd_atual >= pessoa_dados["limite_emprestimos"]:
            raise ValueError(f"Limite de empréstimos ({pessoa_dados['limite_emprestimos']}) atingido para este usuário.")

        novo_id = len(self.emprestimos) + 1
        novo_emprestimo = Emprestimo(novo_id, id_livro, id_pessoa)
        self.emprestimos.append(novo_emprestimo)

        return self._para_dicionario(novo_emprestimo)