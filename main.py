import pandas as pd
from network_generator import random_generate
from network_generator import bla_generate
from prepare_json import prepare_df


Node_list=list(range(1,51))
#Node_list=map(str, Node_list)
p=0.07

#df=random_generate(Node_list,p)

df=bla_generate(Node_list)





prepare_df(df)