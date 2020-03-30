# Copyright 1999-2020 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .to_gpu import to_gpu
from .to_cpu import to_cpu
from .rechunk import rechunk
from .reset_index import df_reset_index, series_reset_index
from .describe import describe
from .fillna import fillna, ffill, bfill
from .string_ import SeriesStringMethod
from .datetimes import SeriesDatetimeMethod
from .isin import isin


def _install():
    from ..core import DATAFRAME_TYPE, SERIES_TYPE, INDEX_TYPE

    for t in DATAFRAME_TYPE:
        setattr(t, 'to_gpu', to_gpu)
        setattr(t, 'to_cpu', to_cpu)
        setattr(t, 'rechunk', rechunk)
        setattr(t, 'reset_index', df_reset_index)
        setattr(t, 'describe', describe)
        setattr(t, 'fillna', fillna)
        setattr(t, 'ffill', ffill)
        setattr(t, 'bfill', bfill)
    for t in SERIES_TYPE:
        setattr(t, 'to_gpu', to_gpu)
        setattr(t, 'to_cpu', to_cpu)
        setattr(t, 'rechunk', rechunk)
        setattr(t, 'reset_index', series_reset_index)
        setattr(t, 'describe', describe)
        setattr(t, 'fillna', fillna)
        setattr(t, 'ffill', ffill)
        setattr(t, 'bfill', bfill)
        setattr(t, 'isin', isin)
    for t in INDEX_TYPE:
        setattr(t, 'rechunk', rechunk)


_install()
del _install
del SeriesStringMethod
del SeriesDatetimeMethod
