# [turtle1.py]
#カラフルな花を書く

from turtle import *
shape("turtle") 
col= ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    circle(100)#半径100の円を描くこと
    left(72)#左に72度曲がること
    
done()
