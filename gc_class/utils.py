# -*- coding: utf-8 -*-
# Copyright (C) 2026 Tomoo Ito
#
# This script is part of the QGIS plugin JP Multi-Source Geocoder.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.


from typing import Optional, Union


def safe_float(value: Optional[Union[str, float, int]]) -> Optional[float]:
    '''
    Safely converts a value to a float. If the conversion fails, returns None. '''
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
