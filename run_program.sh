#!/bin/bash

# Function to run your program
run_program() {
    python3 Genetic.py  # Replace 'python my_script.py' with the actual command to run your program
}

# Run the program 30 times and record the real-time
total_time=0
for ((i=1; i<=30; i++)); do
    start_time=$(date +%s.%N)  # Record the start time in seconds with nanoseconds
    run_program  # Run your program

    # Calculate the elapsed time for each run
    end_time=$(date +%s.%N)
    elapsed_time=$(echo "$end_time - $start_time" | bc)
    total_time=$(echo "$total_time + $elapsed_time" | bc)  # Accumulate total time
    # Print the real-time for each run
    echo "Run $i: Real-time taken -> $elapsed_time seconds"
done

# Display the total time taken for all runs
echo "Total time taken for 30 runs: $total_time seconds"

