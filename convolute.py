def convolute(A, B, C):
    """
    This function is more the convolution of three values.
    It raises the first argument to the power of the second,
    and then divided by one less than the third. 
    :param A: This is the value returned by afunc.
    :param B: This is the value returned by bfunc.
    :param C: This is the value returned by cfunc.
    :return: The returned value is a floating point.
    """
    return (A ** B) / (C - 1)