---
comments: true
---

# Extragalactic X-ray Binary Catalog
Extragalactic X-ray Binary Catalog described in Inoue, Yabe, &amp; Ueda 2021 PASJ

## Introduction
We construct a new catalog of extragalactic X-ray binaries (XRBs) utilizing the latest Chandra, XMM-Newton, and Swift X-ray source catalogs by matching with the local galaxy catalogs. Our fiducial catalog including Chandra sources only contains 4430 XRBs hosted by 237 galaxies within ~130 Mpc. Utilizing the latest XMM-Newton, and Swift X-ray source catalog data sets, additional XRB candidates are also found resulting in 5757 XRBs hosted by 311 galaxies.

## Catalog Download

- Main Catalog (Chandra data only)
  - [FITS](../files/data/exrb_catalog_CSC2_compact.fits)/[Ascii](../files/data/exrb_catalog_CSC2_compact.dat)
  - Used for XRB XLF construction in the paper.
  
- Full Catalog (Chandra, XMM-Newton, & Swift data)
  - [FITS](../files/data/exrb_catalog_CXS_compact.fits)/[Ascii](../files/data/exrb_catalog_CXS_compact.dat)
  
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
D25|arcmin|Major angular diameter of the host galaxy|
b/a||Axial ratio of the host galaxy|
PA|deg|Position angle of the host galaxy|
Morphology||Morphology of the host galaxy, defiend by de vvv|
 Distance|Mpc|Distance to the host galaxy|
 SFR|$$M_\odot/{\rm yr}$$|Star formation rate of the host galaxy|
 Stellar_Mass|$$M_\odot$$|Stellar mass of the host galaxy|
 Galaxy_Catalog||Identification of the parent galaxy catalog. LVG: _LVG_ Catalog, IRAS: _IRAS_ Catalog|

 
## Contact
If you have any queries, please contact me freely.

