# 📚 API - Biblioteca Comunitária

Este projeto é o backend de um sistema de Biblioteca Comunitária, desenvolvido como avaliação para a disciplina de Programação Orientada a Objetos. O sistema segue uma arquitetura rígida em 4 camadas (`data`, `models`, `controllers` e `routes`), aplicando conceitos de encapsulamento, herança e polimorfismo.

## 🚀 Como Rodar o Projeto

Para executar a API localmente, siga os passos abaixo:

1. **Clone o repositório** (ou extraia a pasta do projeto):
   ```bash
   cd nome-do-sistema
   ```

2. **Crie e ative um ambiente virtual (recomendado):**
   * No Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   * No Linux/Mac:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Nota: O arquivo requirements.txt deve conter no mínimo `fastapi` e `uvicorn`)*

4. **Inicie o servidor local:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Acesse a documentação interativa (Swagger):**
   * Abra o navegador em: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🏗️ Diagrama de Classes

Abaixo está o diagrama em formato de texto demonstrando as 3 entidades principais, a hierarquia de `Pessoa` e o vínculo feito pelo `Emprestimo`.

```text
  +-----------------------+        +-----------------------+
  |         Livro         |        |      Emprestimo       |
  +-----------------------+        +-----------------------+
  | - _id: int            |<-------| - _id: int            |
  | - _titulo: str        |        | - _id_livro: int      |
  | - _ano_publicacao: int|        | - _id_pessoa: int     |
  +-----------------------+        +-----------------------+
                                               |
                                               v
                                   +-----------------------+
                                   |        Pessoa         |
                                   +-----------------------+
                                   | - _id: int            |
                                   | - _nome: str          |
                                   | - _email: str         |
                                   | - LIMITE_EMPRESTIMOS  |
                                   | - PODE_CADASTRAR_LIVRO|
                                   +-----------------------+
                                            /     \
                                   ________/       \________
                                  /                         \
                   +-----------------------+   +-----------------------+
                   |        Leitor         |   |     Bibliotecario     |
                   +-----------------------+   +-----------------------+
                   | LIMITE_EMP = 3        |   | LIMITE_EMP = 10       |
                   | PODE_CADAS = False    |   | PODE_CADAS = True     |
                   +-----------------------+   +-----------------------+
```

---

## 🌐 Tabela de Rotas

O sistema expõe 7 rotas RESTful para gerenciar o acervo e os empréstimos:

| Método | Rota | Descrição | Retorno de Sucesso | Possíveis Erros |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/api/livros` | Lista todo o acervo de livros da biblioteca. | `200 OK` | - |
| **GET** | `/api/livros/disponiveis` | Lista apenas os livros que não estão emprestados no momento. | `200 OK` | - |
| **GET** | `/api/livros/{id}` | Busca os detalhes de um livro específico pelo seu ID. | `200 OK` | `404 Not Found` |
| **POST** | `/api/livros` | Cadastra um novo livro (requer que a pessoa logada seja Bibliotecário). | `201 Created` | `404 Not Found`, `403 Forbidden`, `422 Unprocessable Entity` |
| **POST** | `/api/login` | Simula o login recebendo um e-mail e retornando os dados e permissões do perfil. | `200 OK` | `404 Not Found` |
| **GET** | `/api/pessoas/{id}/emprestimos`| Lista todos os livros que uma determinada pessoa está no momento. | `200 OK` | `404 Not Found` |
| **POST** | `/api/emprestimos` | Registra um novo empréstimo, validando limites e disponibilidade. | `201 Created` | `404 Not Found`, `409 Conflict`, `422 Unprocessable Entity` |

---

## 👥 Quem fez o quê

* **[Seu Nome / Nome 1]**: Responsável por estruturar as regras de negócio nas `Models`, garantindo o encapsulamento e as validações nos construtores (ex: regra do ano de publicação).
* **[Nome 2]**: Responsável pela implementação do polimorfismo (`Leitor` e `Bibliotecario`) e por criar os arquivos de Mocks (`data`).
* **[Nome 3]**: Desenvolveu a camada `Controllers`, garantindo a ausência de código HTTP, construindo o método genérico de serialização em dicionário e list comprehensions.
* **[Nome 4 / Todos em conjunto]**: Construção da camada `Routes` com FastAPI, traduzindo os erros genéricos (ValueError) para o padrão de status de requisição web (404, 409, 422) e documentação final.