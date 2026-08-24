# src/handler.py
import json
from decimal import Decimal
from pedido_service import validar_pedido, salvar_pedido

class DecimalEncoder(json.JSONEncoder):
    """Converte Decimal (usado pelo DynamoDB) em float para o JSON."""
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

def handler(event, context):
    """Função Lambda principal: processa o pedido e devolve a resposta HTTP."""
    try:
        corpo = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"erro": "JSON inválido no corpo da requisição"}),
        }

    erros = validar_pedido(corpo)
    if erros:
        return {
            "statusCode": 400,
            "body": json.dumps({"erros": erros}),
        }

    pedido = salvar_pedido(corpo)

    return {
        "statusCode": 201,
        "body": json.dumps(pedido, cls=DecimalEncoder),
    }