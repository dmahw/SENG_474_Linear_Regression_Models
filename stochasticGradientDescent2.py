import sys
import numpy as np
import datetime

def writeToFile(filepath, N, D, X, y, W, loss):
    filename = filepath.split(".tsv")
    outputFile = open(filename[0] + "_output_q3_2.tsv", "w")
    
    for i in range(1, D + 1):
        outputFile.write("w" + str(i) + "\t")
    outputFile.write("w0\n")
    
    for j in range(0, D + 1):
        outputFile.write(str(W[j]) + "\t")
    outputFile.write("\n")
    outputFile.close()

def calcLoss (N, D, X, y, W):
    constant = (1 / (2 * N))
    W_T = np.transpose(W)
    W_T_X = np.matmul(X, W_T)
    Z = y - W_T_X
    tpower = np.power(Z, 2)
    tsum = np.sum(tpower)
    loss = constant * tsum
    return loss

def calcOmega (N, D, X, y):
    T = 12
    alpha = 0.0000001
    m = 1

    W = np.random.random_sample(D + 1)

    for t in range(0, T):
        for n in range(0, N):
            c = alpha / m
            W_T = np.transpose(W)
            h = np.matmul(X[n], W_T)
            y_h = y[n] - h
            y_h_X = y_h * X[n]
            cYHX = c * y_h_X
            W = W + cYHX

    return W

def main (argv):
    files = open(argv[1], encoding="utf-8")
    file = [line.rstrip('\n') for line in files]

    lines = []
    linesKey = 0
    for line in file:
        lines.append(line.split("\t"))
        linesKey = linesKey + 1

    N = int(lines[0][0])
    D = int(lines[1][0])

    X = np.empty((N, D + 1))
    y = np.empty(N)

    xSize = 0
    ySize = 0
    for line in lines[3:]:
        line.append(1)

        X[xSize] = np.asarray(line[1:]).astype(float)
        y[ySize] = float(line[0])

        xSize = xSize + 1
        ySize = ySize + 1

    W = calcOmega(N, D, X, y)
    loss = calcLoss(N, D, X, y, W)
    writeToFile(argv[1], N, D, X, y, W, loss)
    print("p2q3_2.py successfully ran\n " + str(loss) + "\n")
    files.close()

print("Starting time:")
print(datetime.datetime.now())
print("\n")
main(sys.argv)
print("Finishing time:")
print(datetime.datetime.now())
