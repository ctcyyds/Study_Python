import pygame
import sys

# 初始化pygame
pygame.init()

# 创建窗口
pygame.display.set_mode(size=(640, 480))

# 创建Logo
icon = pygame.image.load("img/sank_logo.png")
pygame.display.set_icon(icon)

while True:
    # 处理事件，获取用户输入的事件
    even_list = pygame.event.get()
    for even in even_list:
        if even.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
