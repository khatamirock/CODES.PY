from pyformlang.cfg import Production, Variable, Terminal, CFG

'''variables'''

E=Variable("E")
F=Variable("F")


'''terminals'''
ter_a=Terminal("a")
ter_b=Terminal("b")
zero=Terminal("0")
one=Terminal("1")
plus=Terminal("+")
mult=Terminal("*")
lbracket=Terminal("(")
rbracket=Terminal(")")

'''production Rules'''
p1=Production(E,[E,plus,E])
p2=Production(E,[E,mult,E])
p3=Production(E,[lbracket,E,rbracket])
p4=Production(E,[F])

p5=Production(F,[ter_a,F])
p6=Production(F,[ter_b,F])
p7=Production(F,[zero,F])
p8=Production(F,[one,F])
p9=Production(F,[one])
p10=Production(F,[zero])
p11=Production(F,[ter_a])
p12=Production(F,[ter_b])
p13=Production(F,[])

#creation of the CFG
cfg=CFG({E,F},{ter_a,ter_b,one,zero,mult,lbracket,rbracket},E,{p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13})

while True:
    s = input('Please Enter a string :')
    if cfg.contains(s):
        print("It is accepted by the grammar\n")
        print("Derivation:")
        result = cfg.get_cnf_parse_tree(s)
        print(result)
    else:
        print("It is not accepted by the grammar")

    print("Do you want to continue?(Y/N):")
    check = input().lower()
    if(check=="n"):
        break