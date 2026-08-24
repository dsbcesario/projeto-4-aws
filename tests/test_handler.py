import json
import boto3
import pytest
from moto import mock_aws

# Configura o DynamoDB mockado (moto) e cria a tabela antes dos testes
@pytest.fixture
def tabela_mock():
    with mock_aws():
        # Cria a tabela mockada igual à do template.yaml
        dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
        dynamodb.create_table(
            TableName="pedidos",
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
            BillingMode="PAY_PER_REQUEST",
        )

        # Importa o handler DENTRO do contexto mock (para pegar o boto3 mockado)
        from src.handler import handler
        yield handler

def test_handler_pedido_valido(tabela_mock):
    """Envia um pedido válido e espera 201 com o total calculado."""
    corpo = json.dumps({
        "cliente": "Maria",
        "itens": [{"produto": "Notebook", "quantidade": 1, "preco": 3500.0}],
    })
    evento = {"body": corpo}
    resposta = tabela_mock(evento, None)

    assert resposta["statusCode"] == 201
    dados = json.loads(resposta["body"])
    assert dados["cliente"] == "Maria"
    assert dados["total"] == 3500.0
    assert "id" in dados

def test_handler_pedido_invalido(tabela_mock):
    """Envia um pedido sem cliente e espera 400 com a lista de erros."""
    corpo = json.dumps({"itens": [{"produto": "X", "quantidade": 1, "preco": 10.0}]})
    evento = {"body": corpo}
    resposta = tabela_mock(evento, None)

    assert resposta["statusCode"] == 400
    dados = json.loads(resposta["body"])
    assert "erros" in dados

def test_handler_json_invalido(tabela_mock):
    """Envia um corpo que não é JSON e espera 400."""
    evento = {"body": "isso nao eh json"}
    resposta = tabela_mock(evento, None)

    assert resposta["statusCode"] == 400