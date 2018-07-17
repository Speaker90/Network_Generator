import numpy as np
import pandas as pd


def random_generate(Node_list,p):
    n=len(Node_list)
    network=[]
    for i in range(0, n-1):
        new=[Node_list[i]]*(n-1-i), Node_list[i+1:]
        new=map(list,zip(*new))
        network.extend(new)
    df=pd.DataFrame(network,columns=['source','target'])
    links=np.random.rand(n*(n-1)/2,1)<=p
    df['links']=links
    df=df[['source','target']].loc[df['links'] == True]
    nodes=map(list,zip(*[Node_list,Node_list]))
    df2=pd.DataFrame(nodes,columns=['source','target'])
    df=df.append(df2, ignore_index=True)
    df['value']=1
    return df


def bla_generate(Node_list):
    n=len(Node_list)
    network=[]
    for i in range(0,n):
        new=[Node_list[i]]*5, [Node_list[(i-2)%n],Node_list[(i-1)%n],Node_list[i],Node_list[(i+1)%n],Node_list[(i+2)%n]]
        new=map(list,zip(*new))
        network.extend(new)
    df=pd.DataFrame(network,columns=['source','target'])
    df['value']=1
    return df   