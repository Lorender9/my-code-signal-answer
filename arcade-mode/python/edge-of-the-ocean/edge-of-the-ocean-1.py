def solution(inputArray):
    max_product = float("-inf")
    for aux in range(len(inputArray)-1):
        product = inputArray[aux]*inputArray[aux+1]
        if(product >= max_product):
            max_product = product
    return max_product
