def get_profile(name, age, *args, **kwargs):
    new_dict={}
    if type(age)!=int or len(args)>5:
        raise ValueError
    else:
        new_dict['name']=name
    new_dict['age']=age
    
    if len(args)>0:
        new_dict['sports']=[]
        for value in args:
            new_dict['sports'].append(value)
        new_dict['sports'].sort()
    if len(kwargs)>0:
        new_dict['awards']={}
        for key,value in kwargs.items():
            new_dict['awards'][key]=value
    
    return new_dict


#pybites solution

def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int):
        raise ValueError('Age needs to be an int')

    if len(sports) > 5:
        raise ValueError('Max of 5 sports allowed')

    profile = {'name': name, 'age': age}

    if sports:
        profile['sports'] = sorted(sports)

    if awards:
        profile['awards'] = awards

    return profile