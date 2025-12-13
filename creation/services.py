from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

User = get_user_model()


def create_user_from_request(access_request):
    password = get_random_string(12)

    user = User.objects.create_user(
        username=access_request.username,
        email=access_request.email,
        password=password,
    )

    user.first_name = access_request.full_name
    user.save()

    return user, password
