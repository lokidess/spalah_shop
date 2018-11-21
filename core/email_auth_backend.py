from django.contrib.auth.models import User


class AuthByEmail:

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, request, username=None, password=None):
        user = None
        try:
            user = User.objects.get(email=username)
            if not user.check_password(password):
                return None
        except User.DoesNotExist:
            pass

        return user

