import numpy as np

def extract_island(arr):

    def cc(ad):
        arr[tuple(ad)] = 0
        if (ad[0] + 1) >= 0 and (ad[0] + 1) < arr.shape[0] and (arr[ad[0] + 1, ad[1]] == 1):
            cc([ad[0] + 1, ad[1]])
        if (ad[0] - 1) >= 0 and (ad[0] - 1) < arr.shape[0]  and (arr[ad[0] - 1, ad[1]] == 1):
            cc([ad[0] - 1, ad[1]])
        if (ad[1] + 1) >= 0 and (ad[1] + 1) < arr.shape[1]  and (arr[ad[0], ad[1] + 1] == 1):
            cc([ad[0], ad[1] + 1])
        if (ad[1] - 1) >= 0 and (ad[1] - 1) < arr.shape[1]  and (arr[ad[0], ad[1] - 1] == 1):
            cc([ad[0], ad[1] - 1])

    for a in range(arr.shape[0] - 1):
        if arr[a, 0] == 1:
            cc([a, 0])
    for a in range(arr.shape[0] - 1):
        if arr[a, arr.shape[1] - 1] == 1:
            cc([a, arr.shape[1] - 1])
    for a in range(arr.shape[1] - 1):
        if arr[0, a] == 1:
            cc([0, a])
    for a in range(arr.shape[1] - 1):
        if arr[arr.shape[0] - 1, a] == 1:
            cc([arr.shape[0] - 1, a])

    return arr  

if __name__ == "__main__":

    #arr = np.array([[1,0,0,0,0],[1,0,1,1,0],[1,0,0,0,0],[0,0,1,1,0]])
    arr = np.random.randint(2, size=(10000, 10000))

    print(arr) 
    print(extract_island(arr))

