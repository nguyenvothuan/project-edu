from rest_framework_jwt.utils import jwt_decode_handler
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model


def generate_jwt_token(user, data):
    data['token'] = str(AccessToken.for_user(user))
    return data


def validate_access_token(access_token):
    """
    Deprecated: This function is no longer supported and should not be used.
    Instead, re-implement this using simplejwt.
    """
    try:
        _ = jwt_decode_handler(access_token)
        return True
    except Exception:
        return False


def get_user_id_from_token(access_token: str):
    return get_user(access_token)['user_id']


def get_user(access_token: str):
    return AccessToken(access_token)


def get_user_from_header(header):
    _, token = header['Authorization'].split()
    user_id = get_user_id_from_token(token)
    print(user_id)
    # Get the user object from the user_id
    User = get_user_model()
    user = User.objects.get(pk=user_id)
    return user
