
def calculate_iterations():

    number =1; iteration = 0

    while number <= 10000:
        number = number * 2
        iteration+=1
    print("Number is: "+str(number))
    return iteration


if __name__ == '__main__':
    #sample project to understand jenkins trigerred by git changes (SCM)
    iteration = calculate_iterations()
    print("Number of iterations: "+str(iteration))
