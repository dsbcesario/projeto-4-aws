import os
import sys
from pathlib import Path

# Define a região AWS (necessário para o boto3 criar o cliente DynamoDB)
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

# Adiciona a raiz do projeto ao caminho de importação
sys.path.insert(0, str(Path(__file__).parent))

# Adiciona a pasta src/ (o handler importa 'pedido_service' sem prefixo)
sys.path.insert(0, str(Path(__file__).parent / "src"))