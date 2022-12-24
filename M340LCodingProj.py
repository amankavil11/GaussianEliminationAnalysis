#Abe Mankavil(UTEID: amm23896)
#M340L - Turnquist
#Midterm #2 Project
from random import random
import numpy as np

class Matrix():
    def __init__(self, m,n):
        self.Matrix = self.create_matrix(m,n)

    def GaussianElim(self, tol=1.0e-12):
        numOfRow = len(self.Matrix)
        numOfColumn = len(self.Matrix[0])
        #Number of pivots can be no more than the lesser of the number of rows and columns
        leastColOrRow = numOfColumn if numOfRow >= numOfColumn else numOfRow

        for j in range(leastColOrRow):
            for i in range(j+1,numOfRow):
                if abs(self.Matrix[i][j]) > abs(self.Matrix[j][j]):
                    self.Matrix[i], self.Matrix[j] = self.Matrix[j], self.Matrix[i]
            for i in range(j+1, numOfRow):
                if self.Matrix[i][j] > tol:
                    q = float(self.Matrix[i][j]/(self.Matrix[j][j]))
                    for k in range(j, numOfColumn):
                        self.Matrix[i][k] -= (self.Matrix[j][k]) * q
                else: 
                    self.Matrix[i][j] = 0.0

        #Uncomment next two lines to use numpy array to zero out any elements that are below the tolerance threshold and deemed round off error
        # matrix_with_roundoff = np.array(self.Matrix)
        # self.Matrix = (np.where(np.abs(matrix_with_roundoff) > tol, matrix_with_roundoff, 0.0)).tolist()

         

    #Creates original matrix using uniform distribution from [0.0,1.0) to fill elements
    def create_matrix(self,m,n):
        new_matrix = [[] for i in range(m)]
        for row in new_matrix:
            for j in range(n):
                row.append(random())
        return new_matrix
    
    #Element-wise print of matrix object
    def print_matrix(self):
        for row in self.Matrix:
            print(row)

if __name__ == '__main__':
    matrix1 = Matrix(11,10) 
    print("Original Matrix")
    matrix1.print_matrix()
    print()
    print("Row Reduced Matrix")
    matrix1.GaussianElim()
    matrix1.print_matrix()
    print('m = ' + str(len(matrix1.Matrix)))
    print('n = ' + str(len(matrix1.Matrix[0])))

