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

def formatOutput(varName, fixedName, vec1, fixedValue):
    output = f"<theader><th colspan=4>{fixedName} = {fixedValue}</th></theader>"
    output += "<tr><th>-</th> <th>P(kPa)</th> <th>-</th><th>-</th></tr>"
    i = 0
    for value in vec1:
        i += 1
        newrow = f"<tr><td>-</td> <td>{value}</td> <td>-</td> <td>-</td> </tr>"
        output += newrow
    return str(output)

def getInputs():
    pptyVariable = document.querySelector('#ppty-variable').value
    pptyFixed = document.querySelector('#ppty-fixed').value

    rangeMax = float(document.querySelector('#range-max').value)
    rangeMin = float(document.querySelector('#range-min').value)
    step = int(document.querySelector('#step').value)
    fixedValue = float(document.querySelector('#fixed-value').value)
    
    inputData = {'varName':pptyVariable, 'fixedName':pptyFixed, 'max':rangeMax, 'min':rangeMin, 'step':step, 'fixedValue':fixedValue}
    return inputData
def testBtn():
    try:
        input = getInputs()
    except:
        dataContainer.innerHTML = "<p>Invalid Input</p>"
    else:    
        rangeMin = input['min']
        rangeMax = input['max']
        step = input['step']

        p = np.linspace(rangeMin, rangeMax, step)
        dataContainer.innerHTML = formatOutput(input['varName'], input['fixedName'], p, input['fixedValue'])
        # display(fig1, target='test-output', append=False)
