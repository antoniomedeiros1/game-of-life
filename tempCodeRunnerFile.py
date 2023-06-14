    cells = np.array([[1 if not (i*j) % 33 else 0 for i in range(W)]
                      for j in range(H)])