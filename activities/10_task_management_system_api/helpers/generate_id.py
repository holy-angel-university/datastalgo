import random
import string


def generate_unique_id():
    return "".join(random.choices(string.ascii_letters + string.digits, k=8))
