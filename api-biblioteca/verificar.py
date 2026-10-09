import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:8000/api"

def requisicao(endpoint, method="GET", payload=None):
    url = f"{BASE_URL}{endpoint}"
    data = json.dumps(payload).encode("utf-8") if payload else None
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method=method)
    
    try:
        with urllib.request.urlopen(req) as response:
            status = response.status
            body = json.loads(response.read().decode("utf-8"))
            return status, body
    except urllib.error.HTTPError as e:
        try:
            body = json.loads(e.read().decode("utf-8"))
        except Exception:
            body = {}
        return e.code, body

def executar_testes():
    print("--- INICIANDO VERIFICAÇÃO DA API BIBLIOTECA ---")
    passou = 0
    total = 12

    # 1. GET /api/livros
    status, body = requisicao("/livros")
    if status == 200 and isinstance(body, list) and len(body) >= 5:
        print("✅ Check 01: Listagem de livros OK")
        passou += 1
    else:
        print("❌ Check 01: Falha ao listar livros")

    # 2. GET /api/livros/1
    status, body = requisicao("/livros/1")
    if status == 200 and body.get("id") == 1:
        print("✅ Check 02: Buscar livro existente OK")
        passou += 1
    else:
        print("❌ Check 02: Falha ao buscar livro por ID")

    # 3. GET /api/livros/999 -> 404
    status, _ = requisicao("/livros/999")
    if status == 404:
        print("✅ Check 03: Livro inexistente retornou 404 OK")
        passou += 1
    else:
        print("❌ Check 03: Deveria retornar 404 para livro inexistente")

    # 4. GET /api/livros/disponiveis
    status, body = requisicao("/livros/disponiveis")
    if status == 200 and isinstance(body, list):
        print("✅ Check 04: Filtro de livros disponíveis OK")
        passou += 1
    else:
        print("❌ Check 04: Falha na rota de livros disponíveis")

    # 5. POST /api/login (Leitor)
    status, body = requisicao("/login", method="POST", payload={"email": "jonathan@email.com"})
    if status == 200 and body.get("limite_emprestimos") == 3:
        print("✅ Check 05: Login de Leitor OK (Limite = 3)")
        passou += 1
    else:
        print("❌ Check 05: Falha no login de Leitor")

    # 6. POST /api/login (Bibliotecário)
    status, body = requisicao("/login", method="POST", payload={"email": "giovane@email.com"})
    if status == 200 and body.get("limite_emprestimos") == 10:
        print("✅ Check 06: Login de Bibliotecário OK (Limite = 10)")
        passou += 1
    else:
        print("❌ Check 06: Falha no login de Bibliotecário")

    # 7. POST /api/login (Inexistente -> 404)
    status, _ = requisicao("/login", method="POST", payload={"email": "invalido@email.com"})
    if status == 404:
        print("✅ Check 07: Login inválido retornou 404 OK")
        passou += 1
    else:
        print("❌ Check 07: Deveria retornar 404 para e-mail não cadastrado")

    # 8. GET /api/pessoas/1/emprestimos
    status, body = requisicao("/pessoas/1/emprestimos")
    if status == 200 and isinstance(body, list):
        print("✅ Check 08: Empréstimos da pessoa consultados OK")
        passou += 1
    else:
        print("❌ Check 08: Falha ao buscar empréstimos da pessoa")

    # 9. POST /api/emprestimos (Livro 1 já emprestado -> 409 Conflict)
    status, _ = requisicao("/emprestimos", method="POST", payload={"id_livro": 1, "id_pessoa": 1})
    if status == 409:
        print("✅ Check 09: Conflito de livro já emprestado retornou 409 OK")
        passou += 1
    else:
        print(f"❌ Check 09: Esperado 409, retornou {status}")

    # 10. POST /api/livros (Ano futuro -> 422 Unprocessable Entity)
    status, _ = requisicao("/livros", method="POST", payload={"titulo": "Futuro", "ano_publicacao": 2030, "id_pessoa_logada": 2})
    if status == 422:
        print("✅ Check 10: Validação de ano futuro retornou 422 OK")
        passou += 1
    else:
        print(f"❌ Check 10: Esperado 422, retornou {status}")

    # 11. POST /api/livros (Leitor sem permissão -> 403 Forbidden)
    status, _ = requisicao("/livros", method="POST", payload={"titulo": "Teste", "ano_publicacao": 2020, "id_pessoa_logada": 1})
    if status == 403:
        print("✅ Check 11: Leitor impedido de cadastrar livro retornou 403 OK")
        passou += 1
    else:
        print(f"❌ Check 11: Esperado 403, retornou {status}")

    # 12. POST /api/livros (Bibliotecário -> 201 Created)
    status, body = requisicao("/livros", method="POST", payload={"titulo": "O Hobbit", "ano_publicacao": 1937, "id_pessoa_logada": 2})
    if status == 201 and body.get("titulo") == "O Hobbit":
        print("✅ Check 12: Cadastro de novo livro retornou 201 OK")
        passou += 1
    else:
        print(f"❌ Check 12: Falha ao cadastrar livro como Bibliotecário")

    print(f"\nResultado final: {passou}/{total} testes passaram.")

if __name__ == "__main__":
    executar_testes()