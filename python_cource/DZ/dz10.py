import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data['is_robot'] = (data['whoAmI'] == 'robot').astype(int)
data['is_human'] = (data['whoAmI'] == 'human').astype(int)

print(data.head(10))

