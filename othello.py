import pygame
#pygameをインポート
import numpy as np
# numpyをインポート

pygame.init()
mesh = np. zeros([8, 8])
#pygameと盤上要素の初期化
# meshの中
# [[0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0. 0. 0.]]
mesh[3,3] = 2
mesh[3,4] = 3
mesh[4,3] = 3
mesh[4,4] = 2
#meshの持つ値によって石の色が変わる
# 0 : 空白
# 1 : 境界
# 2 : 黒石
# 3 : 白石

def situation(mesh):
    # 戦況の描画
    for x in range(8):
        for y in    range(8):
            pygame.draw.rect(screen, (0,0,0), (x*100,y*100,100,100), 1)
            if mesh[x, y] == 2: #黒石の描画
                pygame.draw.circle(screen, (0,0,0), (x*100+50,y*100+50), 45)
            elif mesh[x, y] == 3: #白石の描画
                pygame.draw.circle(screen, (255,255,255), (x*100+50,y*100+50), 45)

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('othello')
# 画面とキャプションの設定

running = True
# 無限ループ
while running:

    screen.fill((0,180,0))
    # 背景色に塗りつぶす

    situation(mesh)
    # 戦況の描画

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False #QUITを押すと終了する

    pygame.display.update()
    # 画面の更新