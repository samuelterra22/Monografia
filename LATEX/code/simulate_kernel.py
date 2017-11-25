@cuda.jit
def simulate_kernel(apX, apY, matrix_results, floor_plan):
    startX, startY = cuda.grid(2)
    gridX = cuda.gridDim.x * cuda.blockDim.x
    gridY = cuda.gridDim.y * cuda.blockDim.y
    for x in range(startX, WIDTH, gridX):
        for y in range(startY, HEIGHT, gridY):
            matrix_results[x][y] = propagation_model_gpu(x, y, 
                                                apX, apY, floor_plan)
