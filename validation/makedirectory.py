import numpy as np
import os
import shutil

for idata in range(1,9):
    if idata!=5:
        for imir in range(2):
            for isider in range(2):
                if imir==0:
                    madd='mirror'
                else:
                    madd='nomirror'
                if isider==0:
                    sadd='btm'
                else:
                    sadd='top'
                stem='smallPBX_'+str(idata)+'_'+madd+'_'+sadd
                os.mkdir('./'+stem+'/')
                shutil.move(stem+'_input.npy','./'+stem+'/input.npy')
                shutil.move(stem+'_output.npy','./'+stem+'/output.npy')
