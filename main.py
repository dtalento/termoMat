import matplotlib.pyplot as plt
import numpy as np
import pyromat as pm
from js import console, window, document # type: ignore
from pyscript import display # type: ignore

unitDict = {'T':'°C', 'p':'kPa', 'u':'kJ/kg', 'h':'kJ/kg', 's':'kJ/(kgK)'}
pm.config['unit_pressure'] = 'kPa'
pm.config['unit_temperature'] = 'C'
sust = pm.get('mp.H2O')

dataContainer = document.querySelector('#data-container')
dataContainer.innerText = 'Choose Things'

# p = np.linspace(rangeMin, rangeMax, 100)
# h = sust.h(p=p, x=1)
fig1, ax1 = plt.subplots()
# ax1.plot(h, p)

def formatOutput(input, outNames, DATA):
    varUnit =   input['varUnit']
    fixedName = input['fixedName']
    fixedValue =input['fixedValue']
    fixedUnit = input['fixedUnit']
    
    step = input['step']

    formattedOutput = f"<theader><th colspan=4>{fixedName} = {fixedValue} {fixedUnit}</th></theader>"
    
    formattedOutput += f"<tr>"
    for name in outNames:
        formattedOutput += f"<th>{name}({unitDict[name]})"
    formattedOutput += "</tr>"
    
    for i in range(step):
        newrow = "<tr>"
        for name in outNames:
            newrow += f"<td>{DATA[name][i]}</td>"
        newrow += "</tr>"
        formattedOutput += newrow
    return str(formattedOutput)

def getVarT(T, varName, min, max, step):
    match varName:
        case 'T':
            raise Exception('Invalid Input')
        case 'p':
            p = np.linspace(min, max, step)
            u = sust.e(T=T, p=p)
            h = sust.h(T=T, p=p)
            s = sust.s(T=T, p=p)
        case 'u':
            u = np.linspace(min, max, step)
            p = sust.p(T=T, e=u)
            h = sust.h(T=T, e=u)
            s = sust.s(T=T, e=u)
        case 'h':
            h = np.linspace(min, max, step)
            p = sust.p(T=T, h=h)
            u = sust.e(T=T, h=h)
            s = sust.s(T=T, h=h)
        case 's':
            s = np.linspace(min, max, step)
            p = sust.p(T=T, s=s)
            u = sust.e(T=T, s=s)
            h = sust.h(T=T, s=s)
        case other:
            raise Exception('PYROMAT ERROR')   
    return p, u, h, s

def getVarP(p, varName, min, max, step):
    match varName:
        case 'p':
            raise Exception('Invalid Input')
        case 'T':
            T = np.linspace(min, max, step)
            u = sust.e(p=p, T=T)
            h = sust.h(p=p, T=T)
            s = sust.s(p=p, T=T)
        case 'u':
            u = np.linspace(min, max, step)
            T = sust.T(p=p, e=u)
            h = sust.h(p=p, e=u)
            s = sust.s(p=p, e=u)
        case 'h':
            h = np.linspace(min, max, step)
            T = sust.p(p=p, h=h)
            u = sust.e(p=p, h=h)
            s = sust.s(p=p, h=h)
        case 's':
            s = np.linspace(min, max, step)
            T = sust.p(p=p, s=s)
            u = sust.e(p=p, s=s)
            h = sust.h(p=p, s=s)
        case other:
            raise Exception('PYROMAT ERROR')   
    return T, u, h, s

def getData(input):
    varName =   input['varName']
    min = input['min']
    max = input['max']
    step = input['step']
    varUnit =   input['varUnit']
    fixedName = input['fixedName']
    fixedValue =input['fixedValue']
    fixedUnit = input['fixedUnit']

    match fixedName:
        case 'T':
            T = fixedValue*np.ones(step)
            p, u, h, s = getVarT(fixedValue, varName, min, max, step)
        case 'p':
            p = fixedValue*np.ones(step)
            T, u, h, s = getVarP(fixedValue, varName, min, max, step)
        case other:
            raise Exception('INVALID PROPERTY')

    DATA = {'T':T, 'p':p, 'u':u, 'h':h, 's':s}

    return DATA

def getInputs():
    pptyVariable = document.querySelector('#ppty-variable').value
    pptyFixed = document.querySelector('#ppty-fixed').value

    rangeMax = float(document.querySelector('#range-max').value)
    rangeMin = float(document.querySelector('#range-min').value)
    step = int(document.querySelector('#step').value)
    fixedValue = float(document.querySelector('#fixed-value').value)
    
    inputData = {'varName':pptyVariable, 'varUnit':unitDict[pptyVariable], 'fixedName':pptyFixed, 'fixedUnit':unitDict[pptyFixed], 'max':rangeMax, 'min':rangeMin, 'step':step, 'fixedValue':fixedValue}
    return inputData
def testBtn():
    try:
        input = getInputs()
    except:
        dataContainer.innerHTML = "<p>Invalid Input</p>"
    else:    
        try:
           DATA = getData(input)
        except Exception as error:
           dataContainer.innerHTML = error
        else:
            outNames = ['T', 'p', 'u', 'h', 's']
            outNames.remove(input['varName'])
            outNames.remove(input['fixedName'])
            outNames.insert(0, input['varName'])
            dataContainer.innerHTML = formatOutput(input, outNames, DATA)
            # display(fig1, target='test-output', append=False)
            pass