import matplotlib.pyplot as plt
import numpy as np
import pyromat as pm
from js import console, window, document # type: ignore
from pyscript import display # type: ignore

pm.config['unit_pressure'] = 'kPa'
pm.config['unit_temperature'] = 'K'
sust = pm.get('mp.H2O')

outputDiv = document.querySelector('#test-output')
outputDiv.innerText = 'Choose Things'

# p = np.linspace(rangeMin, rangeMax, 100)
# h = sust.h(p=p, x=1)
fig1, ax1 = plt.subplots()
# ax1.plot(h, p)

def formatOutput(vec1, vec2):
    output = "#\tP(kPa)"
    i = 0
    for value in vec1:
        newrow = f"\nN = {i}\tN + 1 = {i+1}"
        output += newrow
        console.log(newrow)
    return str(output)

def testBtn():
    pptyVariable = document.querySelector('#ppty-variable')
    pptyFixed = pptyVariable = document.querySelector('#ppty-fixed')

    rangeMax = float(document.querySelector('#range-max').value)
    rangeMin = float(document.querySelector('#range-min').value)
    step = int(document.querySelector('#step').value)
    fixedValue = float(document.querySelector('#fixed-value').value)

    p = np.linspace(rangeMin, rangeMax, step)
    outputDiv.innerText = formatOutput(p, p)
    # display(fig1, target='test-output', append=False)
