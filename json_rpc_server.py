from jsonrpcserver import method, serve, Success, Error

usuarios = {}
next_id = 1

@method
def create_user(nome, email, idade):
    global next_id
    if not nome or not email:
        return Error("Nome e email obrigatórios!")
    
    for usuario in usuarios.values():
        if usuario['email'] == email:
            return Error("Email já existe!")
    
    usuario_id = str(next_id)
    usuario = {'id': usuario_id, 'nome': nome, 'email': email, 'idade': idade}
    usuarios[usuario_id] = usuario
    next_id += 1
    
    return Success(usuario)

@method
def list_users():
    return Success(list(usuarios.values()))

@method  
def get_user(usuario_id):
    usuario_id = str(usuario_id)
    if usuario_id not in usuarios:
        return Error("Usuário não encontrado!")
    return Success(usuarios[usuario_id])

@method
def update_user(usuario_id, nome=None, email=None, idade=None):
    usuario_id = str(usuario_id)
    if usuario_id not in usuarios:
        return Error("Usuário não encontrado!")
    
    usuario = usuarios[usuario_id]
    if nome: usuario['nome'] = nome
    if email: usuario['email'] = email
    if idade is not None: usuario['idade'] = idade
    
    return Success(usuario)

@method
def delete_user(usuario_id):
    usuario_id = str(usuario_id)
    if usuario_id not in usuarios:
        return Error("Usuário não encontrado!")
    
    usuario_removido = usuarios.pop(usuario_id)
    return Success(usuario_removido)

serve('localhost', 5000)

serve('localhost', 5000)