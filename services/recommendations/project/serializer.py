def comp_serialize(heroes):
    """Given an array of hero ids return a number with
    it the correct bit string representation
    """
    if len(heroes) > 0:
        result = 0
        for h in heroes:
            result = result | (2**h)
        return result
    return -1

# example_comp = [1,2,5]
# result = ids_to_bit_string(example_comp)
# print('{0:b}'.format(result))
# should return

def comp_deserialize(n):
    """Given a number representing a teams composition
    return an array of hero ids
    """
    i = 1
    pos = 1
    team_ids = []
    while(n):
        if (n&1) == 1:
            team_ids.append(pos)
        n = n >> 1
        pos += 1
    return team_ids

# example_comp = (2**2)|(2**1)|(2**3)
# print('{0:b}'.format(example_comp))

# should return [2, 1, 3]
# get_hero_index(example_comp)
