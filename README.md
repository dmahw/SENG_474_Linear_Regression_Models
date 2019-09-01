SENG 474 Programming Assignment Linear Regression Models
========

## Developers
* David Mah
* Adam Leung

## Description
This repository is comprised of multiple solutions to solve linear regression models using normal equations, batch gradient descent, and stochastic gradient descent. Please note that the 100k dataset may be extremely expensive to compute however it is expected. 

* The 10k data set is expected to run for less than 5 minutes on all algorithms.
* The 100k data set is expected to run for less than 10 minutes only on stochastic gradient descent 2.

## Requirements
* Python 3.7.2
* numpy

## Instructions
1. Run the respective commands below for each part


Part 1 Normal Equations:
1. Run
    `python normalEquations.py [filename].tsv`
* You may need to use python3 instead of python if you have another version of python installed
2. The program will output in the console the starting time, loss, and finishing time.
3. All output files will be named "[filename]_output_q1.tsv"


Part 2 Batch Gradient Descent:
1. Run
    `python batchGradientDescent.py [filename].tsv`
* You may need to use python3 instead of python if you have another version of python installed
2. The program will output in the console the starting time, loss, and finishing time.
3. All output files will be named "[filename]_output_q2.tsv"


Part 3_1 Stochastic Gradient Descent (T = 20, learning rate = 0.000001):
1. Run
    `python stochasticGradientDescent1.py [filename].tsv`
* You may need to use python3 instead of python if you have another version of python installed
2. The program will output in the console the starting time, loss, and finishing time.
3. All output files will be named "[filename]_output_q3_1.tsv"


Part 3_2 Stochastic Gradient Descent (T = 12, learning rate = 0.0000001):
1. Run
    `python stochasticGradientDescent2.py [filename].tsv`
* You may need to use python3 instead of python if you have another version of python installed
2. The program will output in the console the starting time, loss, and finishing time.
3. All output files will be named "[filename]_output_q3_2.tsv"


## Resources
https://hunglvosu.github.io/DMW19.html
http://cs229.stanford.edu/notes/cs229-notes1.pdf



