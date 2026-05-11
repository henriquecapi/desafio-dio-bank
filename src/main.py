from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.controllers import account, auth, transaction
from src.database import database
from src.exceptions import AccountNotFoundError, BusinessError


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


tags_metadata = [
    {
        "name": "auth",
        "description": "Operações de autenticação.",
    },
    {
        "name": "account",
        "description": "Operações para manutenção de contas",
    },
    {
        "name": "transaction",
        "description": "Operações para manutenção de transações.",
    },
]


app = FastAPI(
    title="Transactions API",
    version="1.0.0",
    summary="Microsserviço para gerenciar operações de saque e depósito em contas correntes.",
    description="""
A API de Transações é o microsserviço para registro de transações de conta corrente. 💸💰

## Account

* **Criar contas**.
* **Listar contas**.
* **Liste as transações da conta por ID.**.

## Transaction

* **Create transactions**.
""",
    openapi_tags=tags_metadata,
    redoc_url=None,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["auth"])
app.include_router(account.router, tags=["account"])
app.include_router(transaction.router, tags=["transaction"])


@app.exception_handler(AccountNotFoundError)
async def account_not_found_error_handler(request: Request, exc: AccountNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"detail": "Account not found."}
    )


@app.exception_handler(BusinessError)
async def business_error_handler(request: Request, exc: BusinessError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT, content={"detail": str(exc)}
    )
