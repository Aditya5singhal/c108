import pandas as pd
import plotly.figure_factory as px
import random

result=[]
count=[]
for i in range(0,100):

    dice1=random.randint(1,6)
   # print(dice1)
    dice2=random.randint(1,6)
    #print(dice2)
    result.append(dice1+dice2)
   # print(result)
    count.append(i)

fig=px.create_distplot([result],["Result"])
fig.show()

