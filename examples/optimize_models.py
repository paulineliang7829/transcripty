"""
Example file
------------

This file illustrates how one could use the `calibrateCPM` and
`calibrateHPM` functions to try to find the best parameters for
the two models
"""
import transcripty as t


# Run the calibration function for common probability model
cparams, trace = t.data.calibrateCPM(nevals=1500)

print("The best calibration found for the common probability model is")
print(cparams)

# Run the calibration function for common probability model
hparams, trace = t.data.calibrateHPM(nevals=2500)

print("The best calibration found for the heterogeneous probability model is")
print(hparams)

