from pyscript import display
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(e):
    days = ['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']
    sold = [4, 3, 5, 7, 2, 1, 6]

    plt.figure()
    plt.plot(days, sold, marker='o', color='yellow')
    plt.title("Milk")
    plt.xlabel("Day")
    plt.ylabel(" Sold")

    display(plt.gcf(), target="output")
