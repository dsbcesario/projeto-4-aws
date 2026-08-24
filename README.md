API Serverless de Processamento de PedidosFunção AWS Lambda exposta via API Gateway que processa pedidos e
armazena os dados no DynamoDB, com deploy automatizado.🎯 ObjetivoDemonstrar o ecossistema AWS: computação serverless, banco gerenciado,
integração de serviços e infraestrutura como código.🛠️ Tecnologias
AWS Lambda (computação serverless)
API Gateway (exposição da API)
DynamoDB (banco NoSQL gerenciado)
S3 (armazenamento de arquivos)
CloudFormation / SAM (infraestrutura como código)
📂 Estrutura├── src/
│   ├── handler.py         # Função Lambda principal
│   └── pedido_service.py  # Lógica de negócio
├── template.yaml          # Definição da infraestrutura (SAM)
├── tests/
│   └── test_handler.py    # Testes da função
├── events/
│   └── evento-exemplo.json # Payload para teste local
├── requirements.txt       # Dependências Python
├── conftest.py            # Configuração do ambiente de testes
└── README.md🚀 Como rodar localmenteExistem duas formas de testar o projeto: com o SAM CLI (fluxo HTTP completo) ou com o pytest + moto (testes de lógica, mais rápidos, sem AWS).Opção 1 — SAM CLI (fluxo HTTP completo)Simula a AWS de verdade (Lambda + API Gateway + DynamoDB local), testando o endpoint como se estivesse em produção.
Instale o AWS SAM CLI
Rode a função localmente:
sam local start-api
Teste o endpoint:
http://localhost:3000/pedidos
Opção 2 — pytest + moto (testes de lógica)Testa a validação, o cálculo e a gravação usando um DynamoDB mockado em memória (moto), sem precisar de AWS nem do SAM CLI.
Instale as dependências:
pip install -r requirements.txt
Rode os testes:
pytest tests/ -v

💡 Qual usar? O SAM CLI testa o fluxo HTTP completo (recomendado antes do deploy). O pytest é mais rápido para validar a lógica a cada mudança no código.
☁️ Como fazer deploysam build
sam deploy --guided🔄 FluxoCliente → API Gateway → Lambda → DynamoDB💰 CustoO AWS Free Tier cobre 1 milhão de requisições/mês por 12 meses,
permitindo deixar a API rodando de graça.