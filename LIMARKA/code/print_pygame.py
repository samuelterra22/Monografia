def print_pygame(matrix_results, access_points, DISPLAYSURF):
    matrix_max_value = matrix_results.max()
    matrix_min_value = -100
    # Le os valores da matriz que contem valores 
    # calculados e colore
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = get_color_of_interval(matrix_results[x][y], 
            matrix_max_value, matrix_min_value)
            draw_point(DISPLAYSURF, color, x, y)
    # Pinta de vermelho a posicao dos Access Points
    for ap in access_points:
        draw_point(DISPLAYSURF, RED, ap[0], ap[1])
    # Atualiza a janela do PyGame para que exiba a imagem
    pygame.display.update()
