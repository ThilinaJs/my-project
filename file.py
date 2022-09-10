A = [[8,3,-3],[-2,-8,5],[3,5,10]]

diagonalc = np.diag(np.abs(A))

offdiagonal = np.sum(np.abs(A),axis = 1)-diagonalc

if np.all(diagonalc > offdiagonal):
  print("Matrix is ")

else:
  print()
