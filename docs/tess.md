# TESS Objects of Interest Table Data Columns

The TESS Objects of Interest (TOI) table lists parameters currently available for the objects of interest identified by the Transiting Exoplanet Survey Satellite Project. These parameters are displayed in the [TOI interactive table](/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=TOI).

The TOI list on the NASA Exoplanet Archive is updated approximately once a week based on the ExoFOP-TESS TOI list. Because the TOIs, and their associated parameters, are continually being updated by the Project and Community on the [ExoFOP-TESS site](https://exofop.ipac.caltech.edu/tess/view_toi.php), the Exoplanet Archive list may be slightly out of sync with the ExoFOP.

**Skip to a section:**

- [TESS Objects of Interest Table Data Columns](#tess-objects-of-interest-table-data-columns)
  - [TESS Identification Columns](#tess-identification-columns)
  - [Position Columns](#position-columns)
  - [Planet Properties Columns](#planet-properties-columns)
  - [Stellar Properties Columns](#stellar-properties-columns)
  - [Dates Columns](#dates-columns)

## TESS Identification Columns

| Database<br />Column Name | Table Label | Description | Uncertainties Column<br />(positive +)<br />(negative -) | Limit Column |
| :--- | :--- | :--- | :--- | :--- |
| toi† | TESS Object of Interest | A number used to identify and track a TESS Object of Interest (TOI). TOIs are identified and numbered by the TESS Project. A TOI name has an integer and a decimal part of the format TOI-NNNNN.DD. The integer part designates the target star; the two-digit decimal part identifies a unique transiting object associated with that star. | | |
| toipfx | TESS Object of Interest Prefix | The integer portion of the TOI Identifier, designating the target star. (See toi description above.) | | |
| tid† | TESS Input Catalog ID | Target identification number, as listed in the [TESS Input Catalog (TIC)](https://ui.adsabs.harvard.edu/abs/2019arXiv190510694S/abstract). | | |
| ctoi_alias | Community TESS Object of Interest Alias | A number used to track and identify objects of interest identified by the TESS project and by the community. This number has an integer and a decimal part, where the integer is the TESS Input Catalog (TIC) ID of the target star, and the two-digit decimal part identifies a unique transiting object associated with that star. | | |
| pl_pnum | Number of Planet Candidates | Number of planet candidates in the planetary system. | | |
| tfopwg_disp† | TFOPWG Disposition | TESS Follow-up Observing Program Working Group (TFOPWG) Dispostion:<br /> **APC**=ambiguous planetary candidate<br /> **CP**=confirmed planet <br /> **FA**=false alarm<br /> **FP**=false positive<br /> **KP**=known planet<br /> **PC**=planetary candidate<br /> | | |

† Default column: these columns display in the interactive table when the table is first loaded, and when **Reset Filters** is clicked.

## Position Columns

| Database<br />Column Name | Table Label | Description | Uncertainties Column<br />(positive +)<br />(negative -) | Limit Column |
| :--- | :--- | :--- | :--- | :--- |
| rastr† | RA [sexagesimal] | Right ascension of the planetary system in sexagesimal. | (+) rastrerr1 <br /> (-) rastrerr2 | |
| ra | RA [deg] | Right Ascension of the planetary system in decimal degrees. | | |
| decstr† | Dec [sexagesimal] | Declination of the planetary system in sexagesimal. | (+) decstrerr1 <br /> (-) decstrerr2 | |
| dec | Dec [deg] | Declination of the planetary system in decimal degrees. | | |
| st_pmra† | PMRA [mas/yr] | Angular change in right ascension over time as seen from the center of mass of the Solar System. | (+) st_pmraerr1 <br /> (-) st_pmraerr2 | st_pmralim |
| st_pmdec† | PMDec [mas/yr] | Angular change in declination over time as seen from the center of mass of the Solar System. | (+) st_pmdecerr1 <br /> (-) st_pmdecerr2 | st_pmdeclim |

† Default column: these columns display in the interactive table when the table is first loaded, and when **Reset Filters** is clicked.

## Planet Properties Columns

| Database<br />Column Name | Table Label | Description | Uncertainties Column<br />(positive +)<br />(negative -) | Limit Column |
| :--- | :--- | :--- | :--- | :--- |
| pl_tranmid† | Planet Transit Midpoint [BJD] | The time given by the average of the time the planet begins to cross the stellar limb and the time the planet finishes crossing the stellar limb. | (+) pl_tranmiderr1 <br /> (-) pl_tranmiderr2 | pl_tranmidlim |
| pl_orbper† | Planet Orbital Period [days] | Time the planet takes to make a complete orbit around the host star or system. | (+) pl_orbpererr1 <br /> (-) pl_orbpererr2 | pl_orbperlim |
| pl_trandurh† | Planet Transit Duration [hours] | The length of time from the moment the planet begins to cross the stellar limb to the moment the planet finishes crossing the stellar limb. | (+) pl_trandurherr1 <br /> (-) pl_trandurherr2 | pl_trandurhlim |
| pl_trandep† | Planet Transit Depth [ppm] | The size of the relative flux decrement caused by the orbiting body transiting in front of the star. | (+) pl_trandeperr1 <br /> (-) pl_trandeperr2 | pl_trandeplim |
| pl_rade† | Planet Radius [R_Earth] | Length of a line segment from the center of the planet to its surface, measured in units of radius of the Earth. | (+) pl_radeerr1 <br /> (-) pl_radeerr2 | pl_radelim |
| pl_insol† | Planet Insolation [Earth flux] | Insolation flux is the measure of the amount of stellar radiation received by the planet in units relative to that measured from the Earth from the Sun. | (+) pl_insolerr1 (-) pl_insolerr2 | pl_insollim |
| pl_eqt† | Planet Equilibrium Temperature [K] | The equilibrium temperature of the planet as modeled by a black body heated only by its host star. | (+) pl_eqterr1 <br /> (-) pl_eqterr2 | pl_eqtlim |

† Default column: these columns display in the interactive table when the table is first loaded, and when **Reset Filters** is clicked.

## Stellar Properties Columns

| Database<br />Column Name | Table Label | Description | Uncertainties Column<br />(positive +)<br />(negative -) | Limit Column |
| :--- | :--- | :--- | :--- | :--- |
| st_tmag† | TESS Magnitude | Brightness of the host star as measured using the TESS-band in units of magnitudes as reported in the TESS Input Catalog. | (+) st_tmagerr1 <br /> (-) st_tmagerr2 | st_tmaglim |
| st_dist† | Stellar Distance [pc] | Distance to the planetary system in units of parsecs as reported in the TESS Input Catalog. | (+) st_disterr1 <br /> (-) st_disterr2 | st_distlim |
| st_teff† | Stellar Effective Temperature [K] | Stellar effective temperature value as reported in the TESS Input Catalog. | (+) st_tefferr1 <br /> (-) st_tefferr2 | st_tefflim |
| st_logg† | Stellar log(g) [cm/s**2] | Gravitational acceleration experienced at the stellar surface as reported in the TESS Input Catalog. | (+) st_loggerr1 <br /> (-) st_loggerr2 | st_logglim |
| st_rad† | Stellar Radius [R_Sun] | Length of a line segment from the center of the star to its surface, measured in units of radius of the Sun as reported in the TESS Input Catalog. | (+) st_raderr1<br />(-) st_raderr2 | st_radlim |

† Default column: these columns display in the interactive table when the table is first loaded, and when **Reset Filters** is clicked.

## Dates Columns

| Database<br />Column Name | Table Label | Description | Uncertainties Column<br />(positive +)<br />(negative -) | Limit Column |
| :--- | :--- | :--- | :--- | :--- |
| toi_created† | TOI Creation Date | Date on which the TESS Project identified the Object of Interest. | | |
| rowupdate† | Date of Last Update | Date of last update of the planet parameters. | | |

Last updated: 9 September 2021
