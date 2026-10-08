from app.models.livro import Livro, carregar_livros

class LivroController:
    def __init__(self):
        self.livros = carregar_livros()

    def _para_dicionario(self, livro: Livro) -> dict:
        return livro.mostrar() if livro else None

    def listar_livros(self) -> list[dict]:
        return [self._para_dicionario(l) for l in self.livros]

    def buscar_livro(self, id_livro: int) -> dict | None:
        for livro in self.livros:
            if livro.mostrar()["id"] == id_livro:
                return self._para_dicionario(livro)
        return None

    def listar_livros_disponiveis(self, ids_emprestados: list[int]) -> list[dict]:
        disponiveis = [l for l in self.livros if l.mostrar()["id"] not in ids_emprestados]
        return [self._para_dicionario(l) for l in disponiveis]
    
    def cadastrar_livro(self, titulo: str, ano_publicacao: int) -> dict:
        novo_id = len(self.livros) + 1
        novo_livro = Livro(novo_id, titulo, ano_publicacao)
        self.livros.append(novo_livro)
        return self._para_dicionario(novo_livro)