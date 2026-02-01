import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score


np.random.seed(1500)

df = pd.DataFrame({ 
    'number_of_houses' : np.random.randint( 20, 95 , 500),

    'number_of_floors' : np.random.randint( 10, 95 , 500),

    'building_age' : np.random.randint( 10, 200 , 500)
})

print(df.head())

base_rent = 5000
base_per_house = 3000
squared_error = 50
base_per_floors = 200
base_per_building_age = 100

df['rent'] = (
    base_rent 
    + base_per_house * df['number_of_houses'] 
    + squared_error * (df['number_of_houses'] **2)
    + base_per_floors * df['number_of_floors'] 
    - base_per_building_age * df['building_age'] 
    
)
df['rent'] += np.random.normal(0, 5000, size=len(df))


x = df[['number_of_houses']]
y = df['rent']

x_train , x_test , y_train , y_test = train_test_split( x , y , test_size= 0.25 , random_state= 1500)

linear_model = LinearRegression()

linear_model.fit( x_train ,y_train )

predicted_model = linear_model.predict(x_test)

print(f'rent = { linear_model.intercept_: .0f}')

#plot linear graph 
plt.figure(figsize= (10 , 5))
plt.scatter( x , y ,alpha=0.3 , s = 10 , label="Actual data")
plt.plot(x_test.sort_values('number_of_houses'), linear_model.predict(x_test.sort_values('number_of_houses')) )
plt.legend()
plt.show()


poly_model = PolynomialFeatures(degree = 2 , include_bias= False)

x_train_poly = poly_model.fit_transform(x_train)

x_test_poly = poly_model.transform(x_test)

poly = LinearRegression()
poly.fit( x_train_poly , y_train)

y_pred = poly.predict(x_test_poly)

x_plot_linear = np.linspace(x['number_of_houses'].min() , x['number_of_houses'].max(), 100).reshape(-1 , 1)
x_plot_poly = poly_model.transform(x_plot_linear)

plt.figure(figsize= (10 , 5))

plt.scatter(x , y , alpha=0.3 , s =10)
plt.plot(x_plot_linear, linear_model.predict(x_plot_linear) , label = " linear model ")
plt.plot(x_plot_linear, poly.predict(x_plot_poly) , label = " poly model ")  
plt.legend()
plt.show()


r_linear = r2_score( y_test , predicted_model)
r_poly = r2_score(y_test , y_pred)

print( f' the linear value { r_linear : .03f}')
print( f' the poly value { r_poly : .03f}')