# Solving a delivery problem.
## Premise
Suppose you need to go to a few different places to run errands. What's the shortest path that gets you to all destinations and then return home?  
In graph theory, a common way to solve this problem is treating it as a Traveling Salesman Problem (for more information on TSP check https://en.wikipedia.org/wiki/Travelling_salesman_problem).  
The issue is that not all graphs fulfill the prerequisites for TSP. For said graphs, one can instead lift the limitation that each destination must be visited only once, though that itself creates several more complexions.  
The project report found in this repository details solving this generalization (denoted as the **delivery problem**) as a mixed integer program, practical considerations while implementing the program into code, efficiency of optimal solutions compared to that of TSP, and performances using solution heuristics.  
## Using this repository
Multiple README files are placed in different directories of the repository that indicate the types of files used for the project and how to properly use the codes/models to replicate results.  
I intend on adding PYOMO model files sometime in the near future.
## Integrity of results
Results from the project report should provide a decent estimate on what results from personal investigations would look like. If there are any new findings on results, please feel free to mention them through the use of the Issues feature in GitHub!
