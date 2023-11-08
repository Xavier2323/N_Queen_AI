from numpy import random
import numpy as np
import time
N = 50 
start_time = time.time()

def random_state():
    arr = np.array([i for i in range(N)])
    random.shuffle(arr)
    return arr

def attacking_pairs(state):
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if abs(state[i] - state[j]) == (j - i):
                ans += 1
    return ans

def hill_climbing():
    current_state = random_state()
    current_value = attacking_pairs(current_state)
    best = N * (N - 1) / 2
    while True:
        if current_value == 0:
            print("Solution found:")
            print(current_state)
            return

        if time.time() - start_time >= 100:
            print("Best # of Attacking: ")
            print(best)
            return

        neighbor_state = current_state.copy()

        for i in range(N - 1):
            for j in range(i + 1, N):
                # Swap i, j and calculate attacking pairs
                neighbor_state[i], neighbor_state[j] = neighbor_state[j], neighbor_state[i]
                neighbor_value = attacking_pairs(neighbor_state)

                # If the value decreases, update the current state.
                if neighbor_value < current_value:
                    current_state = neighbor_state.copy()
                    current_value = neighbor_value
                    if(neighbor_value < best):
                        best = neighbor_value
                    break

                # Undo the swap
                neighbor_state[i], neighbor_state[j] = neighbor_state[j], neighbor_state[i]
        
        # If no improvement in the state, jump to a random neighbor and continue hill-climbing
        if np.array_equal(current_state, neighbor_state) and current_value != 0:
            current_state = random_state()
            current_value = attacking_pairs(current_state)

# Solve the N-queens problem using Hill Climbing
hill_climbing()

