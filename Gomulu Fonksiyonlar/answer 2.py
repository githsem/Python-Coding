def ucgen(demet):
    if ((demet[0]+demet[1])>demet[2]) and ((demet[1]+demet[2])>demet[0]) and ((demet[0]+demet[2])>demet[1]) :
        return True
    else :
        return False
liste = [(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(ucgen,liste)))