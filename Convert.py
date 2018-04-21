# Convert test.eel1.pdb into Result.pdb
# Insung Na. 12/17/2014

def main():
    Test = open('./dock1/start/test.eel1.pdb', 'r')
    Test_rl = Test.readlines()
    Test.close()

    Out = open('Result.pdb', 'w')

    i = 0
    j = 1

    for i in range(len(Test_rl)):
        if ('REMARK' in Test_rl[i]) and ('energy' not in Test_rl[i]):
            Out.write('MODEL'+'        '+str(j)+'\n'+Test_rl[i])
        elif ('REMARK' in Test_rl[i]) and ('energy' in Test_rl[i]):
            Out.write(Test_rl[i])
        elif ('ATOM' in Test_rl[i]):
            Out.write(Test_rl[i])
        elif ('TER' in Test_rl[i]):
            Out.write(Test_rl[i]+'ENDMDL'+'\n')
            j = j+1
        else:
            pass

    Out.close()

main()
