# Esse controller gerencia as informações do perfil de saúde do usuário. As funções podem incluir:

# Visualizar Perfil:

# Retornar os dados de saúde do usuário logado (data da última avaliação, medicamentos, IMC).
# Atualizar Perfil:

# Permitir que o usuário atualize suas informações de saúde, como adicionar medicamentos ou atualizar a data da última avaliação.

from flask import Blueprint, request, jsonify

user = Blueprint('user', __name__)

@user.route('/profile', methods=['GET'])
def get_profile():
    # Lógica para obter as informações do perfil do usuário
    # user_data = db.get_user_data(user_id)
    return jsonify(user_data), 200

@user.route('/profile', methods=['PUT'])
def update_profile():
    # Lógica para atualizar as informações do perfil do usuário
    updated_data = request.json
    # db.update_user_data(user_id, updated_data)
    return jsonify({"message": "Perfil atualizado com sucesso!"}), 200
