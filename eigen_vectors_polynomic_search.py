import numpy as np
import math as mt


def norma(x):
    res = 0
    for j in x:
         res += j**2
    res = mt.sqrt(res)
    return res


def is_diff(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            diff = mt.fabs(x[i]-x[j])
            if diff >= eps:
                return False

    return True


eps = 0.001
eigen_value = 0
eigen_vector = np.array([])

size = int(input('Enter size of A-matrix: '))
print('Enter matrix A:')
A = []

for i in range(size):
    temp_string = input('')
    temp_list = temp_string.split()
    for j in range(len(temp_list)):
        temp_list[j] = float(temp_list[j])
    A.append(temp_list)

Matrix = np.array(A)

prev_iter = np.arange(size)
prev_iter = prev_iter/norma(prev_iter)
current_iter = np.dot(Matrix, prev_iter)
values = current_iter / prev_iter
print('x_prev = ' + str(prev_iter) + ' x_next = ' + str(current_iter))
while not is_diff(values) :
    prev_iter = current_iter
    prev_iter = prev_iter/norma(prev_iter)
    current_iter = np.dot(Matrix, prev_iter)
    values = current_iter/prev_iter
    print('x_prev = ' + str(prev_iter) + ' x_next = ' + str(current_iter))

eigen_vector = current_iter/norma(current_iter)
eigen_value = values[0]
print('eigen value' + str(eigen_value))
print('eigen value' + str(eigen_vector))






