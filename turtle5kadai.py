# s24019
#カラフルな５角形を書く

from turtle import *
shape("turtle") 
col= ["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    forward(30)
    left(70)
    
done()
