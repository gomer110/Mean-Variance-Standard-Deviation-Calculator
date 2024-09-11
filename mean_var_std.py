import numpy as np

def test():
    # testing = [0,1,2,3,4,5,6,7,8]
    testing = [2,6,2,8,4,0,1,5,7]
    return testing 

def calculate(list):
    
    my_array = np.array([[list[0], list[1], list[2]], [list[3], list[4], list[5]], [list[6], list[7], list[8]]])

    calculations = {'mean': [[my_array[:3,0].mean(), my_array[:3,1].mean(), my_array[:3,2].mean()],
                    [my_array[0,:3].mean(), my_array[1,:3].mean(), my_array[2,:3].mean()],
                    my_array.mean()], 
                    'variance': [[my_array[:3,0].var(), my_array[:3,1].var(), my_array[:3,2].var()],
                    [my_array[0,:3].var(), my_array[1,:3].var(), my_array[2,:3].var()],
                    my_array.var()],
                    'standard deviation': [[my_array[:3,0].std(), my_array[:3,1].std(), my_array[:3,2].std()],
                    [my_array[0,:3].std(), my_array[1,:3].std(), my_array[2,:3].std()],
                    my_array.std()],
                    'max': [[my_array[:3,0].max(), my_array[:3,1].max(), my_array[:3,2].max()],
                    [my_array[0,:3].max(), my_array[1,:3].max(), my_array[2,:3].max()],
                    my_array.max()],
                    'min': [[my_array[:3,0].min(), my_array[:3,1].min(), my_array[:3,2].min()],
                    [my_array[0,:3].min(), my_array[1,:3].min(), my_array[2,:3].min()],
                    my_array.min()],
                    'sum': [[my_array[:3,0].sum(), my_array[:3,1].sum(), my_array[:3,2].sum()],
                    [my_array[0,:3].sum(), my_array[1,:3].sum(), my_array[2,:3].sum()],
                    my_array.sum()]}

    return calculations

if __name__ == '__main__':
    temp = test()
    print(calculate(temp))