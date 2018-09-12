#CSCI 1133 Homework 1
#Erik Lindeman
#Problem 1D

def absError(act, meas):
    error = act-meas
    Errorabs = abs(error)
    errorFinal = round(Errorabs, 6)
    return errorFinal

def relError(act, meas):
    ErrorRel = (abs(act-meas))/act
    errorFinal = round(ErrorRel, 6)
    return errorFinal
