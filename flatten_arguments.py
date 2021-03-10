# This function takes all the arguments passed and returns them in a list
# al the elements contained in arrays and sub-arrays passed as arguments are extracted and just the values inside them
# are passed into the list that will be returned

def flatten(*args):
    unchecked = True  # checks if arguments were changed in the last iteration of the following while loop
    while unchecked:
        arguments = []  # This is the list were all the values that are not lists go
        unchecked = False  # variable is set to False so that the loop can finish
        for arg in args:
            if type(arg) == list:  # checks if the current value of the arguments is a list
                for a in arg:  # if it is a list, it iterates between his elements and puts them into the argument list
                    arguments.append(a)
                unchecked = True  # if a list is found, all the unpacked elements must be checked too
            else:
                arguments.append(arg)
        args = arguments[:]  # the value of args is updated for the next iteration
    return arguments


print(flatten(['hello',2,['text',[4,5]]],[[]],'[list]'))  # test case
