import numpy as np
# from scipy import stats 

class CLTSample:

    def __init__(self, Dist, Type, N, Iter, P):
        self.Dist = Dist
        self.Type = Type
        self.N = N
        self.Iter = Iter
        self.P = P

    def isValidPara(self):
        if self.P == None:
            if self.Dist >= 1 and self.Dist <= 8:
                if self.Type >= 1 and self.Type <= 3:
                    if self.N > 0:
                        if self.Iter > 0:
                            return True
                        else: 
                            print("Interation should be a positive interger. Please re-enter!")
                            return False
                    else:
                        print("N should be a positive interger. Please re-enter!")
                        return False

                else:
                    print("Type provided only includes 1 to 3. Please re-enter!")
                    return False
            else:
                print("Distribution provided only includes 1 to 8. Please re-enter!")
                return False
        elif self.P >= 0 and self.P <= 1:
            if self.Dist >= 1 and self.Dist <= 8:
                if self.Type >= 1 and self.Type <= 3:
                    if self.N > 0:
                        if self.Iter > 0:
                            return True
                        else:
                            print("Interation should be a positive interger. Please re-enter!")
                            return False
                    else:
                        print("N should be a positive interger. Please re-enter!")
                        return False

                else:
                    print("Type provided only includes 1 to 3. Please re-enter!")
                    return False
            else:
                print("Distribution provided only includes 1 to 8. Please re-enter!")
                return False
        else:
            return False

    def typeEst(self, sampleList):
        if self.Type == 1:
            distSample = np.mean(sampleList)
        elif self.Type == 2:
            distSample = np.median(sampleList)
        else:
            distSample = np.quantiles(sampleList, self.P)

        return distSample

    def estSample(self):
        if self.isValidPara() == True:
            pass
        else:
            print("Wrong input! Please re-enter!")
    
        estimatorList = []            
        firstList = []
        i = 0

        for i in range(self.Iter):
            print("正在進行第 %d 次抽樣實驗 \n" % (i + 1))
            
            randomList = []
            
            if self.Dist == 1:
                randomList = np.random.uniform(0, 1, self.N)
            elif self.Dist == 2:
                randomList = np.random.normal(0, 1, self.N)
            elif self.Dist == 3:
                randomList = np.random.beta(0.5, 2, self.N)
            elif self.Dist == 4:
                randomList = np.random.beta(2, 0.5, self.N)
            elif self.Dist == 5:
                randomList = np.random.binomial(1, 0.5, self.N)
            elif self.Dist == 6:
                randomList = np.random.poisson(6, self.N)
            elif self.Dist == 7:
                randomList = np.random.exponential(6, self.N)
            else:
                randomList = np.random.uniform(0, 1, self.N) * 100

            if i == 0:
                firstList = randomList
                
            estimatorList.append(self.typeEst(randomList))

        return firstList, estimatorList

# def normalityCheckJB(sampleList):
#     jbTest = stats.jarque_bera(sampleList)

#     if jbTest[1] > 0.05:
#         return "樣本統計量符合常態分配"
#     else:
#         return "樣本統計量不符合常態分配"


# def strToPara(parameters):
#     paraList = parameters.split(" ")
#     lengthInput = len(paraList)

#     if lengthInput == 4:
#         try:
#             Dist, Type, N, Iter = [element for element in paraList]
#             CLTSampleClass = CLTSample(int(Dist), int(Type), int(N), int(Iter), None)
#         except ValueError:
#             print("Only integers are allowed in the input. Please re-enter!")
#     elif lengthInput == 5:
#         try:
#             Dist, Type, N, Iter, P = [element for element in paraList]
#             CLTSampleClass = CLTSample(int(Dist), int(Type), int(N), int(Iter), float(P))
#         except ValueError:
#             print("Only integers are allowed in the input. Please re-enter!")
#     else:
#         print("Wrong input length! Please re-enter")


#     return CLTSampleClass




