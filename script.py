import math as maths
def runge_kutta_4(f, x0, y0, x1, n,c1,c2,c3,c4,q1,q2,q3,w1,w2,w3):
    # Calculate step size
    h = (x1 - x0) / n
    
    # Initialize current values
    x_curr = x0
    y_curr = y0
    array_values=[]
    # Iterate over the desired number of steps
    for i in range(n):
        # Calculate k1, k2, k3, and k4
        k1 = h * f(x_curr, y_curr)
        k2 = h * f(x_curr + q1*h , y_curr + w1*k1 )
        k3 = h * f(x_curr + q2*h , y_curr + w2*k2 )
        k4 = h * f(x_curr + q3*h, y_curr + w3*k3)
        
        # Update x and y
        x_curr += h
        y_curr += c1*k1 + c2 * k2 + c3 * k3 + c4*k4
        array_values.append(y_curr) 
    
    # Return final value of y
    return y_curr,array_values
def rms_error(arr1, arr2):
  sum_of_squares = sum([(arr1[i] - arr2[i])**2 for i in range(len(arr1))])
  mean_of_squares = sum_of_squares / len(arr1)
  rms_error = maths.sqrt(mean_of_squares)

  return rms_error
def f(x, y):
  #my id is 24529
  return (29*x+1.33*y)/(1.33*x+29*y)
array_proven_values=[]  
array_my_values=[]  
#proven coefficients   
c1,c2,c3,c4,q1,q2,q3,w1,w2,w3=1/6,2/6,2/6,1/6,1/2,1/2,1,1/2,1/2,1
# since h=x1-x0/n, n is number of intervals so here it is
n=1
y_proven_coefficients,array_proven_values = runge_kutta_4(f, 0, 29/1.33, 29, n,c1,c2,c3,c4,q1,q2,q3,w1,w2,w3)
#my coefficients are just a multiple of proven coefficients; in report I  have mentioned reason that why I chose coefficients that
# are just a multiple of a proven coefficients
y_my_coefficients,array_my_values = runge_kutta_4(f, 0, 29/1.33, 29, n,2*c1,2*c2,2*c3,2*c4,2*q1,2*q2,2*q3,2*w1,2*w2,2*w3)
rmse=rms_error(array_proven_values,array_my_values)
print("when n=1, solution using proven coefficients:   ",round(y_proven_coefficients,4),"     solution using my coefficients:     ",round(y_my_coefficients,4),"   Root Mean Squared Error:   ",round(rmse,4))
n=2
y_proven_coefficients,array_proven_values = runge_kutta_4(f, 0, 29/1.33, 29, n,c1,c2,c3,c4,q1,q2,q3,w1,w2,w3)
y_my_coefficients,array_my_values = runge_kutta_4(f, 0, 29/1.33, 29, n,2*c1,2*c2,2*c3,2*c4,2*q1,2*q2,2*q3,2*w1,2*w2,2*w3)
rmse=rms_error(array_proven_values,array_my_values)
print("when n=2, solution using proven coefficients:   ",round(y_proven_coefficients,4),"     solution using my coefficients:     ",round(y_my_coefficients,4),"   Root Mean Squared Error:   ",round(rmse,4))
n=4
y_proven_coefficients,array_proven_values = runge_kutta_4(f, 0, 29/1.33, 29, n,c1,c2,c3,c4,q1,q2,q3,w1,w2,w3)
y_my_coefficients,array_my_values = runge_kutta_4(f, 0, 29/1.33, 29, n,2*c1,2*c2,2*c3,2*c4,2*q1,2*q2,2*q3,2*w1,2*w2,2*w3)
rmse=rms_error(array_proven_values,array_my_values)
print("when n=4, solution using proven coefficients:   ",round(y_proven_coefficients,4),"     solution using my coefficients:     ",round(y_my_coefficients,4),"   Root Mean Squared Error:   ",round(rmse,4))
n=8
y_proven_coefficients,array_proven_values = runge_kutta_4(f, 0, 29/1.33, 29, n,c1,c2,c3,c4,q1,q2,q3,w1,w2,w3)
y_my_coefficients,array_my_values = runge_kutta_4(f, 0, 29/1.33, 29, n,2*c1,2*c2,2*c3,2*c4,2*q1,2*q2,2*q3,2*w1,2*w2,2*w3)
rmse=rms_error(array_proven_values,array_my_values)
print("when n=8, solution using proven coefficients:   ",round(y_proven_coefficients,4),"     solution using my coefficients:     ",round(y_my_coefficients,4),"   Root Mean Squared Error:   ",round(rmse,4))
n=16
y_proven_coefficients,array_proven_values = runge_kutta_4(f, 0, 29/1.33, 29, n,c1,c2,c3,c4,q1,q2,q3,w1,w2,w3)
y_my_coefficients,array_my_values = runge_kutta_4(f, 0, 29/1.33, 29, n,2*c1,2*c2,2*c3,2*c4,2*q1,2*q2,2*q3,2*w1,2*w2,2*w3)
rmse=rms_error(array_proven_values,array_my_values)
print("when n=16, solution using proven coefficients:   ",round(y_proven_coefficients,4),"     solution using my coefficients:     ",round(y_my_coefficients,4),"   Root Mean Squared Error:   ",round(rmse,4))