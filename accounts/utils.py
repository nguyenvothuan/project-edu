from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_decode_handler






def generate_jwt_token(user, data):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    data['token'] = token
    return data

def validate_access_token(access_token):
    try:
        token = jwt_decode_handler(access_token)
        return True
    except Exception:
        return False
    
def get_user_id_from_token(access_token):
    token = jwt_decode_handler(access_token)
    user_id = token['user_id']
    return user_id
