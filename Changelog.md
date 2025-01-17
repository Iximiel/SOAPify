# Changelog

Until we get to a release version you may encounter different broken interface problem each time we increase a minor version.

## Changes since v0.1.0rc0

- `SOAPify.HDF5er.isTrajectoryGroup` now returns `False` with Datasets
- Added some simple cli interfaces
- Added examples for LENS and tSOAP and for generating hdf5 files
- Added `getSOAPSettings()` for getting the SOAP organization from a hdf5 dataset
- Added `getTimeSOAPSimple()` to give the user a shortcut to solve memory problem with large SOAP datasets
- Now `createUniverseFromSlice()` returns also types
- added precision selection for storing the trajectories and the SOAP fingerprints

## Changes since v0.0.6

- The **v0.0.6** has been set flagged as the 'stable version'
- Forced **float64** precision in most of the calculations &larr; **THIS IS A MAJOR CHANGE AND COULD IMPACT YOUR RESULTS**
- Changed the package name to cpctools, for storing it on https://pypi.org/
- Removed the old and unused procedure for calculating the references
- Compacted the workflows for a PR
- Added the coveralls.io badge
- Now documentation in rtd uses the standard rtd workflow
- Refactored of the transition submodules, now support the 'window' and 'stride' concepts, added an entry to the documentation to explain it
- Now `saponifyMultipleTrajectories` calls `saponifyTrajectory`
- Moved HDF5er into SOAPify, to simplify the deployment
    - change your `import HDF5er` to `import SOAPify.HDF5er as HDF5er` in your old codes
    - `HDF5er.HDF5erUtils` &rarr; `SOAPify.HDF5er.HDF5erUtils`
    - `HDF5er.HDF5To` &rarr; `SOAPify.HDF5er.HDF5To`
    - `HDF5er.ToHDF5` &rarr; `SOAPify.HDF5er.ToHDF5`
- renamed some submodules to clarify the usage:
    - `SOAPify.SOAPbase` &rarr; `SOAPify.distances`
    - `SOAPify.SOAPengine` &rarr; `SOAPify.engine`
    - `SOAPify.SOAPclassify` &rarr; `SOAPify.classify`
    - `SOAPify.SOAPTransitions` &rarr; `SOAPify.transitions`
    - `SOAPify.Saponify` &rarr; `SOAPify.saponify`
- renamed some functions to avoid naming collision, and to be more clear:
    - `SOAPify.SOAPclassify.classify()` &rarr; `SOAPify.classify.applyClassification()`
    - `SOAPify.Saponify.saponifyGroup()` &rarr; `SOAPify.saponify.saponifyMultipleTrajectories()`
    - `SOAPify.Saponify.saponify()` &rarr; `SOAPify.saponify.saponifyTrajectory()`
    - `SOAPify.SOAPTransitions.normalizeMatrix()` &rarr; `SOAPify.transitions.normalizeMatrixByRow()`
    - `SOAPify.SOAPbase.KernelSoap()` &rarr; `SOAPify.distances.kernelSoap()`
    - `SOAPify.RemoveAtomIdentityFromEventTracker()` &rarr; `SOAPify.transitions.saponifyTrajectory()`
- Cleaned the code with pylint
- Added LENS and tempoSOAP base functions


## Changes since v0.0.4

- Increased test coverage
- Now if the box changes in a mda.Universe the ToHDF5 method saves it correctly
- set quippy-ase compatibility to 0.9.10
- Now tests prevents error in merging references
- Checked and added python 3.10 compatibility

## Changes since v0.0.3

- `getXYZfromTrajGroup` now accept IO objects as inputs
- **WARNING**: broken interface for `getXYZfromTrajGroup`, now it needs 3 inputs and the first is a file-like object
- `saveXYZfromTrajGroup` and `getXYZfromTrajGroup` now can export comments per frames
- `transitionMatrixFromSOAPClassification` now creates matrix with shape  `(n,n)` and no more `(n+1,n+1)`, where `n` is the lenght of the legend. The user will now need to address the errors in the legend, if needed
- added `calculateResidenceTimesFromClassification` for calculating the residence times of the states during the MD
- added `trackStates` for calculating the history of the evolution of the states in the MD
- the result of `trackStates` can be used for calculating the residence times and the transition matrices
- Now when appliyng soap, the created dataset will be given attributes that describe the parameters used for its creation
- Removed some default values in function from Saponify and fillSOAPVectorFromdscribe
- fillSOAPVectorFromdscribe now can fill soap vectors from multispecies calculations
- changed slightly `saponifyGroup` and `saponify`: now they accept dscribe SOAP options as a dictionary, but not the sparse option
- Now HDFTo.getXYZfromTrajGroup accepts slices as an option to export the trajectory
- **WARNING**: broken interface for saponify
- `isTrajectoryGroup` added to HDF5er to check if a group contain a trajectory in our format
- now it is possible to select 'quippy' for calculating SOAP
- tests reahul
- fillSOAPVectorFromdscribe now is between 10 to 20 times faster than before
- now name of the used engine is stored in the hdf5 file's SOAP dataset
- added a small utility to make the nmax/lmax/rcut getter work regardless the compatible dscribe engine
- now installation procedure ignores dscribe/quippy: you should install them separately, but you do not need to wait for their compilation if you only need the analysis features
- created `getXYZfromMDA` for exporting exyz files (with personalized header and columns) from mda universe
- removed a bug in `getXYZfromHDF5`: now boxes are exported correctly
- some QoL improvements behind the curtains and in the tests
- added CI for documentation
- merged `src/HDF5er/MDA2HDF5.py` and `src/HDF5er/ase2HDF5.py` into `src/HDF5er/ToHDF5.py`
- Heavy changes in the documentation
- Now the documentation coverage should work
- Documentation now should also be hosted by readthedocs.io

## Changes since v0.0.2a

- Only for Monospecies systems: added a small utility (`fillSOAPVectorFromdscribe`) that returns the complete SOAP vector from the simplified one from dscribe
- Added a utility for normalize SOAP vectors
- Added `createReferencesFromTrajectory` that creates a variables that stores SOAP references
- set up a way to classify with soap with a different method thant the original idea
- the new references now can be loaded/unloaded on an hdf5 file
- added a patch for hdf5 imported files: workaround for mda not loading correctly non orthogonal boxes from lammps dumps

## Changes since v0.0.2

- Added the possiblity to export xyz files from the hdf5 trajectories, also with extra data columns
- Improved performance for getXYZfromTrajGroup

## Changes since v0.0.1

- Tests
- Changed default imports for HDF5er
- Adding override option to HDF5er.MDA2HDF5
- Added 3rd neighbours in the References
- Added attributes to HDF5er.MDA2HDF5
- In the referenceMaker: added the possibility to choose lmax and nmax for SOAP
- Added the possibility to export to hdf5 slices of the trajectories
