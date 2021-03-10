def Van_Eck_Sequence(n):
    if n<=0 or n//1 != n:  # eliminate all impossible values of N
        return None
    known_elements = []
    sequence = [0]
    for i in range(n-1): # first element is already in the list, so range should be -1
        if sequence[-1] in known_elements:
            sequence.append(sequence[:-1][::-1].index(sequence[-1])+1)
        else:
            known_elements.append(sequence[-1])
            sequence.append(0)
    return sequence