def sobrepoe_solucoes_DIV_dBm(propagation_array, size):
    if size == 1:
        return propagation_array[0]
    matrixMin = propagation_array[0]
    matrixMax = propagation_array[0]
    for i in range(1, size):
        matrixMin = np.minimum(propagation_array[i], matrixMin)
        matrixMax = np.maximum(propagation_array[i], matrixMax)
    # pois ao subtrair dBm, deve ser o maior/menor
    sub = np.divide(matrixMax, matrixMin)
    return sub
