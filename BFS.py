import time
import math
import numpy as np
import matplotlib.pyplot as plt

def check(n, v):

    if len(v) != len(set(v)):
        return False

    for i in range(n):
        for j in range(i+1,n):
            if i==j:
                continue
            if (abs(i-j) == abs(v[i]-v[j])):
                return False
    return True

def board(v):
    for b in v:
        for i in b:
            print('')
            for j in range(len(b)):
                if j != i:
                    print("-", end=' ')
                else:
                    print("Q", end=' ')
        print('')

def bfs(n, vec):
    start = time.time()
    if n <= 3:
        if n == 1:                          
            end = time.time()
            e_t = end - start
            return [1], 1, 0, 1, e_t 
        end = time.time()
        e_t = end - start
        return [], 0, 0, 0, e_t 

    queue = [[]]
    final_queens = 0
    gen_states = 0
    check_states = 0
    l_c_s = []

    while len(queue) != 0:                
        state = queue.pop()
        if len(state) == n:
            if check(len(state), state) == True:
                final_queens +=1
                vec.append(state)
                l_c_s.append(check_states)
            check_states += 1

        for q in range(n):
            queens = state.copy()
            if len(queens) < n:
                queens.append(q)
                queue.append(queens)
                gen_states += 1

    end = time.time()
    e_t = end - start
    return vec, final_queens, gen_states, l_c_s , round(e_t, 3)


n_l, g_l, c_l, e_t_l = [], [], [], []
for n in range(4, 9):
    hetmans, quantity, generated, checked, e_t  = bfs(n, [])
    g_l.append(generated)
    c_l.append(checked[0])
    e_t_l.append(e_t)
    n_l.append(n)
    print("FOR N: ", n)
    board(hetmans)
    print(hetmans)
    print("Quantity: ", quantity, "Generated states: ", generated, "Estimated time in seconds: ", e_t)
    print("Checked states: ", checked)
    print("===========================================================================================")

                                                 # PLOTS
plt.subplot(3,1,1)
plt.plot(n_l, g_l, 'r.', linestyle = 'solid', label="Generated states")
for i in range(len(n_l)):
    plt.text(n_l[i], g_l[i], (g_l[i]))
plt.xticks(np.arange(min(n_l), max(n_l)+1, 1))
plt.xlabel("N-Queens")
plt.ylabel("Generated states")
plt.subplot(3,1,2)
plt.plot(n_l, c_l, 'b.', linestyle = 'solid', label="Checked states")
for i in range(len(n_l)):
    plt.text(n_l[i], c_l[i], (c_l[i]))
plt.xticks(np.arange(min(n_l), max(n_l)+1, 1))
plt.xlabel("N-Queens")
plt.ylabel("Checked states")
plt.subplot(3,1,3)
plt.plot(n_l, e_t_l, 'g.', linestyle = 'solid', label="Estimated time (s)")
for i in range(len(n_l)):
    plt.text(n_l[i], e_t_l[i], (e_t_l[i]))
plt.xticks(np.arange(min(n_l), max(n_l)+1, 1))
plt.xlabel("N-Queens")
plt.ylabel("Estimated time (s)")
plt.tight_layout()
plt.show()