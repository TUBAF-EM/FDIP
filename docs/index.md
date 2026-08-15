# Frequency-Domain Induced-Polarization (FDIP) data processing

Formerly part of [BERT](https://gitlab.com/resistivity-net/bert) repository, but since 2026 independent.
The code is based upon pyGIMLi (Rücker et al. 2017) and its ERT module based on Günther et al. (2006).
Whereas the ERT module only includes only single-frequency (or chargeability) inversion, the spectral induced polarization (SIP) in the frequency domain. For time domain SIP, please use [TDIP](https://github.com/TUBAF-EM/TDIP)

For details and examples, we refer to the papers of Günther & Martin (2016) describing the methodology, Martin et al. (2020) comparing with time domain, Martin et al. (2021) for application to slag heaps, and the accompanying data sets with codes at Zenodo (e.g. [Martin2020 data](https://doi.org/10.5281/zenodo.4419735)).

## References

* Günther, T. & Martin, T. (2016): Spectral two-dimensional inversion of frequency-domain induced polarisation data from a mining slag heap. Journal of Applied Geophysics 135, 436-448, [doi:10.1016/j.jappgeo.2016.01.008](https://doi.org/10.1016/j.jappgeo.2016.01.008).
* Martin, T., Günther, T., Orozco, A.F. & Dahlin, T. (2020): Evaluation of spectral induced polarization field measurements in time and frequency domain, J. Appl. Geophys. 180, 104141, [doi:10.1016/j.jappgeo.2020.104141](https://doi.org/10.1016/j.jappgeo.2020.104141).
* Martin, T., Günther, T., Weller, A. & Kuhn, K. (2021): Classification of slag material by spectral induced polarization laboratory and field measurements. J. Appl. Geophys. 194, 104439, [doi:10.1016/j.jappgeo.2021.104439](https://doi.org/10.1016/j.jappgeo.2021.104439).
* Rücker, C., Günther, T., Wagner, F.M. (2017): pyGIMLi: An open-source library for modelling and inversion in geophysics, Computers & Geosciences 109, 106-123, [doi:10.1016/j.cageo.2017.07.011](http://doi.org/10.1016/j.cageo.2017.07.011).
* Günther, T., Rücker, C. & Spitzer, K. (2006): Three-dimensional modeling and inversion of dc resistivity data incorporating topography – II: Inversion. Geophys. J. Int. 166, 506-517, [doi:10.1111/j.1365-246X.2006.03011.x](https://doi.org/10.1111/j.1365-246X.2006.03011.x).
* Rücker, C., Günther, T. & Spitzer, K. (2006): Three-dimensional modeling and inversion of dc resistivity data incorporating topography – I: Modeling. Geophys. J. Int. 166, 495-505, [doi:10.1111/j.1365-246X.2006.03010.x](https://doi.org/10.1111/j.1365-246X.2006.03010.x).