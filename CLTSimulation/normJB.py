from scipy import stats 

def normalityCheckJB(sampleList):
    jbTest = stats.jarque_bera(sampleList)

    if jbTest[1] > 0.05:
        return "樣本統計量符合常態分配"
    else:
        return "樣本統計量不符合常態分配"