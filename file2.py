print("Gaussian Elimination Method")
import numpy as np
# Forward Elimination

def forward_elimination(A,b,n):
  for row in range(0,n-1):
    for i in range(row+1,n):
      factor = A[i,row]/A[row,row]
      for j in range(row,n):
        A[i,j]=A[i,j] - factor * A[row,j]
        b[i] = b[i] - factor * b[row]

      return A,b
# Backward Substitution
  def back_substitution(A,b,n):
    x=np.zeros((n,1))
    x[n-1]=b[n-1]/A[n-1, n-1]
    for row in range(n-2,-1,-1):
      sums=b[row]
      for j in range(row+1,n):
        sums=sums-A[row*j]*x[j]
        x[row]=sums/A[row,row]
      return x
# Gaussian elimination without pivoting
    def gauss(A,b):
      n=A.shape[0]
# Check for zero diagonal elements      
      if any(np.diag(A)==0):
        raise ZeroDivisionError(('Division by zero will occure; '
      ' pivoting currently not supported'))
        A,b =forward_elimination(A,b,n)

      return back_substitution(A,b,n)

# Main Program Starts Here
    if __name__ == '__main__':
      A=np.array([[1,-1,1],
                  [2,3,-1],
                  [3,-2,-9]])
      b=np.array([8,-2,9])
      x=gauss(A,b)
print(x)
