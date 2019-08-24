def comp_serialize(heroes):
    """Given an array of hero ids return a number with
    it the correct bit string representation
    """
    if len(heroes) > 0:
        result = 0
        for h in heroes:
            result = result | (2**h)
        return '{0:b}'.format(result)
    return "0"

def comp_deserialize(bit_string):
    """Given a number representing a teams composition
    return an array of hero id.fs
    """
    n = int(bit_string, 2)
    i = 1
    pos = 0
    team_ids = []
    while(n):
        if (n&1) == 1:
            team_ids.append(pos)
            # if len(team_ids) == 0:
            #     team_ids += str(pos)
            # else:
            #     team_ids += ',' + (str(pos))
        n = n >> 1
        pos += 1
    return team_ids

# example_comp = (2**2)|(2**1)|(2**3)
# print('{0:b}'.format(example_comp))

# should return [2, 1, 3]
# get_hero_index(example_comp)
