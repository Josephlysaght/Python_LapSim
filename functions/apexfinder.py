import varibles
import numpy as np
import matplotlib.pyplot as plt

def apexfinder():
    acurv = abs(varibles.fcurv)
    varibles.apex = np.arange(varibles.trackpoints, dtype=float)
    num = varibles.trackpoints - 1;
    n = 0;
    mina = min(acurv);

    while n < num:
        if acurv[n] >= acurv[n-1] and acurv[n] >= acurv[n+1] and acurv[n] > mina+0.01:
            varibles.apex[n] = 1;
        else:
            varibles.apex[n] = 0;
        n = n + 1;

    varibles.apex[num] = 0
    varibles.apex[0] = 0

    steps = np.arange(varibles.trackpoints, dtype=float)
    plt.plot(steps, varibles.apex)
    plt.plot(steps, acurv)
    plt.show()
