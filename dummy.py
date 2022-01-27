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

  # 한 줄 추가
  third = (last - first + 1) // 3
  # git push origin develop - develop 브랜치 remote 레포지토리(origin)에 push!

  # 나머지 부분 이어서 작성
  m_sort(A, first, first + third)

  m_sort(A, first + third + 1, first + 2 * third)

  m_sort(A, first + 2 * third + 1, last)