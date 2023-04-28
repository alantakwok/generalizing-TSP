'''Performs analysis and returns arrays for plotting.'''
def analysis():
    import numpy as np
    
    # adjust sample sizes as necessary
    (sample11,sample13,sample15,sample16,sample17,sample18,sample19) = (100,100,100,100,70,40,10)
    
    # do not change anything below this
    totalSamples = sample11+sample13+sample15+sample16+sample17+sample18+sample19
    ratioarray = np.zeros((totalSamples,5))
    
    totalDummy = 0
    
    time11 = np.zeros((sample11,2))
    dummy = 0
    f = open('../results/out_11.csv','r')
    f.readline()
    for line in f:
        linedata = line.split(',')
        (tsp,dp,mstHalf,mst3c,mst) = (int(linedata[2]),int(linedata[6]),int(linedata[8]),int(linedata[9]),int(linedata[-1][:-1]))
        timetsp = int(linedata[3])-int(linedata[1])
        timedp = int(linedata[7])-int(linedata[5])
        if timetsp < 0:
            timetsp += 3600
        if timedp < 0:
            timedp += 3600
        time11[dummy,:] = [timetsp,timedp]
        ratioarray[totalDummy,:] = [dp/tsp,tsp/dp,mst/dp,mstHalf/dp,mst3c/dp]
        dummy += 1
        totalDummy += 1
    f.close()
    
    time13 = np.zeros((sample13,2))
    dummy = 0
    f = open('../results/out_13.csv','r')
    f.readline()
    for line in f:
        linedata = line.split(',')
        (tsp,dp,mstHalf,mst3c,mst) = (int(linedata[2]),int(linedata[6]),int(linedata[8]),int(linedata[9]),int(linedata[-1][:-1]))
        timetsp = int(linedata[3])-int(linedata[1])
        timedp = int(linedata[7])-int(linedata[5])
        if timetsp < 0:
            timetsp += 3600
        if timedp < 0:
            timedp += 3600
        time13[dummy,:] = [timetsp,timedp]
        ratioarray[totalDummy,:] = [dp/tsp,tsp/dp,mst/dp,mstHalf/dp,mst3c/dp]
        dummy += 1
        totalDummy += 1
    f.close()
    
    time15 = np.zeros((sample15,2))
    dummy = 0
    f = open('../results/out_15.csv','r')
    f.readline()
    for line in f:
        linedata = line.split(',')
        (tsp,dp,mstHalf,mst3c,mst) = (int(linedata[2]),int(linedata[6]),int(linedata[8]),int(linedata[9]),int(linedata[-1][:-1]))
        timetsp = int(linedata[3])-int(linedata[1])
        timedp = int(linedata[7])-int(linedata[5])
        if timetsp < 0:
            timetsp += 3600
        if timedp < 0:
            timedp += 3600
        time15[dummy,:] = [timetsp,timedp]
        ratioarray[totalDummy,:] = [dp/tsp,tsp/dp,mst/dp,mstHalf/dp,mst3c/dp]
        dummy += 1
        totalDummy += 1
    f.close()
    
    time16 = np.zeros((sample16,2))
    dummy = 0
    f = open('../results/out_16.csv','r')
    f.readline()
    for line in f:
        linedata = line.split(',')
        (tsp,dp,mstHalf,mst3c,mst) = (int(linedata[2]),int(linedata[6]),int(linedata[8]),int(linedata[9]),int(linedata[-1][:-1]))
        timetsp = int(linedata[3])-int(linedata[1])
        timedp = int(linedata[7])-int(linedata[5])
        if timetsp < 0:
            timetsp += 3600
        if timedp < 0:
            timedp += 3600
        time16[dummy,:] = [timetsp,timedp]
        ratioarray[totalDummy,:] = [dp/tsp,tsp/dp,mst/dp,mstHalf/dp,mst3c/dp]
        dummy += 1
        totalDummy += 1
    f.close()
    
    time17 = np.zeros((sample17,2))
    dummy = 0
    f = open('../results/out_17.csv','r')
    f.readline()
    for line in f:
        linedata = line.split(',')
        (tsp,dp,mstHalf,mst3c,mst) = (int(linedata[2]),int(linedata[6]),int(linedata[8]),int(linedata[9]),int(linedata[-1][:-1]))
        timetsp = int(linedata[3])-int(linedata[1])
        timedp = int(linedata[7])-int(linedata[5])
        if timetsp < 0:
            timetsp += 3600
        if timedp < 0:
            timedp += 3600
        time17[dummy,:] = [timetsp,timedp]
        ratioarray[totalDummy,:] = [dp/tsp,tsp/dp,mst/dp,mstHalf/dp,mst3c/dp]
        dummy += 1
        totalDummy += 1
    f.close()
    
    time18 = np.zeros((sample18,2))
    dummy = 0
    f = open('../results/out_18.csv','r')
    f.readline()
    for line in f:
        linedata = line.split(',')
        (tsp,dp,mstHalf,mst3c,mst) = (int(linedata[2]),int(linedata[6]),int(linedata[8]),int(linedata[9]),int(linedata[-1][:-1]))
        timetsp = int(linedata[3])-int(linedata[1])
        timedp = int(linedata[7])-int(linedata[5])
        if timetsp < 0:
            timetsp += 3600
        if timedp < 0:
            timedp += 3600
        time18[dummy,:] = [timetsp,timedp]
        ratioarray[totalDummy,:] = [dp/tsp,tsp/dp,mst/dp,mstHalf/dp,mst3c/dp]
        dummy += 1
        totalDummy += 1
    f.close()
    
    time19 = np.zeros((sample19,2))
    dummy = 0
    f = open('../results/out_19.csv','r')
    f.readline()
    for line in f:
        linedata = line.split(',')
        (tsp,dp,mstHalf,mst3c,mst) = (int(linedata[2]),int(linedata[6]),int(linedata[8]),int(linedata[9]),int(linedata[-1][:-1]))
        timetsp = int(linedata[3])-int(linedata[1])
        timedp = int(linedata[7])-int(linedata[5])
        if timetsp < 0:
            timetsp += 3600
        if timedp < 0:
            timedp += 3600
        time19[dummy,:] = [timetsp,timedp]
        ratioarray[totalDummy,:] = [dp/tsp,tsp/dp,mst/dp,mstHalf/dp,mst3c/dp]
        dummy += 1
        totalDummy += 1
    f.close()
    
    return (time11,time13,time15,time16,time17,time18,time19,ratioarray)