'''
Generates the string to be put into AMPL data files.
Includes graph generation.
'''
def genStr(n,M,p):
    
    # Importing the numpy module for use.
    import numpy as np

    dummy = 0
    
    while dummy < n-1:  # Condition for if a spanning tree exists.
        
        # Generate random edge weights for time and fuel
        dataT = 1 + np.random.randint(1,10,int(n*(n-1)/2))
        dataF = 1 + np.random.randint(1,10,int(n*(n-1)/2))
        
        # Insert the random edge weights into parameter arrays
        fuel = np.ones((n,n))*M
        time = np.ones((n,n))*M
        dummy = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if np.random.rand() > p and (j-i-1)%(n-2) > 0:  # second clause guarantees a Hamiltonian cycle.
                    (time[i,j], time[j,i]) = (M,M)
                else:
                    (time[i,j], time[j,i]) = (dataT[dummy], dataT[dummy])
                (fuel[i,j], fuel[j,i]) = (dataF[dummy], dataF[dummy])
                dummy += 1
        
        # Generate the MST
        dupl = time.copy()              # duplicate matrix of time costs
        for i in range(n):
            for j in range(n):
                if j<i:
                    dupl[i,j] = M
        cMat = np.zeros((n,n))          # node connectivity matrix for MST
        mstMat = np.zeros((n,n))        # MST adjacency matrix
        mstEdgeA = np.zeros(n-1)        # MST edges list of nodes on one side
        mstEdgeB = np.zeros(n-1)        # same as above, except it's nodes on the other side
        mstHalfMat = np.zeros((n,n))    # greedy MST components adjacency matrix
        nodes = set()                   # dummy node set that indicate which nodes are connected to each other during MST algorithm process.
        
        dummy = 0
        while dummy<n-1:
            
            # locate branch with least cost
            if np.amin(dupl) == M:      # stopping condition
                break
            k = np.argmin(dupl)
            (k1, k2) = (k//n, k%n)
            dupl[k1,k2] = M
            
            # check whether branch creates a cycle
            if cMat[k1,k2] != 1:
                
                # update all matrices related to heurisitic approaches
                nodes.add(k1)
                nodes.add(k2)
                cMat[k1,k2] = 1
                mstMat[k1,k2] = 1
                mstEdgeA[dummy] = k1
                mstEdgeB[dummy] = k2
                if dummy < int((n-1)/2):
                    mstHalfMat[k1,k2] =1
                
                # update node connectivity matrix
                flag = True
                while flag == True:
                    flag = False
                    for i in range(n-2):
                        for j in range(i+1,n-1):
                            for k in range(j+1,n):
                                if cMat[i,j] + cMat[j,k] + cMat[i,k] == 2:
                                    cMat[i,j] = 1
                                    cMat[j,k] = 1
                                    cMat[i,k] = 1
                    
                dummy += 1
    
    # Generate the string
    dataStr = 'param fuelCost:'
    for i in range(n):
        dataStr += '  '+str(i+1)
    dataStr += ' :=\n'
    for i in range(n):
        dataStr += str(i+1)
        for j in range(n):
            dataStr += '  '+str(int(fuel[i,j]))
        dataStr += '\n'
    dataStr += ';\n'
    
    dataStr += 'param timeCost:'
    for i in range(n):
        dataStr += '  '+str(i+1)
    dataStr += ' :=\n'
    for i in range(n):
        dataStr += str(i+1)
        for j in range(n):
            dataStr += '  '+str(int(time[i,j]))
        dataStr += '\n'
    dataStr += ';\n'
    
    dataStr += 'param mst:'
    for i in range(n):
        dataStr += '  '+str(i+1)
    dataStr += ' :=\n'
    for i in range(n):
        dataStr += str(i+1)
        for j in range(n):
            if i>=j:
                dataStr += '  .'
            else:
                dataStr += '  '+str(int(mstMat[i,j]))
        dataStr += '\n'
    dataStr += ';\n'
    
    dataStr += 'param mstHalf:'
    for i in range(n):
        dataStr += '  '+str(i+1)
    dataStr += ' :=\n'
    for i in range(n):
        dataStr += str(i+1)
        for j in range(n):
            if i>=j:
                dataStr += '  .'
            else:
                dataStr += '  '+str(int(mstHalfMat[i,j]))
        dataStr += '\n'
    dataStr += ';\n'
    
    dataStr += 'param mstEdges:'
    for i in range(2):
        dataStr += '  '+str(i+1)
    dataStr += ' :=\n'
    for i in range(n-1):
        dataStr += str(i+1)
        dataStr += '  '+str(int(mstEdgeA[i]+1))
        dataStr += '  '+str(int(mstEdgeB[i]+1))
        dataStr += '\n'
    dataStr += ';\n'
    
    return dataStr