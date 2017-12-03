def sobrepoe_solucoes_MAX(propagation_array, size):
    max = propagation_array[0]
    for i in range(1, size):
        max = np.maximum(propagation_array[i], max)				
    return max
