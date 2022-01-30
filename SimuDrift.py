#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 21:26:09 2022
@author: Luis Rodrigo Arce-Valdés

SimuDrift is a simple genetic flow simulation I did as a way to practice python.
This program creates simulated plots of changes in allelic frequencies in generations as a function of effective population size.
The program assumes a Fisher-Wright like population of haploid organisms with non-overlapping generations, no gene-flow, mutation or selection towards one allele.
"""

# Importing modules
import numpy as np
import matplotlib.pyplot as plt

# Prompt to be displayed to the user
A1 = int(input("Enter the number of A1 alleles (the allele we will be tracking):\n"))
if A1 <= 0:
    print("Invalid A1 input, must be an integer higher or equal than 1")
    exit()
else:
    A2 = int(input("Enter the number of A2 alleles:\n"))
    if A2 <= 0:
        print("Invalid A2 input, must be an integer higher or equal than 1")
        exit()
    else:
        gens = int(input("Enter the number of generations to track:\n"))
        if gens <= 0:
            print("Invalid generations input, must be an integer higher or equal than 1")
            exit()
        else:
            sims = int(input("Enter the number of simulations to perform:\n"))
            if sims <= 0:
                print("Invalid simulations input, must be an integer higher or equal than 1")
                exit()

# Creating simulated population
initial_pop = []
for i in range(A1):
    initial_pop.append("A1")

for i in range(A2):
    initial_pop.append("A2")
    
# Estimating effective population size and initial allelic frequency (A1)
Ne = len(initial_pop)
initial_p = initial_pop.count("A1")/Ne

# Creating more lists:
p_list = [initial_p]
drift = []

# Genetic drift simulation inside for loops:
for a in range(sims):
    pop = initial_pop
    for b in range(gens):
        temp_pop = []
        for c in range(Ne):
            index = np.random.randint(0, Ne)
            temp_pop.append(pop[index])
        p = temp_pop.count("A1")/Ne
        p_list.append(p)
        pop = temp_pop
    drift.append(p_list)
    p_list = [initial_p]

# Transforming into a numpy array and transposing:
drift = np.transpose(np.array(drift))

# Ploting
plt.plot(drift)
plt.xlabel("Generation")
plt.ylabel("p[A1]")
plt.suptitle("Ne= " + str(Ne) + "; p(t0)= " + str(round(initial_p, 3)))

# Setting axis limits
ax = plt.gca()
ax.set_ylim([0, 1])

# Printing plot
plt.show()
