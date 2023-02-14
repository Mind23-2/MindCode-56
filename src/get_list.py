# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Generate test lists"""
import scipy.io as io
import numpy as np

f1 = 'image_list_for_lfw.txt'

mat_lfw = io.loadmat('LightenedCNN_B_lfw.mat')
lfw_path_list = mat_lfw['image_path']
lfw_path_list = np.transpose(lfw_path_list)

lfw_label_list = mat_lfw['labels_original']
lfw_label_list = np.transpose(lfw_label_list)

for i in range(len(lfw_path_list)):
    print(lfw_path_list[i][0][0][10:], lfw_label_list[i][0][0])
    with open(f1, 'a') as file:
        line = lfw_path_list[i][0][0][10:] + ' ' + lfw_label_list[i][0][0]
        file.write(line + '\n')


f2 = 'image_list_for_blufr.txt'

mat_blufr = io.loadmat('BLUFR/config/lfw/blufr_lfw_config.mat')
blufr_path_list = mat_blufr['imageList']

for i in range(len(blufr_path_list)):
    print(blufr_path_list[i][0][0])
    with open(f2, 'a') as file:
        file.write(blufr_path_list[i][0][0] + '\n')
