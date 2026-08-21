import json
from src.handler import handler

def test_handler_pedido_valido():
    """Envia um pedido válido e espera 201 com o total calculado."""
    corpo = json.dumps({
        "cliente": "Maria",
        "itens": [{"produto": "Notebook", "quantidade": 1, "preco": 3500.0}],
    })
    evento = {"body": corpo}
    resposta = handler(evento, None)

    assert resposta["statusCode"] == 201
    dados = json.loads(resposta["body"])
    assert dados["cliente"] == "Maria"
    assert dados["total"] == 3500.0
    assert "id" in dados

def test_handler_pedido_invalido():
    """Envia um pedido sem cliente e espera 400 com a lista de erros."""
    corpo = json.dumps({"itens": [{"produto": "X", "quantidade": 1, "preco": 10.0}]})
    evento = {"body": corpo}
    resposta = handler(evento, None)

    assert resposta["statusCode"] == 400
    dados = json.loads(resposta["body"])
    assert "erros" in dados

def test_handler_json_invalido():
    """Envia um corpo que não é JSON e espera 400."""
    evento = {"body": "isso nao eh json"}
    resposta = handler(evento, None)

    assert resposta["statusCode"] == 400