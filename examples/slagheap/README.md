# Field data example

This example uses the field FDIP data published by Günther & Martin (2016)
and Martin et al. (2021). It consists of three parts (and thus notebooks):

1. Pre-processing of data including filtering, limiting frequency content &
single-frequency inversion,
2. Simultaneous (spectrally constrained) inversion of whole data set after
Günther & Martin (2016) and fitting of Cole-Cole model,
3. Post-processing result by extracting spectra and computing imaginary
conductivity for low, medium & high frequency (Martin et al. 2021).

Although all could be done in one script, it saves filtered data and
inversion result so that each process can be treated separately.

## References

* Günther, T. & Martin, T. (2016): Spectral two-dimensional inversion of frequency-domain induced polarisation data from a mining slag heap. Journal of Applied Geophysics 135, 436-448, [doi:10.1016/j.jappgeo.2016.01.008](https://doi.org/10.1016/j.jappgeo.2016.01.008).
* Martin, T., Günther, T., Weller, A. & Kuhn, K. (2021): Classification of slag material by spectral induced polarization laboratory and field measurements. J. Appl. Geophys. 194, 104439, [doi:10.1016/j.jappgeo.2021.104439](https://doi.org/10.1016/j.jappgeo.2021.104439).
