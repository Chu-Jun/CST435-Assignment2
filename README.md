# Execute the MPI code by typing this command in your console:
mpiexec -n NUMOFPROCESS python CODEFILEPATH INPUTFILEPATH

# Execute the MapReduce code by typing this command in your console:
type INPUTFILEPATH | python MAPPERFILEPATH | sort | python REDUCERFILEPATH

The command above is just for running mapreduce in local.

It needs to be run in Apache Hadoop to increase the number of process.

Feel free to add more integers to the text file, so that it can show the differences between their performance.
