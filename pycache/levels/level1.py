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
-                                                         -
-                                                         -
-   ---         ---       ---                             -
-----------------------------------------------------------'''

def get_level() -> str:
    return level

level = get_level()

tiles_list = []
def level_rect_list(w, h):
    x_cur = y_cur = 0
    for row in level.split("\n"):
        for col in row:
            if col == '-':
                tiles_list.append(pygame.Rect(x_cur, y_cur, w, h))
            x_cur += w
        x_cur = 0
        y_cur += h
    return tiles_list