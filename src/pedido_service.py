import boto3
import os
import uuid

# Tabela DynamoDB (nome vem do ambiente, definido no template.yaml)
TABELA = os.getenv("TABELA_PEDIDOS", "pedidos")

# Cliente do DynamoDB
dynamodb = boto3.resource("dynamodb")
tabela = dynamodb.Table(TABELA)

def validar_pedido(dados: dict) -> list:
    """Valida o pedido e retorna a lista de erros (vazia se estiver ok)."""
    erros = []

    if not dados.get("cliente"):
        erros.append("Campo 'cliente' é obrigatório")

    itens = dados.get("itens")
    if not itens or not isinstance(itens, list) or len(itens) == 0:
        erros.append("Campo 'itens' deve ser uma lista não vazia")
    else:
        for item in itens:
            if not item.get("produto"):
                erros.append("Cada item deve ter um 'produto'")
            if item.get("quantidade", 0) <= 0:
                erros.append("Cada item deve ter 'quantidade' maior que zero")
            if item.get("preco", 0) <= 0:
                erros.append("Cada item deve ter 'preco' maior que zero")

    return erros

def calcular_total(itens: list) -> float:
    """Soma o total do pedido (quantidade x preco de cada item)."""
    return round(sum(item["quantidade"] * item["preco"] for item in itens), 2)

def salvar_pedido(dados: dict) -> dict:
    """Gera um id, calcula o total e grava o pedido no DynamoDB."""
    pedido = {
        "id": str(uuid.uuid4()),
        "cliente": dados["cliente"],
        "itens": dados["itens"],
        "total": calcular_total(dados["itens"]),
    }
    tabela.put_item(Item=pedido)
    return pedido