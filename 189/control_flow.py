IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def contains_digit(name):
    for i in name:
        if i.isdigit():
            return True
    return False

def filter_names(names):
    filtered_list = []
    digits = range(0,10)
    count = 0
    for name in names:
    	if name[0]== QUIT_CHAR or count>=MAX_NAMES:
    		break
    	elif name[0]==IGNORE_CHAR or contains_digit(name) :
    		continue
    	else:
    		filtered_list.append(name)
    		count+=1
    
    
    return filtered_list