from django.contrib.auth.models import User


class EmailBackend(object):

    def authenticate(self, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        try:
            if email:
                user = User.objects.get(email=email)
            else:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = User.objects.get(email=username)
            
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None