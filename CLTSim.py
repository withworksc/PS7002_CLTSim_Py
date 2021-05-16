import os 

# Please manually change your working directory
# e.g.,
# In MacOS: os.chdir("/Users/seanchiang/Desktop/CLTSimPy")
# In Windows: 

os.chdir("/Users/seanchiang/Desktop/CLTSimPy") ## Here to change


##############################################################################
##                      Central Limit Simulation                            ##
##         Do NOT change the following unless you know what you are doing   ##
##############################################################################


from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from CLTSimulation import CLT as clt
from CLTSimulation import normJB as jb


currentPath = os.getcwd()
fontPath = currentPath + "/font/TaipeiSansTCBeta-Regular.ttf"
font = FontProperties(fname = fontPath, size = 16)
footnote = FontProperties(fname = fontPath, size = 14)


def CLTSimulation(distInput, typeInput, nInput, iterInput, pInput = None):
    
    CLTSampleClass = clt.CLTSample(distInput, typeInput, nInput, iterInput, pInput)
    
    CLTSampleClass.isValidPara()
    
    firstList = CLTSampleClass.estSample()[0]
    estimatorList = CLTSampleClass.estSample()[1]
    
    estNormalMsg = jb.normalityCheckJB(estimatorList)
    print(estNormalMsg)
    
    plt.figure(figsize = (12, 8), dpi = 300)
    plt.hist(firstList, color = "#DAA520", alpha = 0.5, bins = 50)
    plt.title("這是第一個樣本的分配", fontproperties = font)
    plt.show()
    
    plt.figure(figsize = (12, 8), dpi = 300)
    plt.hist(estimatorList, color = "#6495ED", alpha = 0.5, bins = 50)
    plt.title("這是樣本統計量分配", fontproperties = font)
    plt.show()
    
    
##############################################################################
##                        End of the Function                               ##
##############################################################################


# The function has following 5 argumants
# CLTSimulation(Dist, Type, N, Iter, P)

# The following is an example of the function

CLTSimulation(2, 1, 1000, 1000) ## Here to change the parameters






