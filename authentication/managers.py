from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where code is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, document_id, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not document_id:
            raise ValueError('The document must be set')
        document_id = self.normalize_email(document_id)
        user = self.model(document_id=document_id, **extra_fields)
        user.set_password(password)
        user.save()
        return user    
    
    def create_superuser(self, document_id, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('state', 'active')
        extra_fields.setdefault('role', 1)
        extra_fields.setdefault('is_active', True)        

        if extra_fields.get('role') != 1:
            raise ValueError('User is not superuser')
        return self.create_user(document_id, password, **extra_fields)    