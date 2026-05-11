# Variáveis
PYTHON = poetry run python
APP_MODULE = src.main:app

.PHONY: install install-prod sync-prod shell migration upgrade run clean-env

# Instalar todas as dependências (incluindo dev)
install:
	poetry install

# Instalar apenas dependências de produção (para deploy)
install-prod:
	poetry install --without dev

# Sincronizar ambiente (remove o que não for de produção)
sync-prod:
	poetry install --sync --without dev

# Abrir o shell do ambiente virtual
shell:
	poetry shell

# Criar uma nova migração automática
# Uso: make migration msg="descrição da mudança"
migration:
	poetry run alembic revision --autogenerate -m "$(msg)"

# Aplicar migrações ao banco de dados
upgrade:
	poetry run alembic -c alembic.ini upgrade head

# Rodar o servidor FastAPI
run:
	poetry run uvicorn $(APP_MODULE) --reload

# Obliterar o ambiente virtual
clean-env:
	poetry env remove --all
