def doesIvanovHit():
    import random
    random.seed()
    return (random.random() < 2/3.0)

def doesPetrovHit():
    import random
    random.seed()
    return (random.random() < 5/6.0)

def isHeads():
    import random
    random.seed()
    return (random.random() < 0.5)