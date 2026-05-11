# Guia de Comandos (Makefile)

Este projeto utiliza um `Makefile` para automatizar tarefas comuns. Aqui está a explicação de cada comando disponível e quando utilizá-los.

---

## Comandos Disponíveis

### 1. `make install`

- **O que faz:** Instala todas as dependências do projeto usando o Poetry.
- **Quando usar:** Na primeira vez que baixar o projeto ou quando novas bibliotecas forem adicionadas ao `pyproject.toml`.

### 2. `make shell`

- **O que faz:** Abre o ambiente virtual no terminal atual.
- **Quando usar:** Quando precisar rodar scripts Python manualmente ou testar comandos no terminal dentro do contexto do projeto.
- **Como sair:** Digite `exit`.

### 3. `make migration msg="descricao"`

- **O que faz:** Gera um novo arquivo de migração (instrução de mudança) no Alembic.
- **Quando usar:** **Sempre e apenas após alterar seus Modelos em `src/models`**.
- **Exemplo:** `make migration msg="cria_tabela_contas"`

### 4. `make upgrade`

- **O que faz:** Aplica as migrações pendentes ao banco de dados (`bank.db`).
- **Quando usar:** Após rodar o `make migration` ou ao atualizar o código do projeto para garantir que o banco de dados esteja sincronizado com o código.

### 5. `make run`

- **O que faz:** Inicia o servidor de desenvolvimento (FastAPI) com recarregamento automático.
- **Quando usar:** Durante o desenvolvimento para testar a API e acessar o Swagger em `http://127.0.0.1:8000/docs`.

### 6. `make clean-env`

- **O que faz:** Remove completamente o ambiente virtual criado pelo Poetry.
- **Quando usar:** Se houver erros no ambiente virtual ou se desejar reinstalar tudo do zero.

### 7. `make install-prod`
- **O que faz:** Instala apenas as dependências necessárias para produção.
- **Quando usar:** No ambiente de deploy ou produção.

### 8. `make sync-prod`
- **O que faz:** Sincroniza o ambiente, removendo dependências de desenvolvimento se estiverem instaladas.
- **Quando usar:** Quando quiser "limpar" o ambiente e deixar apenas o necessário para produção.

---

## Fluxo de Trabalho Recomendado

Sempre que você alterar a estrutura do banco de dados (modelos):

1.  **Altere o código** em `src/models`.
2.  **Gere a migração:** `make migration msg="nome_da_mudanca"`.
3.  **Aplique no banco:** `make upgrade`.
4.  **Inicie o servidor:** `make run`.

---

_Dica: O Makefile utiliza `poetry run` internamente, então você não precisa se preocupar em ativar o ambiente manualmente para rodar esses comandos._
