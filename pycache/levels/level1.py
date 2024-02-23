import pygame

level =  '''-----------------------------------------------------------
-                                                         -
-                                                         -
-                                                         -
-                                                         -
-                                                         -
-                                                         -
-                                                         -
-                                                         -
-                                                         -
-                                                         -
-                                                         -
-                                                         -
-                      -                                  -
-                                                         -
-          -                                              -
-                                                         -
-                  -                                      -
-                   -                                     -
-      -      -      -                                    -
-      --             -                                   -
-                   -  -                                  -
-                       -                                 -
-                        -                                -
-   ---         ---       ---                             -
-----------------------------------------------------------'''

def get_level() -> str:
    return level

level = get_level()

tiles_list = []
def level_rect_list():
    x_cur = y_cur = 0
    for row in level.split("\n"):
        for col in row:
            if col == '-':
                tiles_list.append(pygame.Rect(x_cur, y_cur, 40, 40))
            x_cur += 40
        x_cur = 0
        y_cur += 40
    return tiles_list