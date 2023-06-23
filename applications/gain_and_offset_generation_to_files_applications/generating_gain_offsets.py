import numpy as np 
import matplotlib.pyplot as plt

def create_gain_array(width): 
    np.random.seed(100)
    
    #Effective y points 
    #gain_array = np.random.randn(width) *(0.1) + 1
    
    #Generate standard normal distributon between 0 and 1
    data = np.random.randn(5000)
    gain_array = (data - data.min()) / (data.max() - data.min())

    #mean = 0.5 
    #variance = 0.1
    
    #data = np.random.randn(5000)
    #gain_array = mean + np.sqrt(variance) * data
    
    #Effective x points 
    x_points = np.arange(0,width)
    
    #print some data
    print("Number of Elements in gain_array   : ", gain_array.size)
    print("Number of Elements in x_points     : ", len(x_points))
    print("Max of gain_array      : ", gain_array.max())
    print("Min of gain_array      : ", gain_array.min())
    print("Mean of gain_array     : ", gain_array.mean())
    print("variance of gain_array : ", gain_array.var())

    #print the graphs to show distributions
    plt.hist(gain_array, bins=100, density=False, alpha=0.7,color = "peru")
    
    # Set labels and title
    plt.xlabel('Value of gain co-efficient')
    plt.ylabel('Frequency')
    plt.title('Gain Co-efficent Values from Standard Normal Distribution')
    plt.xlim(0,1)
    plt.ylim(0,200)
    
    #show the graph
    plt.show()   
   
    
def create_offset_array(width): 
    np.random.seed(100)
    offset_array = np.random.randint(10,size=(width))
    x_points = np.arange(0,5000)
    
    count_0 = np.count_nonzero(offset_array == 0)
    count_1 = np.count_nonzero(offset_array == 1)
    count_2 = np.count_nonzero(offset_array == 2)
    count_3 = np.count_nonzero(offset_array == 3)
    count_4 = np.count_nonzero(offset_array == 4)
    count_5 = np.count_nonzero(offset_array == 5)
    count_6 = np.count_nonzero(offset_array == 6)
    count_7 = np.count_nonzero(offset_array == 7)
    count_8 = np.count_nonzero(offset_array == 8)
    count_9 = np.count_nonzero(offset_array == 9)
    
    frequency_of_int_values = np.array([count_0,count_1,count_2,count_3,count_4,count_5,count_6, count_7, count_8, count_9])
    

    
    #print some data
    print("Number of Elements in offset_array   : ", offset_array.size)
    print("Number of Elements in x_points     : ", len(x_points))
    print("min of offset_array : ", offset_array.min() )
    print("max of offset_array : ", offset_array.max() )
    print("mean of the offset_array: ",offset_array.mean())
    #print the graphs to show distributions
    #plt.hist(offset_array, bins=100, density=False, alpha=0.7,color = "slategrey")
    
    #plt.bar(x_points,frequency_of_int_values,width=0.9)
    plt.plot(x_points,offset_array)
    plt.scatter(x_points,offset_array)
    
    #plt.plot(x_points, offset_array)
    # Set labels and title
    #plt.xlabel('Value of offset constant')
    plt.xlabel('Column Index')
    #plt.ylabel('Frequency')
    plt.ylabel('Offset Value')
    #plt.title('Offset Constant Values of Random Ints')
    plt.title('Offset Constant Values for First 20 Pixel Columns')
    plt.xlim(-1,20)
    #plt.xticks(x_points,x_points)
    plt.ylim(-1,10)
    
    
    #show the graph
    plt.show()   
   
    
    
def main(): 
    width = 5000
    #create_gain_array(width)
    create_offset_array(width)
    
    
    

    

    
if __name__ == "__main__": 
    main()