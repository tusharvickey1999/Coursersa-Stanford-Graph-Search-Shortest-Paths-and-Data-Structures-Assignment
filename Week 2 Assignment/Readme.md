# Dijsktra Single Source Shortest Path  
This algorithm is designed to calculate shortest distance between a source and all other vertices in the graph.  
We can implement this algorithm using array(O(m*n)) or heap(O(m*logn)) but heap implementation gives better run time.  
heappush() : Used to push a element into heap and then bubble it up as required.  
heappop() : Used to pop the root and then copy the last element to the root. bubble it down as required.  
heappop2() : Used to pop any specific element from the heap other than root.
For the given testcase:  
Running time : 0.01 seconds  
Memory : less than 100 MB  
file : foo.txt (change it to your file name)  
