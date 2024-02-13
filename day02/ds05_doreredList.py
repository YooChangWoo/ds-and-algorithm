# file : ds05_orderedList.py
# desc : 선형리스트 응용\2

def printPoly(p_x) :
    term = len(p_x) - 1
    polyStr = "P(x)="

    for i in range(len(px)):
        coef = p_x[i]

        if(coef >=0) :
            polyStr += "+"
            polyStr += str(coef) + "x^" + str(term)+" "
            term -= 1

        return polyStr
    
def calcPloy(xVal, p_x) :
    retValue = 0
    term = len(p_x)-1

    for i in range(len(px)):
        coef = p_x[i]
        retValue += coef * xVal **term
        term -= 1

    return retValue

## 전역 변수 선언 부분 ##
px = [7, -4, 0, 5]  # 7x^3 -4x$2 +0*^1 +5x^0


# 메인 코드 부분##
if __name__ == "__main__":

    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxVlue = int(calcPloy(xValue, px))
    print(pxVlue)

    ##함수 선언 부분 ##
    def printPoly(t_x, p_x) :
        polyStr = "P(x)="

        for i in range(len(p_x)) :
            term = t_x[i]
            coef = p_x[i]

            if (coef >=0) :
                polyStr += "+"
            polyStr += str(coef) + "x^" + str(term) + " "

        return polyStr
    
    def calcPly(xVal, t_x, p_x):
        retValue = 0

        for i in range(len(px)):
            term = t_x[i]
            coef = p_x[i]
            retValue += coef * xValue **term

        return retValue

