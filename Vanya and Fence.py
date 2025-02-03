
def count_friends_in_view(n, h, heights):
    total_width = 0  
    for height in heights:
        if height > h:  
            total_width += 2  
        else:  
            total_width += 1  

    return total_width  

if __name__ == "__main__":

    n, h = map(int, input().split())
    
    heights = list(map(int, input().split()))
    
    result = count_friends_in_view(n, h, heights)
    print(result)
