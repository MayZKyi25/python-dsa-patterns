'''
If a given list of numbers has duplicate, return True
else, return false
list = [1,2,3,3]
'''


def hasDuplicate(nums):
    my_dict = {}
    for current_num in nums:    # for x in [x,y,z,z,z]
        if current_num in my_dict:   #if there is that key (1) in dictionary?
            return True
        else:
           my_dict[current_num] = 1
    return False

def main (): 
    nums = [4,2,2352,456,2,8]
    print(f"Has duplicate in the given list of numbers? : {hasDuplicate(nums)}")

if __name__ == "__main__":
    main()

    

    
