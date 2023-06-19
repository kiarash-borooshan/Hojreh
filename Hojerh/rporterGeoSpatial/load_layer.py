"""
add polygon layers to map
https://www.dideo.ir/v/yt/Gtb3QHS2y3g/geodjango-tutorial-4%3A-generate-gis-model-from-geospatial-data
"""

import os
from .models import IRN_adm1
from django.contrib.gis.utils import LayerMapping

irn_adm1_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'type_1': 'TYPE_1',
    'engtype_1': 'ENGTYPE_1',
    'nl_name_1': 'NL_NAME_1',
    'varname_1': 'VARNAME_1',
    'geom': 'MULTIPOLYGON',
}


county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                          'data/Irn/IRN_adm1.shp'))


def run(verbose=True):
    lm = LayerMapping(IRN_adm1,
                      county_shp,
                      irn_adm1_mapping,
                      transform=False)
    lm.save(strict=True, verbose=verbose)
