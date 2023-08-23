# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import pynini
from nemo_text_processing.inverse_text_normalization.jp.graph_utils import NEMO_DIGIT, GraphFst
from nemo_text_processing.inverse_text_normalization.jp.utils import get_abs_path
fr


class DateFst(GraphFst):
    """
    Finite state transducer for classifying date, e.g., 
    一日 -> 1日
    五から九日 -> (5~9日)
    一月 -> 1月
    三から四月 -> 3~4月
    一月一日 -> 1月1日
    七十年代 -> 70年代
    七十から八十年代 -> 70~80年代
    七月中 -> 7月中
    二十一世紀 -> 21世紀
    二千九年 -> 2009年
    月曜日 -> 
    """
    
