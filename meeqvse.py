def outer_func():
    example = "esaa garefunction"
    
    def inner_func():
        # wvdoma outer functionidan
        print(example)
    
    # davareturnot inner 
    return inner_func

if __name__ == "__main__":
    closure = outer_func()
    closure()
