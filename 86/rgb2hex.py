def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    code = '0123456789ABCDEF'
    lst = ['#']
    error_string = f'Value not in range(0-255)'
    if any(value not in range(0, 256) for value in rgb):
        raise ValueError(error_string)

    else:
        for i in rgb:
            if i < 10:
                lst.extend(f'0{i}')
            else:
                first = i//16
                second = int((i/16-first)*16)
                lst.extend(f'{code[first]}{code[second]}')
    return ''.join(lst)



