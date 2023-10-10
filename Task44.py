"""В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?"""
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

categories = data['whoAmI'].unique()
category_dict = {category: [1 if value == category else 0 for value in categories] for category in categories}
for category, encoded_values in category_dict.items():
	data[category] = encoded_values
data = data.drop('whoAmI', axis = 1)
data.head()