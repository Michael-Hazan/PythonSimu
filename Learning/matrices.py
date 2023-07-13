def create_matrix(m,n):
	nums = []
	for i in range(m):
		row = []
		for j in range(n):
			row.append(0)
		nums.append(row)
	return nums

# problem 1
def is_valid_matrix(matrix):
	for i in range(len(matrix)):
		if i+1 == len(matrix):
			return True
		if len(matrix[i]) != len(matrix[i+1]):
			return False

# problem 2
def matrix_multiply(m,n):
	if not (is_valid_matrix(m) or is_valid_matrix(n)):
		return None
	if len(m) != len(n) or len(m[0]) != len(n[0]):
		return None
	
	length_cols = len(m) # collums variable
	length_rows = len(m[0]) # rows varaible
	m0 = create_matrix(length_cols, length_rows) # returned matrix

	for i in range(length_cols):
		for j in range(length_rows):
			m0[i][j] = m[i][j]*n[i][j]
	return m0

ma1 = [[1,2,3],[1,2,3]]
ma2 = [[3,2,1],[3,2,1]]
print(matrix_multiply(ma1, ma2))
