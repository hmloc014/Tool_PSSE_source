import numpy as np
np.random.seed(1)

def bin2int(bin_list):
    #bin_list = [0, 0, 0, 1]
    int_val = ""
    for k in bin_list:
        int_val += str(int(k))
    #int_val = 11011011    
    return int(int_val, 2)

def gray2bin(g):
  len_g= len(g)
  b = g[0] 

  for i in range(1,len_g):
    x = (int(b[i-1])^int(g[i]))
    b = b+ str(x)
  return b

def random_sum_pairs(num):
    # num - no of samples
    bin_len = 14
    X = np.zeros((num, bin_len)).astype(int)
    Y = np.zeros((num)).astype(int)
    Z = np.zeros((num, bin_len)).astype(int)

    for i in range(num):
        X[i] = np.around(np.random.rand(bin_len)).astype(int)
        # print('-----X[i]:',X[i])
        b = ''
        for j in range(len(X[i])):
            b = b+str(int(X[i][j]))
        # Z[i] = gray2bin(X[i])
        Y[i] = bin2int(gray2bin(b))
    return X, Y

# convert data to strings
def to_string(X, y, n_numbers, largest):
	max_length = 14 #n_numbers * ceil(log10(largest+1)) + n_numbers - 1
	Xstr = list()
	for pattern in X:
		# print(pattern)
		strp = ''.join([str(n) for n in pattern])
		# strp = ''.join([' ' for _ in range(max_length-len(strp))]) + strp
		Xstr.append(strp)
	max_length = 6 #ceil(log10(n_numbers * (largest+1)))
	ystr = list()
	for pattern in y:
		strp = str(pattern)
		strp = ''.join([' ' for _ in range(max_length-len(strp))]) + strp
		ystr.append(strp)
	return Xstr, ystr
 
# integer encode strings
def integer_encode(X, y, alphabet,alphabetx):
	char_to_intx = dict((c, i) for i, c in enumerate(alphabetx))
	char_to_int = dict((c, i) for i, c in enumerate(alphabet))
	Xenc = list()
	for pattern in X:
		integer_encoded = [char_to_intx[char] for char in pattern]
		Xenc.append(integer_encoded)
	yenc = list()
	for pattern in y:
		# print("----y: ",y)
		# print("----pattern: ",pattern)
		integer_encoded = [char_to_int[char] for char in pattern]
		# print("----integer_encoded: ",integer_encoded )
		yenc.append(integer_encoded)
	return Xenc, yenc
 
# one hot encode
def one_hot_encode(X, y, max_int,max_intx):
	Xenc = list()
	for seq in X:
		pattern = list()
		for index in seq:
			vector = [0 for _ in range(max_intx)]
			vector[index] = 1
			pattern.append(vector)
		Xenc.append(pattern)
	yenc = list()
	for seq in y:
		pattern = list()
		for index in seq:
			vector = [0 for _ in range(max_int)]
			vector[index] = 1
			pattern.append(vector)
		yenc.append(pattern)
	return Xenc, yenc

def generate_data(n_samples, n_numbers, largest, alphabet,alphabetx):
	# generate pairs
	X, y = random_sum_pairs(n_samples)
	print('random_sum_pairs: ',X,y)
	# convert to strings
	X, y = to_string(X, y, n_numbers, largest)
	print('to_string: ',X,y)
	# integer encode
	X, y = integer_encode(X, y, alphabet,alphabetx)
	print('integer_encode: ',X,y)
	# one hot encode
	# X, y = one_hot_encode(X, y, len(alphabet),len(alphabetx))
	# print('one_hot_encode: ',y)
	# return as numpy arrays
	X, y = np.array(X), np.array(y)
	return X, y

# invert encoding
def invert(seq, alphabet):
	int_to_char = dict((i, c) for i, c in enumerate(alphabet))
	strings = list()
	for pattern in seq:
		string = int_to_char[np.argmax(pattern)]
		strings.append(string)
	return ''.join(strings)

# n_samples = 2000
n_numbers = 14
largest = 1
alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',' ']
alphabetx = ['0', '1']
no_of_smaples = 20
no_of_smaples_test = 5
trainX, trainY =  generate_data(no_of_smaples, n_numbers, largest, alphabet,alphabetx)
testX, testY = generate_data(no_of_smaples_test, n_numbers, largest, alphabet,alphabetx)

class RNN:
    def __init__(self):
        self.W = [1, 1]
        self.W_delta = [0.001, 0.001]
        self.W_sign = [0, 0]

        self.eta_p = 1.1
        self.eta_n = 0.6

    def state(self, xk, sk):
        print("--------xk: ",xk.shape )
        print("--------sk: ",sk.shape )
        stat =  xk * self.W[0] + sk * self.W[1]
        print("stat,stat.shape: ",stat,stat.shape)
        return stat
        

    def forward_states(self, X):
        print("----X.shape: ",X.shape)
        S = np.zeros((X.shape[0], X.shape[1]+1))
        print(S.shape[0],S.shape[1])
        for k in range(1, X.shape[1]):
            # print(k)
            next_state = self.state(X[:,k], S[:,k])
            S[:,k+1] = next_state
        print("----S: ",S, S.shape)
        return S

    def output_gradient(self, guess, real):
        print("--- Guess: ",guess.shape)
        print("--- real: ",real.shape)
        return 2 * (int(invert(guess,alphabet)) - int(invert(real,alphabet))) / no_of_smaples

    def backward_gradient(self, X, S, grad_out):
        grad_over_time = np.zeros(( X.shape[0], X.shape[1]+1 ))
        grad_over_time[:,-1] = grad_out
        wx_grad = 0
        wr_grad = 0
    
        # print("------------------X.shape[1]: ",X.shape[0],X.shape[1])
        for k in range(X.shape[1], 0, -1):
            # print("------------------grad_over_time: ",np.sum( grad_over_time[:, k] * X[:, k-1]))
            wx_grad += np.sum( grad_over_time[:, k] * X[:, k-1] )
            wr_grad += np.sum( grad_over_time[:, k] * S[:, k-1] )
            # print("------------------S[:, k-1]: ",S[:, k-1])
            grad_over_time[:, k-1] = grad_over_time[:, k] * self.W[1]
        
        return (wx_grad, wr_grad), grad_over_time

    def update_rprop(self, X, Y, W_prev_sign, W_delta):
        S = self.forward_states(X)
        print("--------S.shape: ",S.shape)
        # print(S.shape[0],S.shape[1], S[:, -1])
        grad_out =  self.output_gradient(S[:, -1], Y)
        W_grads, _ = self.backward_gradient(X, S, grad_out)
        self.W_sign = np.sign(W_grads)
        # print("----------------W_grads: ",W_grads)

        for i, _ in enumerate(self.W):
            if self.W_sign[i] == W_prev_sign[i]:
                W_delta[i] *= self.eta_p
            else:
                W_delta[i] *= self.eta_n
        self.W_delta = W_delta
        # print("W_delta in update_rprop: ",W_delta)

    def train(self, X, Y, training_epochs):
        for epochs in range(training_epochs):
            self.update_rprop(X, Y, self.W_sign, self.W_delta)
            # print('------------self.W:',self.W)
            for i, _ in enumerate(self.W):
                
                self.W[i] -= self.W_sign[i] * self.W_delta[i]

rnn = RNN()
rnn.train(trainX, trainY, 2)
print("Weight: \t", rnn.W)
print("Real: \t\t", invert(testY[:10]))

y = rnn.forward_states(testX)[:, -1]
print("Predicted: \t",invert(y[:10]))