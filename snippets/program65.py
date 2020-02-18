import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset =pd.read_csv('data/weather.csv')
dataset.shape
dataset.describe()

dataset.plot(x='MinTemp',y='MaxTemp',style='o')
plt.title('minTemp vs MaxTemp')
plt.xlabel('MinTemp')
plt.ylabel('maxTemp')
plt.show()

plt.figure(figsize=(15,10)
plt.tight_layout()
seabornInstance.distplot(dataset['MaxTemp'])

x=dataset['MinTemp'].values.reshape(-1,1)
y=dataset['MaxTemp'].values.reshape(-1,1)

X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)

regressor=LinearRegression()
regressor.fit(x_train,ytrain)

print(regressor.intercept_)
print(regressor.coef_)

df=pd.DataFrame({"Actual":y_test.flatten(),'predicted':y_pred.flatten()})
df

df1=df.head(25)
df1.plot(kind='bar',figsize=(16,10))
plt.grid(which='major',linestyle='-',linewidth='0.5',color='green')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
plt.show()


plt.scatter(X_test,y_test,color='gray')
plt.plot(X_test,y_pred,color='red',linewidth=2)
plt.show()

print('Mean Absolute Error:',metrice.mean_absolute_error(y_test,y_pred))
print('Mean Squard Error:',metrics.mean_squared_error(y_test,y_pred))
print('Root Mean Squared Error:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))
