import json
from pedido_service import validar_pedido, salvar_pedido

def handler(event, context):
    """Função Lambda principal: processa o pedido e devolve a resposta HTTP."""
    try:
        # Lê o corpo da requisição (API Gateway envia como string JSON)
        corpo = json.loads(event.get("body", "{}"))
    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "body": json.dumps({"erro": "JSON inválido no corpo da requisição"}),
        }

    # Valida o pedido
    erros = validar_pedido(corpo)
    if erros:
        return {
            "statusCode": 400,
            "body": json.dumps({"erros": erros}),
        }

    # Salva o pedido no DynamoDB
    pedido = salvar_pedido(corpo)

    return {
        "statusCode": 201,
        "body": json.dumps(pedido),
    }