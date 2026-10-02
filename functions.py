from numpy.f2py import rules


def simple_reflex_agent(percept):

    rules = {"dust" : "clean" , "wall" : "turn" ,
            "obstacles" : "turn" , "clean_floor" : "move_forward" , }
    return rules.get(percept , "no action")

for p in ["dust" , "wall" , "Clean_floor" , "obstacles" ]:
    print(p , "->" , simple_reflex_agent(p))