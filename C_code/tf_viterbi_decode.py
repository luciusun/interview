#!/usr/bin/env python
# -*- coding: utf-8 -*-

' tensorflow维特比解码, 参考：https://github.com/tensorflow/tensorflow/blob/r1.8/tensorflow/contrib/crf/python/ops/crf.py'

__author__ = 'Sun Liang'

import numpy as np

def viterbi_decode(score, transition_params):
  """Decode the highest scoring sequence of tags outside of TensorFlow.
  This should only be used at test time.
  Args:
    score: A [seq_len, num_tags] matrix of unary potentials.
    transition_params: A [num_tags, num_tags] matrix of binary potentials.
  Returns:
    viterbi: A [seq_len] list of integers containing the highest scoring tag
        indices.
    viterbi_score: A float containing the score for the Viterbi sequence.
  """
  trellis = np.zeros_like(score)
  backpointers = np.zeros_like(score, dtype=np.int32)
  trellis[0] = score[0]

  for t in range(1, len(score)):
    # b0 = np.expand_dims(trellis[t - 1], 1)
    v = np.expand_dims(trellis[t - 1], 1) + transition_params
    # b1 = score[t]
    # b2 = np.max(v, 0)
    trellis[t] = score[t] + np.max(v, 0)
    # b3 = score[t] + np.max(v, 0)
    # b4 = np.argmax(v, 0)
    backpointers[t] = np.argmax(v, 0)



  viterbi = [np.argmax(trellis[-1])]
  # b5 = trellis[-1]
  # b6 = np.argmax(trellis[-1])
  # b7 = backpointers[1:]

  for bp in reversed(backpointers[1:]):
    # b8 = bp
    # b9 = bp[viterbi[-1]]
    viterbi.append(bp[viterbi[-1]])

  viterbi.reverse()

  viterbi_score = np.max(trellis[-1])
  return viterbi, viterbi_score





#LTSM-CRF模型：LSTM输出的2个参数, 模型地址：https://github.com/luciusun/zh-NER-TF


#example：我想到仙葫宾馆停车场
score = [[-26.027508, -30.446663  ,-32.095524 , -32.845524 ],
 [ -5.587373,   -6.7593894, -10.926412 ,  -8.4131   ],
 [-21.166603,  -23.149029 , -25.346634 , -21.89478  ],
 [  2.4026604 , 11.540352 ,  -7.339636 ,  -6.6280584],
 [ 44.77494  ,  41.91407 ,   44.076794 ,  47.784664 ],
 [ 53.988213  , 50.826843 ,  54.13177 ,   54.337772 ],
 [ 44.029934  , 40.22435 ,   43.935413  , 45.1827   ],
 [ 34.80221  ,  31.385918 ,  34.385857 ,  33.761864 ],
 [ 25.96698   , 22.97392  ,  24.499361  , 25.053926 ],
 [  8.182451 ,  -4.3964767,  -5.321798  ,  8.880457 ]]



transition_params = [[  0.52801377 , -5.8691854,  -22.835735  , -21.817001  ],
 [-13.961705,   -27.57293   ,   2.904173   ,  2.449105  ],
 [-24.47217  ,  -28.298948  ,   1.9355817   , 1.9138696 ],
 [ -7.580759 ,  -28.631573  , -26.004593 ,  -25.073975  ]]




viterbi, viterbi_score = viterbi_decode(score, transition_params)
print(viterbi)
print(viterbi_score)


