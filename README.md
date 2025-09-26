# CRUD com JSON-RPC

Sistema CRUD (Create, Read, Update, Delete) implementado usando JSON-RPC para comunicação entre cliente e servidor.

## Descrição

Este projeto demonstra a implementação de um sistema distribuído usando RPC (Remote Procedure Call) com protocolo JSON-RPC 2.0 para gerenciar usuários.

## Funcionalidades

- **CREATE**: Criar novo usuário
- **READ**: Listar todos os usuários ou buscar usuário por ID
- **UPDATE**: Atualizar dados de um usuário existente
- **DELETE**: Remover usuário do sistema

## Estrutura do Projeto

```
├── json_rpc_server.py    # Servidor JSON-RPC com métodos CRUD
├── json_rpc_client.py    # Cliente para testar as operações
├── requirements.txt      # Dependências do projeto
└── README.md            # Este arquivo
```

## Instalação

1. Clone ou baixe o projeto
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Executar

### 1. Iniciar o Servidor
```bash
python json_rpc_server.py
```
O servidor será iniciado em `http://localhost:5000`

### 2. Executar o Cliente (em outro terminal)
```bash
python json_rpc_client.py
```

## Métodos Disponíveis

- `create_user(nome, email, idade)` - Criar usuário
- `list_users()` - Listar todos os usuários
- `get_user(usuario_id)` - Buscar usuário por ID
- `update_user(usuario_id, nome, email, idade)` - Atualizar usuário
- `delete_user(usuario_id)` - Deletar usuário

## Exemplo de Uso

O cliente executa automaticamente todas as operações CRUD:
1. Cria um usuário
2. Lista todos os usuários
3. Busca o usuário criado
4. Atualiza os dados do usuário
5. Remove o usuário

## Tecnologias

- Python 3.x
- JSON-RPC 2.0
- Biblioteca `jsonrpcserver`
- Biblioteca `requests`