import varibles
import numpy as np
import matplotlib.pyplot as plt

def apexfinder():
    acurv = abs(varibles.fcurv)
    varibles.apex = np.zeros(varibles.trackpoints, dtype=float)
    num = varibles.trackpoints - 1;
    n = 0;
    mina = min(acurv);

    while n < num:
        preapex = varibles.apex[n]+varibles.apex[n-1]+varibles.apex[n-2];
        if acurv[n] >= acurv[n-1] and acurv[n] >= acurv[n+1] and acurv[n] > mina+0.01 and preapex < 0.9:
            varibles.apex[n] = 1;
        else:
            varibles.apex[n] = 0;
        n = n + 1;

    varibles.apex[num] = 0
    varibles.apex[0] = 0

    steps = np.arange(varibles.trackpoints, dtype=float)
    plt.plot(steps, varibles.apex)
    plt.plot(steps, varibles.fcurv)
    plt.show()

    del num,n,mina,acurv,steps;