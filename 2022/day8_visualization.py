import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import day8
import requests


res = requests.get("https://google.com")


day8.check_distance()

with open("day8.input", "r") as file:
    data = file.read().strip().split("\n")


forrest = []
for d in data:
    forrest.append([j for j in d])

arr = np.array(forrest, dtype=float)

ax = sns.heatmap(arr)
plt.show()
