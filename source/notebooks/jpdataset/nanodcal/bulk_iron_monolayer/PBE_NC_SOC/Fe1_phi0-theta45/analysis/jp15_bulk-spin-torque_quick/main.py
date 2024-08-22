import numpy as np
import junpy as jp
from junpy.factory import nanodcal

#==============================================================================

filename = '../../NanodcalStructObject.mat'
device = nanodcal.load_nanodcal_device(filename)

#==============================================================================

calc = jp.calculation.BulkSpinTorque(
    device=device,
    kpoints=jp.UniformKspaceSampling(
        gridNumber=(2,3,1),
        isTimeReversalSymmetry=False,
    ),
    equilibriumEnergies=dict(
        circlePoints=4,
        lowestEnergy=-30,
    ),
    etaGF=1e-2,
    chemicalPotential=device.hsdata.fermiEnergy,
    spinAccumulationDetail=True,
)
jp.run(calc)

#==============================================================================

