import secrets
import string

alphabet= string.ascii_uppercase + string.digits

def gen_key(parts=4, chars_per_part = 8):
    final_list = []
    for i in range(parts):
        final_list.append(''.join([secrets.choice(alphabet) for i in range(chars_per_part)]))
    return ('-'.join(final_list))





""" Pybites solution
def gen_key(parts=4, chars_per_part=8):
    return DASH.join(''.join(choice(ALPHABET) for i in range(chars_per_part))
                     for _ in range(parts))
"""


