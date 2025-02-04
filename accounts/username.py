from .models import User
from string import digits
from random import choice

def get_username(instance):
    first_name = instance.first_name.upper()
    last_name = instance.last_name.upper()
    user_id = str(instance.id)
    random_numbers = "".join(choice(digits) for _ in range(2))
    username = f"{first_name}.{last_name}-{user_id}{random_numbers}"

    return username
