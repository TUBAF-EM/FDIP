---
title: 'FDIP: A Python package for Frequency-Domain Induced Polarization data'
tags:
  - Python
  - spectral induced polarization
  - electrical resistivity
  - geophysics
authors:
  - name: Thomas Günther
    orcid: 0000-0001-5409-0273
    equal-contrib: true
    affiliation: "1, 2" # (Multiple affiliations must be quoted)
affiliations:
 - name: TU Bergakademie Freiberg
   index: 1
date: 07 June 2026
bibliography: paper.bib
---

# Summary

Spectral Induced Polarization observes polarization phenomena in subsurface
material and can provide valuable information about the internal structures.
While the method is routinely carried out in the laboratory, field data
acquisition is still not very common. Extensive data processing and analysis
is requires in order to attribute spectra to the subsurface.
We provide a Python-based software that allows non-programmers for quick
data analysis from the raw data to the production of paper figures.

# Statement of need

In the subsurface, various polarization mechanisms lead to frequency-dependent
conductivity that is expressed as imaginary spectrum between the injected
current and the measured voltage in the Fourier domain [@Loewer2017].
Such spectral induced polarization measurements have been carried out routinely
in the laboratory since in the last decades. Such measurements can also be done
in the field, using standard Electrical Resistivity Tomography (ERT) electrode
arrays and combinations. Subsurface imaging is done by inverting for a complex
valued conductivity for single frequencies. To this end, several open-source
software packages are available, like the Python-based Geophysical Inversion
and Modelling Library `pyGIMLi` [@Ruecker2017].

While one can do this frequency by frequency, additional stability is achieved
by inverting data of all frequencies at the same time and coupling them through
smoothness constraints not only in the spatial, but also the spectral domain.
@Guenther2016 presented such an approach and applied it to a synthetic case and
a field data set from a slag heap. In practice, data processing routines are
needed to do the individual steps of preprocessing, inversion and visualization.
`FDIP` is a convenient Python-package to do all these steps in a reproducible
way, thus allowing for Open Science publications.

# State of the field



# Software design

`Gala`'s design philosophy is based on three core principles: (1) to provide a
user-friendly, modular, object-oriented API, (2) to use community tools and
standards (e.g., Astropy for coordinates and units handling), and (3) to use
low-level code (C/C++/Cython) for performance while keeping the user interface
in Python. Within each of the main subpackages in `gala` (`gala.potential`,
`gala.dynamics`, `gala.integrate`, etc.), we try to maintain a consistent API
for classes and functions. For example, all potential classes share a common
base class and implement methods for computing the potential, forces, density,
and other derived quantities at given positions. This also works for
compositions of potentials (i.e., multi-component potential models), which
share the potential base class but also act as a dictionary-like container for
different potential components. As another example, all integrators implement a
common interface for numerically integrating orbits. The integrators and core
potential functions are all implemented in C without support for units, but the
Python layer handles unit conversions and prepares data to dispatch to the C
layer appropriately.Within the coordinates subpackage, we extend Astropy's
coordinate classes to add more specialized coordinate frames and
transformations that are relevant for Galactic dynamics and Milky Way research.

# Research impact statement

`Gala` has demonstrated significant research impact and grown both its user base
and contributor community since its initial release. The package has evolved
through contributions from over 18 developers beyond the original core developer
(@adrn), with community members adding new features, reporting bugs, and
suggesting new features.

While `Gala` started as a tool primarily to support the core developer's
research, it has expanded organically to support a range of applications across
domains in astrophysics related to Milky Way and galactic dynamics. The package
has been used in over 400 publications (according to Google Scholar) spanning
topics in galactic dynamics such as modeling stellar streams [@Pearson:2017],
Milky Way mass modeling, and interpreting kinematic and stellar population
trends in the Galaxy. `Gala` is integrated within the Astropy ecosystem as an
affiliated package and has built functionality that extends the widely-used
`astropy.units` and `astropy.coordinates` subpackages. `Gala`'s impact extends
beyond citations in research: Because of its focus on usability and user
interface design, `Gala` has also been incorporated into graduate-level galactic
dynamics curricula at multiple institutions.

`Gala` has been downloaded over 100,000 times from PyPI and conda-forge yearly
(or ~2,000 downloads per week) over the past few years, demonstrating a broad
and active user community. Users span career stages from graduate students to
faculty and other established researchers and represent institutions around the
world. This broad adoption and active participation validate `Gala`'s role as
core community infrastructure for galactic dynamics research.

# Mathematics

Single dollars ($) are required for inline mathematics e.g. $f(x) = e^{\pi/x}$

Double dollars make self-standing equations:

$$\Theta(x) = \left\{\begin{array}{l}
0\textrm{ if } x < 0\cr
1\textrm{ else}
\end{array}\right.$$

You can also use plain \LaTeX for equations
\begin{equation}\label{eq:fourier}
\hat f(\omega) = \int_{-\infty}^{\infty} f(x) e^{i\omega x} dx
\end{equation}
and refer to \autoref{eq:fourier} from text.

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# AI usage disclosure

No generative AI tools were used in the development of this software, the writing
of this manuscript, or the preparation of supporting materials.

# Acknowledgements

We thank Tina Martin for providing field data and fruitful discussions.

# References

