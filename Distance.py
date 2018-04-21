# MBD2-p66a inhibitor discovery
# Distance between compound and binding site calculation
# Insung Na. 11/28/2014

from scipy.spatial import distance

def main():
    Target = open('coor_V227_L234.txt', 'r')
    Target_rl = Target.readlines()
    Target.close()

    Comp = open('topdock_onlyATOMs.pdb')
    Comp_read = Comp.read()
    Comp.close()

    Output = open('Distance.txt', 'w')

##### Target Geometric Center #####

    i = 0
    X = 0
    Y = 0
    Z = 0

    for i in range(len(Target_rl)):
        if 'ATOM' in Target_rl[i]:
            X = X + float(Target_rl[i][31:38].replace(' ',''))
            Y = Y + float(Target_rl[i][39:46].replace(' ',''))
            Z = Z + float(Target_rl[i][47:54].replace(' ',''))
        else:
            break

    X = X/len(Target_rl)
    Y = Y/len(Target_rl)
    Z = Z/len(Target_rl)

    Output.write('Geometric Center of Target Site : ')
    Output.write(str(X)+' '+str(Y)+' '+str(Z)+'\n')


##### Compound Geometric Center & Distance Calculation #####

    j = 0

    J = Comp_read.count('MODEL')    # J : Number of Models

    while j <= J:
        One_Comp = Comp_read.split('MODEL')[j+1]
        k = 0
        x = 0
        y = 0
        z = 0
        for k in range(One_Comp.count('ATOM')):
            One_Atom = One_Comp.split('ATOM')[k+1]
            x = x+float(One_Atom[27:34].replace(' ',''))
            y = y+float(One_Atom[35:42].replace(' ',''))
            z = z+float(One_Atom[43:50].replace(' ',''))

        x = x/One_Comp.count('ATOM')
        y = y/One_Comp.count('ATOM')
        z = z/One_Comp.count('ATOM')

        A = (x, y, z)                   # Compound's Geometric Center
        B = (X, Y, Z)                   # Target's Geometric Center
        DIST = distance.euclidean(A,B)  # Distance Calculation using scipy module

        Output.write('MODEL '+str(j+1)+'|'+str(x)+','+str(y)+','+str(z))
        Output.write('|Distance '+str(DIST)+'|No. of Atoms '+str(One_Comp.count('ATOM'))+'\n')

        j = j+1
        
    Output.close()
