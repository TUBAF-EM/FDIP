# FDIP
Frequency-Domain Induced-Polarization data processing

Formerly part of BERT repository, the theory behind the heart, spectral inversion, is described by Günther & Martin (2016).
The code is based upon pyGIMLi (Rücker et al. 2017) and its ERT module and uses complex-valued forward modelling and inversion.
For usage, we refer to Martin et al. (2020) and the accompagnying Zenodo data sets with codes.

To use the package and keep updated, just

1. `git clone` the repository and go to its location with bash, PowerShell etc.
2. install the code editable by `pip install -e .`
3. Update at any later time by `git pull` (no further step needed)

## References

* Günther, T. & Martin, T. (2016): Spectral two-dimensional inversion of frequency-domain induced polarisation data from a mining slag heap. Journal of Applied Geophysics 135, 436-448, [doi:10.1016/j.jappgeo.2016.01.008](https://doi.org/10.1016/j.jappgeo.2016.01.008).

* Martin, T., Günther, T., Orozco, A.F. & Dahlin, T. (2020): Evaluation of spectral induced polarization field measurements in time and frequency domain, J. Appl. Geophys. 180, 104141, [doi:10.1016/j.jappgeo.2020.104141](https://doi.org/10.1016/j.jappgeo.2020.104141).

* Rücker, C., Günther, T., Wagner, F.M. (2017): pyGIMLi: An open-source library for modelling and inversion in geophysics, Computers & Geosciences 109, 106-123, [doi:10.1016/j.cageo.2017.07.011](http://doi.org/10.1016/j.cageo.2017.07.011).
