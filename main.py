import matplotlib.pyplot as plt
import numpy as np
import pyromat as pm
from js import console, window, document # type: ignore
from pyscript import display # type: ignore

pm.config['unit_pressure'] = 'kPa'
pm.config['unit_temperature'] = 'K'
sust = pm.get('mp.H2O')

dataContainer = document.querySelector('#data-container')
dataContainer.innerText = 'Choose Things'

# p = np.linspace(rangeMin, rangeMax, 100)
# h = sust.h(p=p, x=1)
fig1, ax1 = plt.subplots()
# ax1.plot(h, p)

def formatOutput(vec1, vec2):
    output = "#\tP(kPa)"
    i = 0
    for value in vec1:
        i += 1
        newrow = f"\nN = {i}\t\t\tp = {value}"
        output += newrow
    return str(output)

def testBtn():
    pptyVariable = document.querySelector('#ppty-variable')
    pptyFixed = document.querySelector('#ppty-fixed')

    rangeMax = float(document.querySelector('#range-max').value)
    rangeMin = float(document.querySelector('#range-min').value)
    step = int(document.querySelector('#step').value)
    fixedValue = float(document.querySelector('#fixed-value').value)

    p = np.linspace(rangeMin, rangeMax, step)
    dataContainer.innerText = formatOutput(p, p)
    # display(fig1, target='test-output', append=False)
