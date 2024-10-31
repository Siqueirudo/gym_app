# Esse controller lida com a autenticação do usuário. As principais funções podem incluir:

# Registro de Usuário:

# Receber dados do usuário (nome de usuário, senha).
# Verificar se o usuário já existe.
# Salvar os dados no banco, garantindo que a senha seja criptografada.
# Login de Usuário:

# Receber dados de login (nome de usuário, senha).
# Verificar se as credenciais estão corretas.
# Retornar um token (se usar autenticação baseada em token, como JWT) ou uma mensagem de sucesso.

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database.db_connection import get_db  # Função para obter a conexão com o DB

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Lógica para verificar se o usuário já existe e salvar no DB
    hashed_password = generate_password_hash(password, method='sha256')
    # db.save_user(username, hashed_password)
    
    return jsonify({"message": "Usuário registrado com sucesso!"}), 201

@auth.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Lógica para verificar as credenciais
    # user = db.get_user(username)
    # if user and check_password_hash(user['password'], password):
    #     return jsonify({"message": "Login bem-sucedido!"}), 200
    return jsonify({"message": "Credenciais inválidas!"}), 401
