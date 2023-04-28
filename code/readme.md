Codes should be run in the following order:  
1. `fileGen.py` generates data files and scripts required to be run in AMPL models.
2. `projcyc.mod` and `tspmod.mod` represent the general delivery program model (directed) and the TSP model written in AMPL; one should alter parameters and/or add constraints if necessary.  
3. `script.run` (generated from Step 1) should be run within AMPL to generate output log files.  
4. `csvGen.py` generates output .csv files that re-organizes all log files of a single graph size.  
5. `analysisPlots.py` generates statistics and plots from the .csv files generated from Step 4.  
Running outside the intended order may not generate the necessary statistics/plots, so please proceed with care.
