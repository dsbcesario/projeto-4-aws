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
└── README.md

## 🚀 Como rodar localmente
1. Instale o AWS SAM CLI
2. Rode a função localmente:
   sam local start-api
3. Teste o endpoint:
   http://localhost:3000/pedidos

## ☁️ Como fazer deploy
sam build
sam deploy --guided

## 🔄 Fluxo
Cliente → API Gateway → Lambda → DynamoDB

## 💰 Custo
O AWS Free Tier cobre 1 milhão de requisições/mês por 12 meses,
permitindo deixar a API rodando de graça.