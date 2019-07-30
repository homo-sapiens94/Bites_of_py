def get_index_different_char(chars):
    a=str(chars[0])
    if a.isalnum():
        for i in range(1,len(chars)):
            if not str(chars[i]).isalnum():
                return i
    else:
        for i in range(1,len(chars)):
            if str(chars[i]).isalnum():
                return i