#s24019
#digitsData1.py

import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("データの個数=",len(digits.images))
print("画像データ=",digits.images[0])
print("なんの数字か",digits.target[0])
