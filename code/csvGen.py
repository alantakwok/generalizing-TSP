'''
Reads output files and converts the output data into csv.
'''
import os
# set parameters first, please copy the values from fileGen.
n = 16
sample_size = 100

# read data
filename = '../results/out_'+str(n)+'.csv'
f = open(filename, 'w')
f.write('graph,tsp_t1,tsp,tsp_t2,dp_tsp,dp_t1,dp,dp_t2,dp_mstH,dp_mst3c,dp_mst\n')
h = open('../data_files/n'+str(n)+'/output/out_' +str(n)+'_tsp.txt', 'r')
for i in range(sample_size):
    f.write(str(i))
    
    flag = 0
    while flag < 2:
        linetsp = h.readline()
        if linetsp[0:5] == 'CPLEX':
            f.write(','+linetsp.split()[-1])
        if linetsp[0:5] == 'ctime':
            timestr = linetsp.split()[-2]
            timetuple = (timestr[3:5],timestr[6:])
            f.write(','+str(int(timetuple[0])*60 + int(timetuple[1])))
            flag += 1
        
    
    if i < 10:
        outputname = '../data_files/n'+str(n)+'/output/out_' +str(n)+'_0'+str(i) + '.txt'
        scriptname = './scripts/script_'+str(n)+'_0'+str(i)+'.run'
    else:
        outputname = '../data_files/n'+str(n)+'/output/out_' +str(n)+'_'+str(i) + '.txt'
        scriptname = './scripts/script_'+str(n)+'_'+str(i)+'.run'
    g = open(outputname, 'r')
    for line in g:
        if line[0:5] == 'CPLEX':
            f.write(','+line.split()[-1])
        if line[0:5] == 'ctime':
            timestr = line.split()[-2]
            timetuple = (timestr[3:5],timestr[6:])
            f.write(','+str(int(timetuple[0])*60 + int(timetuple[1])))

    g.close()
    f.write('\n')
    
    if os.path.exists(scriptname):
        os.remove(scriptname)
h.close()
f.close()

if os.path.exists('./scripts/script_tsp.run'):
    os.remove('./scripts/script_tsp.run')
if os.path.exists('./scripts/script.run'):
    os.remove('./scripts/script.run')