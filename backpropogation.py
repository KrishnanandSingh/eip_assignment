""" Generates a backpropogation table with one output and one hidden layer """
import numpy as np
import re


def sigmoid(x, derivative=False):
    return x*(1-x) if derivative else 1/(1+np.exp(-x))


def md_matrix(arr, name):
    if len(arr.shape) == 2:
        elems = arr.shape[1]
    elif len(arr.shape) == 1:
        elems = arr.shape[0]
    else:
        print("don't know what to do with this matrix")
        return
    elems = elems + 1

    header_bars = ['|' for elem in range(elems)]
    header_bars.insert(int(elems/2), name)
    table_header = ''.join(header_bars)
    header_line = '-'.join(['|' for elem in range(elems)])
    md_string = table_header+'\n'+header_line + '\n'
    
    arr = np.around(arr, decimals=3)
    arr_string = str(arr)
    arr_string = re.sub('(\[{1,2}\s*)|(\[{1,2})|(\s*\]{1,2})|(\]{1,2})|(\s+)', '|', arr_string)
    arr_string = re.sub('\|\|\|', '|\n|', arr_string)
    return md_string + arr_string + '\n\n'

with open('KRISHNANAND_BATCH_6_ASSIGNMENT2B.md', 'w+') as mdfile:
    input = np.array([[1, 0, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1]])
    desired_output = np.reshape(np.array([1, 1, 0]), (3, 1))
    mdfile.write('**Step 0**: Read input and output\n\n')
    mdfile.write(md_matrix(input, 'X'))
    mdfile.write(md_matrix(desired_output, 'Y'))

    wh = np.random.random((4,3))
    bh = np.random.random((1,3))
    wout = np.random.random((3,1))
    bout = np.random.random((1,1))

    # wh = np.array([[0.42, 0.88, 0.55],
    #             [0.10, 0.73, 0.68],
    #             [0.60, 0.18, 0.47],
    #             [0.92, 0.11, 0.52]])
    # bh = np.array([0.46, 0.72, 0.08])
    # wout = np.reshape(np.array([0.30, 0.25, 0.23]), (3, 1))
    # bout = np.array([0.69])


    mdfile.write('**Step 1**: Initialize weights and biases with random values (There are methods to initialize weights and biases but for now initialize with random values)\n\n')
    mdfile.write(md_matrix(wh, 'wh'))
    mdfile.write(md_matrix(bh, 'bh'))
    mdfile.write(md_matrix(wout, 'wout'))
    mdfile.write(md_matrix(bout, 'bout'))

    hidden_layer_input = input.dot(wh) + bh
    hidden_layer_actvn = sigmoid(hidden_layer_input)
    mdfile.write('----------------------\n')
    mdfile.write('**Step 2**: Calculate hidden layer input\n\n')
    mdfile.write(md_matrix(hidden_layer_input, 'hidden_layer_input'))
    mdfile.write('**Step 3**: Perform non-linear transformation on hidden linear input\n\n')
    mdfile.write(md_matrix(hidden_layer_actvn, 'hidden_layer_actvn'))

    outer_layer_input = hidden_layer_actvn.dot(wout) + bout
    actual_output = sigmoid(outer_layer_input)
    mdfile.write('**Step 4**: Perform linear and non-linear transformation of hidden layer activation at output layer\n\n')
    mdfile.write(md_matrix(actual_output, 'output'))
    error = desired_output - actual_output
    mdfile.write('**Step 5**: Calculate gradient of Error(E) at output layer\n\n')
    mdfile.write(md_matrix(error, 'E'))

    slope_hidden_layer = sigmoid(hidden_layer_actvn, derivative=True)
    slope_output_layer = sigmoid(actual_output, derivative=True)
    mdfile.write('**Step 6:** Compute slope at output and hidden layer\n\n')
    mdfile.write(md_matrix(slope_hidden_layer, 'slope hidden layer'))
    mdfile.write(md_matrix(slope_output_layer, 'Slope output'))

    mdfile.write('**Step 7**: Compute delta at output layer\n\n')
    delta_output = error * slope_output_layer
    mdfile.write(md_matrix(delta_output, 'delta output'))

    mdfile.write('**Step 8**: Calculate Error at hidden layer\n\n')
    error_at_hidden_layer = delta_output.dot(wout.T)
    mdfile.write(md_matrix(error_at_hidden_layer, 'error at hidden layer'))

    mdfile.write('**Step 9**: Compute delta at hidden layer\n\n')
    delta_hidden_layer = error_at_hidden_layer*slope_hidden_layer
    mdfile.write(md_matrix(delta_hidden_layer, 'delta hidden layer'))

    mdfile.write('**Step 10**: Update weight at both output and hidden layer\n\n')
    learning_rate = 0.1
    wout = wout + np.dot(hidden_layer_actvn.T, delta_output)*learning_rate
    wh = wh + np.dot(input.T, delta_hidden_layer)*learning_rate
    mdfile.write(md_matrix(wout, 'wout'))
    mdfile.write(md_matrix(wh, 'wh'))

    mdfile.write('**Step 11**: Update biases at both output and hidden layer\n\n')
    bh = bh + np.sum(delta_hidden_layer, axis=0)*learning_rate
    bout = bout + np.sum(delta_output, axis=0)*learning_rate
    mdfile.write(md_matrix(bh, 'bh'))
    mdfile.write(md_matrix(bout, 'bout'))
