import numpy as np
import numpy.matlib


def knndis(t,X_M,k):
	Mg = X_M.shape[1]
	dist = np.sum((np.transpose(np.matlib.repmat(t,Mg,1)) - X_M)**2,0) 
	dist = np.sort(dist)
	return sum(dist[0:k])



def test(Nominal,Test,k,fast,alpha):
	errors = list()
	np.random.shuffle(Nominal)
	Ng = int(0.3*len(Nominal))
	Mg = Nominal.shape[1] - Ng

	X_N = Nominal[:,0:Ng]
	X_M = Nominal[:,Ng:-1]

	for i in range(Ng):
		
		e = knndis(X_N[:,i],X_M[:,i],k)
		errors.append(e)


	Lm = np.sort(errors)[int(len(errors)*(1-alpha))]
	print("Nominal Statistic Computed")

	t_len = Test.shape[1]
	stat = [0]
	for i in range(0,t_len):
		dis = knndis(Test[:,i],X_M,k)
		dis = dis - Lm
		stat.append(np.max((0,stat[i] +d)))

		if i > 5:
			if stat[i+1] - stat[i] <=0 and stat[i] - stat[i-1] <=0 and stat[i-1] - stat[i-2] <=0:
				stat[i+1] = 0

	return stat