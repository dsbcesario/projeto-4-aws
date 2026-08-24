# API Serverless de Processamento de Pedidos

Função AWS Lambda exposta via API Gateway que processa pedidos e
armazena os dados no DynamoDB, com deploy automatizado.

## 🎯 Objetivo
Demonstrar o ecossistema AWS: computação serverless, banco gerenciado,
integração de serviços e infraestrutura como código.

## 🛠️ Tecnologias
- AWS Lambda (computação serverless)
- API Gateway (exposição da API)
- DynamoDB (banco NoSQL gerenciado)
- S3 (armazenamento de arquivos)
- CloudFormation / SAM (infraestrutura como código)

## 📂 Estrutura
├── src/
│   ├── handler.py         # Função Lambda principal
│   └── pedido_service.py  # Lógica de negócio
├── template.yaml          # Definição da infraestrutura (SAM)
├── tests/
│   └── test_handler.py    # Testes da função
├── events/
│   └── evento-exemplo.json # Payload para teste local
├── requirements.txt       # Dependências Python
├── conftest.py            # Configuração do ambiente de testes
└── README.md

## 🚀 Como rodar localmente

Existem **duas formas** de testar o projeto: com o **SAM CLI** (fluxo HTTP completo) ou com o **pytest + moto** (testes de lógica, mais rápidos, sem AWS).

### Opção 1 — SAM CLI (fluxo HTTP completo)

Simula a AWS de verdade (Lambda + API Gateway + DynamoDB local), testando o endpoint como se estivesse em produção.

1. Instale o AWS SAM CLI
2. Rode a função localmente:
   sam local start-api
3. Teste o endpoint:
   http://localhost:3000/pedidos

### Opção 2 — pytest + moto (testes de lógica)

Testa a validação, o cálculo e a gravação usando um DynamoDB **mockado em memória** (moto), sem precisar de AWS nem do SAM CLI.

1. Instale as dependências:
   pip install -r requirements.txt
2. Rode os testes:
   pytest tests/ -v

> 💡 **Qual usar?** O SAM CLI testa o fluxo HTTP completo (recomendado antes do deploy). O pytest é mais rápido para validar a lógica a cada mudança no código.

## ☁️ Como fazer deploy
sam build
sam deploy --guided

## 🔄 Fluxo
Cliente → API Gateway → Lambda → DynamoDB

## 💰 Custo
O AWS Free Tier cobre 1 milhão de requisições/mês por 12 meses,
permitindo deixar a API rodando de graça.