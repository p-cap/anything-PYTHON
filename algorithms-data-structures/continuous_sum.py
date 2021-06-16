

# Reference: https://nbviewer.ipython.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20SOLUTIONS/Largest%20Continuous%20Sum%20-%20SOLUTION.ipynb

def large_cont_sum(arr): 
    
    # Check to see if array is length 0
    if len(arr)==0: 
        return 0
    
    # Start the max and current sum at the first element
    max_sum=current_sum=arr[0] 
   
    # For every element in array
    # the array below does not include the first element
    for num in arr[1:]: 
        
        # Recursive function
        current_sum=max(current_sum+num, num)
        # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum) 
        
    return max_sum 

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
