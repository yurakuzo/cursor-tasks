import random
import string

def coupon_code_gen(length=16):
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    coupon_code = ''.join(random.choice(characters) for _ in range(length))
    return coupon_code
