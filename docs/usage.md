# Usage

The fdip package holds some functions for importing, modelling and inverting tomographic spectral IP data measured in the frequency domain, based upon [pyGIMLi](https://pygimli.org).
Single-frequency modelling and inversion is completely included in pyGIMLi, so this repository adds up for exploiting the spectral information.

Main entry is the class FDIP, to be imported by

```python
from fdip import FDIP
```

It can be initialized empty or directly with a data file

```python
pro = TDIP("datafile.ohm")
```

Valid formats are:

* ERT scheme set accompagnied by .RHOA/.PHIA files
* Radic RES file from SIP256C or D
* MPT DAS-1
* single files holding individual frequencies

You can also create an empty instance and use `pro.load(filename)`.

As a result, the instance holds an ERT data file `pro.data`and matrices of apparent resistivity `pro.RHOA`) and phase ( `pro.PHIA`).

You can add other files by `pro.addData(filename)`

## Preprocessing

Most important preprocessing tool is `pro.filter()`.
It works either along the data sequence axis (like `data.remove()`) or along the time axis and removes complete data (including all gates) or gates (for all data).
Important keywords are

```python
nr=[], # list of numbers
fmin=0, fmax=1e9, # minimum/maximum frequency
kmax=1e6, # maximum geometric factor
forward=False, # keep only forward measurements
electrode=None, ab=None, mn=None, # electrodes (combinations)
```

If you don't want to remove the whole data point, but only disregard some erroneous data (like outliers), you can mask these using `.mask()` with the keywords
```python
rhomin=0, rhomax=9e99, # min/max app res.
phimin=-9e99, phimax=9e99 # min/max app. phase
```
You can also mask the whole decay by `filter(..., mask=True)` in order to not to loose the apparent resistivity information.

You can generate synthetic data assuming a Cole-Cole model by using
```python
pro.simulate(mesh, rhovec, mvec, tauvec, cvec)
```
where rhovec, mvec, tauvec, cvec are vectors pointing into the different regions of the mesh

`.getDataSpectrum()`

`.showSingleFrequencyData`

`.showAllFrequencyData`

`.generateDataPDF()`

`.showDataSpectrum()`

`.generateSpectraPDF()`

`.removeEpsilon()`

## Inversion

`pro.singleInversion()`

This triggers an `ERTIPManager()` to which you can pass all options.

`pro.showSingleResult` shows the result

To invert all frequencies sequentially, use
`pro.individualInversion()`
or simultaneously, use
`pro.simultaneousInversion()`
which in turn calls
`pro.simultaneousRestivityInversion()`
and
`pro.simultaneousPhaseInversion()`


There is a special inversion into Debye models for every cell.
`pro.invertDebye()`

Class instances can be accessed by `pro.ERT`, `pro.invIP`

## Postprocessing

As a result of apparent chargeability inversion, you have a matrix of resistivities `pro.RES` and phases `pro.PHI` for every model cell, matching the inversion mesh `pro.pd`.

`.showModelSpectrum()` plots the inverted spectrum for a certain position (and `showModelSpectra` for a list of them), whereas `.getModelSpectrum()` returns a pyGIMLi SIP `Spectrum` class instance which then can be further analysed.

`.fitAllRhoPhi()` fits both resistivity and phase, whereas `.fitAllPhi()` fits only phases

As a result, you obtain a Cole-Cole model for every cell, whose parameter can be show with `showColeColeParameters`.

`saveFigures()`

`saveResults()`

`loadResults()`

so that you can do postprocessing independent of inversion by

```python
pro = FDIP(filename)
pro.loadResults()
...
```

## Working in 3D

While visualization is designed for 2D profiles, numerical computations should work in 3D as well, provided a 3D mesh is created for the ERT manager.

## Conversion to TD

`convertToTD()` converts the whole data set to a time-domain instance `TDIP` through Debye decomposition (package TDIP required).
