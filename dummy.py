def merge(A, i, j, k, l):
  # i <= j and j < k <= l
  start = i
  B = []
  while i <= j and k <= l:
    if A[i] <= A[k]:
      B.append(A[i])
      i += l
    else:
      B.append(A[k])
      k += l
    for a in range(i, j+1):
      B.append(A[a])
    for b in range(k, l+1):
      B.append(A[b])
    for i in range(len(B)):
      A[start+i] = B[i]

def m_sort(A, first, last):
  # 3-way merge sort

  if first >= last: return