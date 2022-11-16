import numpy as np
import os
import shutil

regmat=['LL','LR','TL','TR']
for idata in range(1,5):
    for imir in range(2):
        for isider in range(2):
            for ireg in range(4):
                if imir==0:
                    madd='mirror'
                else:
                    madd='nomirror'
                if isider==0:
                    sadd='btm'
                else:
                    sadd='top'
                reg=regmat[ireg]
                stem='largePBX_'+str(idata)+'_'+madd+'_'+sadd+'_'+reg
                os.mkdir('./'+stem+'/')
                shutil.move(stem+'_input.npy','./'+stem+'/input.npy')
                shutil.move(stem+'_output.npy','./'+stem+'/output.npy')
