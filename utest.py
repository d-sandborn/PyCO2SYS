import PyCO2SYS as pyco2

par1 = 2300
par2 = 2150
par1type = 1
par2type = 2
sal = 32
tempin = 10
tempout = 20
presin = 0
presout = 1000
si = 10
phos = 3
nh3 = 1
h2s = 0.5
phscale = 1
k1k2c = 10
kso4c = 3
kfc = 1

co2dict = pyco2.CO2SYS(par1, par2, par1type, par2type, sal, tempin, tempout,
                       presin, presout, si, phos, phscale, k1k2c, kso4c,
                       KFCONSTANT=kfc)

Uncert = pyco2.engine.uCO2SYS(co2dict, uncertainties={
    "PAR1": [],
    "PAR2": [],
    })
