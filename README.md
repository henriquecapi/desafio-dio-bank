# Desafio: API Bancária Assíncrona com FastAPI

Este sistema é uma **API Bancária Assíncrona** desenvolvida com **FastAPI**. O objetivo principal é gerenciar operações de contas correntes, permitindo depósitos, saques e consulta de extratos, tudo protegido por autenticação **JWT (JSON Web Token)** e utilizando programação assíncrona para alta performance.

---

## 1. Visão Geral do Sistema
*   **Tecnologias:** Python 3.11+, FastAPI, SQLAlchemy/Databases (Assíncrono), Alembic (Migrações), Pydantic e JWT.
*   **Arquitetura:** Segue um padrão de camadas:
    *   `src/models`: Definições das tabelas do banco de dados.
    *   `src/schemas`: Validação de dados de entrada e saída (Pydantic).
    *   `src/controllers`: Lógica das rotas da API.
    *   `src/services`: Lógica de negócio (ex: validar saldo antes de saque).
    *   `src/security.py`: Gerenciamento de tokens JWT e senhas.

---

## 2. Passo a Passo para Execução

### **Passo 1: Preparar o Ambiente**
O projeto utiliza o **Poetry** para gerenciar dependências.

1.  **Crie o arquivo de configuração de ambiente:**
    Copie o conteúdo de `.env.example` para um novo arquivo chamado `.env`:
    ```bash
    cp .env.example .env
    ```
    *Isso garantirá que o sistema saiba onde criar o banco de dados (por padrão, um arquivo local `bank.db`).*

### **Passo 2: Criar o Ambiente Virtual e Instalar Dependências**
Dentro da pasta raiz do projeto, execute:
```bash
# Instala todas as dependências listadas no pyproject.toml
poetry install

# Ativa o ambiente virtual criado pelo Poetry
poetry shell
```

### **Passo 3: Criação da Base de Dados (Migrações)**
O sistema utiliza o **Alembic** para versionar o banco de dados. Para criar as tabelas pela primeira vez:
```bash
alembic upgrade head
```
*Este comando lerá os modelos em `src/models` e criará o arquivo `bank.db` com todas as tabelas (contas, transações, usuários).*

### **Passo 4: Subir o Servidor**
Com o ambiente ativo e o banco criado, inicie a aplicação com o **Uvicorn**:
```bash
uvicorn src.main:app --reload
```
*   `src.main:app`: Aponta para o objeto `app` dentro de `src/main.py`.
*   `--reload`: Reinicia o servidor automaticamente sempre que você alterar o código.

---

## 3. Acessando a Documentação
Assim que o servidor subir (geralmente em `http://127.0.0.1:8000`), o FastAPI gera automaticamente uma documentação interativa:

*   **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
*   **Redoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 4. Resumo de Comandos Rápidos:
1. `cp .env.example .env`
2. `poetry install`
3. `poetry shell`
4. `alembic upgrade head`
5. `uvicorn src.main:app --reload`