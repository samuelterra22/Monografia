@jit
def simula_propagacao_gpu(pointX, pointY):
    g_matrix = np.zeros(shape=(WIDTH, HEIGHT), dtype=np.float32)
    blockDim = (48, 8)
    gridDim = (32, 16)
    d_matrix = cuda.to_device(g_matrix)
    simulate_kernel[gridDim, blockDim](pointX, pointY, 
                                        d_matrix, floor_plan)
    d_matrix.to_host()
    return g_matrix
