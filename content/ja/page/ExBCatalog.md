---
comments: true
---

# Extragalactic X-ray Binary Catalog   
Inoue & Yabe in prep. 

## Introduction
We construct a new catalog of extragalactic X-ray binaries (ExB) utilizing the latest Chandra, XMM-Newton, and Swift X-ray source catalogs by matching with the local galaxy catalogs. Our ExB catalog contains 9314 XRBs hosted by 417 galaxies, which is the largest ever XRB catalog. 

## Catalog Download

- Compact Object Catalog (Main Catalog)
  - [FITS](../files/data/ExB_Catalog_CXS_compact.fits)/[Ascii](../files/data/ExB_Catalog_CXS_compact.dat)
## Table Description
  Column Name| Unit|Note|
------------------:|  -----:  |---|
Name_XRB||Source name|
RA|deg|Right ascension of the source|
DEC|deg|Declination of the source|
L_X_2_10|erg/s|2-10 keV luminosity|
Satellite||ID of the satellite which measured the source. C: _Chandra_, X: _XMM-Newton_, S: _Swift_/XRT|
Name_Host||Host galaxy name|
RA_Host|deg|Right ascension of the host galaxy|
DEC_Host|deg|Declination of the host galaxy|
a26|arcmin|Major angular diameter of the host galaxy|
b/a||Axial ratio of the host galaxy|
PA|deg|Position angle of the host galaxy|
Morphology||Morphology of the host galaxy, defiend by de vvv|
 Distance|Mpc|Distance to the host galaxy|
 SFR|$$M_\odot/{\rm yr}$$|Star formation rate of the host galaxy|
 Stellar_Mass|$$M_\odot$$|Stellar mass of the host galaxy|
 Galaxy_Catalog||Identification of the parent galaxy catalog. LVG: _LVG_ Catalog, IRAS: _IRAS_ Catalog|

 
 ## Extended Source Catalog
 We also provide the extended source list. As they are classified as the extended objects, most are not XRBs. However, some could be XRBs. If you use this catalog, careful check is appreciated. The table description is the same as the main catalog.
 - Extended Object Catalog
   - [FITS](../files/data/ExB_Catalog_CXS_extended.fits)/[Ascii](../files/data/ExB_Catalog_CXS_extended.dat)
 
## Contact
If you have any queries, please contact me freely.

