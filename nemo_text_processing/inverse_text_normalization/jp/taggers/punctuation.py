# Copyright (c) 2023, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
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
from nemo_text_processing.inverse_text_normalization.jp.graph_utils import GraphFst
from pynini.lib import pynutil


class PunctuationFst(GraphFst):
    """
    Finite state transducer for classifying punctuation
        e.g. a, -> tokens { name: "a" } tokens { name: "," }
    """

    def __init__(self):
        super().__init__(name="punctuation", kind="classify")

        s = "!#$%&'()*+,-./:;<=>?@^_`{|}~。，；：《》“”·~【】！？、‘’.<>-——_、。.「」『』‘`／・；’”“”‷･〔〕々〃ゝゞヽ〲〱〳〴〵ヾ〆，"
        punct = pynini.union(*s)

        graph = pynutil.insert('name: "') + punct + pynutil.insert('"')

        self.fst = graph.optimize()
