import numpy as np


def forward_elimination(A,b,n):
  for row in range(0,n-1):
    for i in range(row+1,n):
      factor = A[i,row]/A[row,row]
      for j in range(row,n):
        A[i,j]=A[i,j] - factor * A[row,j]
        b[i] = b[i] - factor * b[row]

      return A,b

  def back_substitution(A,b,n):
    x=np.zeros((n,1))
    x[n-1]=b[n-1]/A[n-1, n-1]
    for row in range(n-2,-1,-1):
      sums=b[row]
      for j in range(row+1,n):
        sums=sums-A[row*j]*x[j]
        x[row]=sums/A[row,row]
      return x

    def gauss(A,b):
      n=A.shape[0]
      
      if any(np.diag(A)==0):
        raise ZeroDivisionError((''))
        A,b =forward_elimination(A,b,n)

      return back_substitution(A,b,n)


    if __name__ == '__main__':
      A=np.array([[1,-1,1],
                  [2,3,-1],
                  [3,-2,-9]])
      b=np.array([8,-2,9])
      x=gauss(A,b)
print(x)
