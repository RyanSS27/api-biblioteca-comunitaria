# Prova em grupo — Sistema Backend

**Disciplina:** Programação Orientada a Objetos  
**Formato:** Entrega em grupo, tema sorteado  
**Grupos:** 3 a 4 pessoas  
**Prazo:** 7 dias corridos a partir do sorteio  
**Repositório modelo:** `kioferta-api` (use como referência de estrutura)  

---

## 1. O que é esta prova

Cada grupo recebe, por sorteio, o tema de um sistema. O trabalho é construir o backend desse sistema do zero, seguindo a mesma arquitetura em quatro camadas do repositório modelo.

O escopo é propositalmente menor que o KiOferta: três a quatro classes, uma hierarquia de herança, e de cinco a sete rotas. Dá para fazer em uma semana sem virar noite.

O que está sendo avaliado não é o tamanho do sistema. É se você consegue:
- Decidir quais classes existem no domínio que recebeu
- Proteger o estado delas e colocar a regra no lugar certo
- Usar herança onde ela se justifica, e polimorfismo para evitar `if`
- Separar `data`, `models`, `controllers` e `routes` sem vazamento
- Traduzir erro de negócio em resposta HTTP

### Por que um tema diferente por grupo
Porque o domínio muda, mas a estrutura não. Quando você vir que a sua clínica veterinária e a locadora do grupo vizinho têm exatamente o mesmo esqueleto, o padrão deixa de ser uma receita decorada e vira uma ferramenta.

---

## 2. Tema sorteado

Todos seguem a mesma forma: uma entidade principal, uma hierarquia, um registro que liga as duas.

### Tema 1 - Biblioteca comunitária
Controle de acervo e empréstimos de um ponto de leitura de bairro.

| Camada | O que criar |
| :--- | :--- |
| **Entidades** | `Livro`, `Emprestimo` |
| **Hierarquia** | `Pessoa` <br> ↳ `Leitor` <br> ↳ `Bibliotecario` |
| **Liga as duas** | `Emprestimo` guarda um `Livro` e uma `Pessoa` |

#### Regras obrigatórias
- Leitor pode ter no máximo 3 empréstimos; bibliotecário, 10 (constante de classe)
- Não é possível emprestar um livro já emprestado
- O ano de publicação não pode ser maior que o ano atual
- Só quem tem a permissão `cadastrar_livro` pode incluir um título novo

#### Rotas mínimas
- `GET /api/livros` — lista o acervo
- `GET /api/livros/{id}` — um livro, ou 404
- `GET /api/livros/disponiveis` — só os que não estão emprestados
- `POST /api/emprestimos` — registra, 201 ou 409
- `GET /api/pessoas/{id}/emprestimos` — o que a pessoa está com
- `POST /api/login` — perfil e permissões

---

## 3. O que todo grupo precisa entregar

Independentemente do tema sorteado.

### Estrutura de pastas
```
nome-do-sistema/
├── main.py
├── requirements.txt
├── verificar.py
├── README.md
└── app/
    ├── __init__.py
    ├── data/          # mocks, um arquivo por entidade
    ├── models/        # classes e regras
    ├── controllers/   # casos de uso
    └── routes/        # endereços e códigos HTTP
```

*Não invente outra organização. Copie a do repositório modelo.*

### Camada data
- [ ] Um arquivo `*_mock.py` por entidade, com lista de dicionários
- [ ] Pelo menos 5 registros por entidade principal
- [ ] Nenhuma classe, nenhum import, nenhuma regra nesses arquivos

### Camada models
- [ ] De 3 a 5 classes, contando a hierarquia
- [ ] Todos os atributos protegidos, com um sublinhado
- [ ] Um `mostrar` para cada leitura necessária
- [ ] `alterar` só onde o valor pode mudar; nenhum `alterar_id`
- [ ] O construtor chama os `alterar_`
- [ ] No mínimo 4 regras de negócio com `raise ValueError`
- [ ] `__repr__` em todas as classes
- [ ] Uma função `carregar_*()` por entidade, no fim do arquivo
- [ ] Nenhum import do FastAPI

### Herança e polimorfismo
- [ ] Uma hierarquia com no mínimo 3 classes e 2 níveis
- [ ] Pelo menos um método sobrescrito que usa `super()` para estender
- [ ] Pelo menos uma constante de classe com valor diferente nas filhas
- [ ] Um dicionário no estilo `PERFIS`, mapeando texto do mock para classe
- [ ] Nenhum `if` comparando tipo ou nome de classe em todo o projeto

### Camada controllers
- [ ] Um controller por entidade principal
- [ ] Um método por caso de uso
- [ ] `_para_dicionario` convertendo o objeto
- [ ] Pelo menos um filtro com compreensão de lista
- [ ] Devolve `None` ou lista vazia quando não encontra; nunca código HTTP

### Camada routes
- [ ] De 5 a 7 rotas, conforme o tema
- [ ] 404 quando não encontra
- [ ] 409 quando conflita com o estado atual
- [ ] 422 quando a regra de negócio é violada
- [ ] 201 na criação
- [ ] `try/except` traduzindo o `ValueError` da model

### Verificação
- [ ] Um `verificar.py` com no mínimo 12 checagens, no formato do modelo
- [ ] Ele precisa passar inteiro antes da entrega

### README
- [ ] Como rodar
- [ ] O diagrama de classes, mesmo que em texto ou foto de desenho à mão
- [ ] A tabela de rotas
- [ ] Quem fez o quê

---

## 4. Diagrama de classes

