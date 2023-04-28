'''
Generates AMPL data files using the graph generation module genStr.
Also generates AMPL scripts that run the optimization.
'''
from genStr import genStr

# Parameters can be set here.
n = 16
M = 100     # some big constant for edges that should not exist in the graph.
p = 0.2     # probability parameter for edge generation.
sample_size = 100 # recommended set to a maximum of 100.

# File generation
for i in range(sample_size):
    
    # Data files
    if i < 10:
        filename = '../data_files/n'+str(n)+'/input/data_'+str(n)+'_0'+str(i)+'.dat'
    else:
        filename = '../data_files/n'+str(n)+'/input/data_'+str(n)+'_'+str(i)+'.dat'
    f = open(filename, 'w')
    f.write(genStr(n,M,p))
    f.close()
    
    # Script files
    if i < 10:
        filename = './scripts/script_'+str(n)+'_0'+str(i)+'.run'
        dataname = '../data_files/n'+str(n)+'/input/data_'+str(n)+'_0'+str(i)+'.dat'
    else:
        filename = './scripts/script_'+str(n)+'_'+str(i)+'.run'
        dataname = '../data_files/n'+str(n)+'/input/data_'+str(n)+'_'+str(i)+'.dat'
    
    g = open(filename, 'w')
    if i < 10:
        g.write('option log_file '+'\'../data_files/n'+str(n)+'/output/out_' +str(n)+'_0'+str(i) + '.txt\';\n')
    else:
        g.write('option log_file '+'\'../data_files/n'+str(n)+'/output/out_' +str(n)+'_'+str(i) + '.txt\';\n')
    g.write('reset; model projcyc.mod; data '+dataname+';\n')
    g.write('subject to tspReq {i in nodes}: z[i] = 1; solve;\n')
    g.write('drop tspReq; display ctime(); solve; display ctime();\n')
    g.write('subject to mstHalfReq {(i,j) in edges}: yTree[i,j] >= mstHalf[i,j]; solve;\n')
    g.write('drop mstHalfReq; subject to threeChange: sum{i in 1..n-1} yTree[mstEdges[i,1],mstEdges[i,2]] = n-4; solve;\n')
    g.write('drop threeChange; subject to mstReq {(i,j) in edges}: y[i,j] >= mst[i,j]; solve;\n')
    g.write('reset; option log_file \'\';\n')
    g.close()

# Big script files
h = open('./scripts/script.run', 'w')
for i in range(sample_size):
    if i < 10:
        h.write('include ./scripts/script_'+str(n)+'_0'+str(i)+'.run;\n')
    else:
        h.write('include ./scripts/script_'+str(n)+'_'+str(i)+'.run;\n')
h.write('reset; option log_file \'\';\n')
h.close()

j = open('./scripts/script.tsp_run', 'w')
j.write('option log_file '+'\'../data_files/n'+str(n)+'/output/out_'+str(n)+'_tsp.txt\';\n')
for i in range(sample_size):
    if i < 10:
        filename = '../data_files/n'+str(n)+'/input/data_'+str(n)+'_0'+str(i)+'.dat'
    else:
        filename = '../data_files/n'+str(n)+'/input/data_'+str(n)+'_'+str(i)+'.dat'
    j.write('reset; model tspmod.mod; data '+filename+'; display ctime(); solve; display ctime();\n')
j.write('reset; option log_file \'\';\n')
j.close()
