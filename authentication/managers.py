from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where code is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, code, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not code:
            raise ValueError('The Email must be set')
        code = self.normalize_email(code)
        user = self.model(code=code, **extra_fields)
        user.set_password(password)
        user.save()
        return user    
    
    def create_superuser(self, code, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(code, password, **extra_fields)    