Entregue um diagrama UML com:
- As 3 a 5 classes, com atributos e métodos
- Os sinais `-` para protegido e `+` para público
- O triângulo vazio da herança
- A linha da associação, com as multiplicidades

*Pode ser feito no Draw.io, no Mermaid dentro do README, ou à mão e fotografado. O que vale é estar correto, não bonito.*

---

## 5. Prazo e entrega

| Etapa | Quando |
| :--- | :--- |
| **Sorteio dos temas** | em aula |
| **Dúvidas por issue no repositório da turma** | até o 5º dia |
| **Entrega** | 7º dia, às 23h59 |
| **Apresentação e arguição** | aula seguinte |

### Como entregar
1. Um repositório público por grupo, no GitHub
2. Commits de todos os integrantes ao longo da semana, e não um commit único no fim
3. O link na planilha da turma
4. Na raiz: o `README.md` e a saída do `verificar.py` colada nele

---

## 6. Apresentação

8 minutos por grupo, mais 4 de perguntas.

| Tempo | O quê |
| :--- | :--- |
| **1 min** | O domínio: que sistema é esse e para quem serve |
| **2 min** | O diagrama de classes e por que vocês modelaram assim |
| **3 min** | A API rodando ao vivo no `/docs`, incluindo um caso de erro |
| **2 min** | Onde está a herança e onde está o polimorfismo, mostrando o código |

*Todos falam. A arguição é individual: qualquer integrante pode ser chamado a explicar qualquer linha.*

---

## 7. Rubrica (100 pontos)

| Critério | Pontos | O que é avaliado |
| :--- | :---: | :--- |
| **Modelagem do domínio** | 15 | as classes fazem sentido para o tema; a hierarquia se justifica |
| **Encapsulamento** | 20 | protegidos, construtor validando, sem `alterar_id`, regra na model |
| **Herança e polimorfismo** | 20 | `super()` estendendo, constante de classe, zero `if` de tipo |
| **Camadas** | 15 | sem vazamento; a model não conhece o FastAPI |
| **Coleções** | 10 | pelo menos um filtro com compreensão de lista |
| **Rotas e códigos HTTP** | 10 | 404, 409, 422 e 201 nos lugares certos |
| **Diagrama e README** | 5 | diagrama correto, instruções que funcionam |
| **Apresentação e arguição** | 5 | todos falam e sabem explicar o código |

### Penalidades
| Falha | Perda |
| :--- | :--- |
| `import` do FastAPI dentro de `models/` | Metade dos pontos de camadas |
| `if` comparando tipo ou nome de classe | Metade dos pontos de herança |
| Validação escrita na rota em vez da model | Metade dos pontos de encapsulamento |
| `return 'mensagem de erro'` em vez de `raise` | Metade dos pontos de encapsulamento |
| Um único commit, ou commits de uma pessoa só | Metade dos pontos de apresentação |
| A API não sobe | Zero nos pontos de rotas |

---

## 8. Perguntas da arguição

Prepare-se para responder sobre o seu próprio código:
1. Por que vocês escolheram essas classes, e não outras?
2. Onde está a herança? Por que ela se justifica aqui?
3. Mostre um método que usa `super()` e explique o que acontece se tirá-lo.
4. Onde está o polimorfismo? Que `if` ele evitou?
5. Por que essa constante está na classe filha e não num `if` no controller?
6. Se eu criar uma quarta subclasse, quantos arquivos vocês mexeriam?
7. Por que esta regra está na model e não no controller?
8. A model importa alguma coisa do FastAPI? Por que isso importa?
9. Se os mocks virassem banco de dados, quais arquivos mudariam?
10. Qual é o tipo de relacionamento entre essas duas classes, e por quê?

---

## 9. Perguntas frequentes

- **Podemos usar biblioteca externa?** Só FastAPI e Uvicorn. Nada de banco de dados, ORM ou autenticação com token.
- **Podemos usar inteligência artificial?** Podem, e é bom que saibam usar. Mas a arguição é individual: código que o grupo não sabe explicar vale zero, mesmo funcionando.
- **Precisa ter tela?** Não. É backend. A prova de que funciona é o `/docs`.
- **Podemos trocar de tema?** Não. O sorteio é a prova.
- **E se o tema parecer grande demais?** Entregue o mínimo pedido nas rotas. Funcionalidade extra não vale ponto adicional; qualidade de modelagem vale.
- **E se não terminarmos?** Entreguem o que fizeram. Models e controllers prontos sem as rotas valem mais do que nada. Mas abram a issue antes do prazo: quase sempre dá para destravar.

---

## 10. Checklist final

- [ ] A API sobe com `uvicorn main:app --reload`
- [ ] As rotas aparecem no `/docs`
- [ ] Nenhum import de FastAPI dentro de `app/models/`
- [ ] Nenhum `if` comparando tipo ou nome de classe
- [ ] A hierarquia tem 3 classes e 2 níveis
- [ ] Existe um método com `super()` estendendo o da base
- [ ] Existe uma constante de classe com valor diferente nas filhas
- [ ] Existem no mínimo 4 regras com `raise`
- [ ] O construtor chama os métodos `alterar_`
- [ ] Não existe `alterar_id`
- [ ] Existe pelo menos um filtro com compreensão de lista
- [ ] As rotas devolvem 404, 409, 422 e 201
- [ ] O `verificar.py` passa em todas as checagens
- [ ] O diagrama de classes está no README
- [ ] Todos os integrantes têm commits
- [ ] Todos sabem explicar todo o código
