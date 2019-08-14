import varibles
import numpy as np
import math
from scipy import signal

def calccur():
    i = 0
    end = varibles.trackpoints - 1
    varibles.curvature = np.arange(varibles.trackpoints, dtype=float)
    varibles.yawsign = np.arange(varibles.trackpoints, dtype=float)

    varibles.yawsign[1] = (varibles.racing_liney[1] - varibles.racing_liney[end]) / (
                varibles.racing_linex[1] - varibles.racing_linex[end]);
    varibles.yawsign[end] = (varibles.racing_liney[end] - varibles.racing_liney[end - 1]) / (
                varibles.racing_linex[end] - varibles.racing_linex[end - 1]);

    while i < end:
        varibles.yawsign[i] = (varibles.racing_liney[i] - varibles.racing_liney[i - 1]) / (
                    varibles.racing_linex[i] - varibles.racing_linex[i - 1]);
        a = math.sqrt((varibles.racing_linex[i + 1] - varibles.racing_linex[i - 1]) ** 2 + (
                    varibles.racing_liney[i + 1] - varibles.racing_liney[i - 1]) ** 2);
        b = math.sqrt((varibles.racing_linex[i + 1] - varibles.racing_linex[i]) ** 2 + (
                    varibles.racing_liney[i + 1] - varibles.racing_liney[i]) ** 2);
        c = math.sqrt((varibles.racing_linex[i] - varibles.racing_linex[i - 1]) ** 2 + (
                    varibles.racing_liney[i] - varibles.racing_liney[i - 1]) ** 2);
        A = abs(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)));

        varibles.curvature[i] = (2 * math.sin(math.pi - A)) / a;
        i = i + 1

    varibles.curvature[end] = 0
    varibles.curvature[0] = 0

    varibles.YawDer = np.gradient(varibles.yawsign);
    varibles.curvature = np.sign(varibles.YawDer) * varibles.curvature;

    b1, a1 = signal.butter(2, 0.05, 'low');
    varibles.fcurv = signal.filtfilt(b1, a1, varibles.curvature)

    del i,b,a,c,A,end,b1,a1;





