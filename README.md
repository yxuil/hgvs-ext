# HGVS Extension Package

An extension package for HGVS variant description handling.

This collects a set of helper functions to use hgvs and hide details.
For ease of use, global variables hdp, hm, hv, hp, hn are used throughout,
and can be accessed by other modules import hgvs_util and initialize these
global variables first:
    ```
    import hgvs_objects as hu
    hu.set_hgvs_objects()
    hu.hm.p_to_c(pvar)
    hu.hv.validate_variant(var)
    ```
(Using setter method to avoid initilization during import)

## Installation

```bash
pip install hgvs-ext