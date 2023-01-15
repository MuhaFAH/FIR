import pygame


def cut_sheet(sheet, columns, rows, width, height):
    return [
        sheet.subsurface(pygame.Rect((width * column, height * row), (width, height)))
        for column
        in range(columns)
        for row
        in range(rows)
    ]


pygame.init()
WINDOW = pygame.display.set_mode((1620, 950))

SILVER_ARMOR = (
    (
        (
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/silver-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/gold-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/rubin-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/emerald-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/silver-armor/diamond-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    )
)

GOLD_ARMOR = (
    (
        (
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/silver-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/gold-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/rubin-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/emerald-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/gold-armor/diamond-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    )
)

RUBIN_ARMOR = (
    (
        (
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/silver-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/gold-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/rubin-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/emerald-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/rubin-armor/diamond-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    )
)

EMERALD_ARMOR = (
    (
        (
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/silver-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/gold-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/rubin-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/emerald-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/emerald-armor/diamond-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    )
)

DIAMOND_ARMOR = (
    (
        (
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/silver-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/gold-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/rubin-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/emerald-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    ), (
        (
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-up-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-up-images/frame-01.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-down-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-down-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-down-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-running-down-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-staying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-staying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-staying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-staying-images/frame-03.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-left-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-left-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-left-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-left-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-left-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-left-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-right-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-right-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-right-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-right-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-right-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-attack-right-images/frame-05.png').convert_alpha()
        ), (
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-dying-images/frame-00.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-dying-images/frame-01.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-dying-images/frame-02.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-dying-images/frame-03.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-dying-images/frame-04.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-dying-images/frame-05.png').convert_alpha(),
            pygame.image.load('assets/player-animation/diamond-armor/diamond-sword/player-dying-images/frame-06.png').convert_alpha(),
        )
    )
)


SILVER_ARMOR_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/armor-btn-images/silver-armor-btn-image.png'
    ).convert_alpha()
]

GOLD_ARMOR_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/armor-btn-images/gold-armor-btn-image.png'
    ).convert_alpha(),
    pygame.image.load(
        'assets/buttons/armor-btn-images/gold-not-buy-image.png'
    ).convert_alpha()
]

RUBIN_ARMOR_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/armor-btn-images/rubin-armor-btn-image.png'
    ).convert_alpha(),
    pygame.image.load(
        'assets/buttons/armor-btn-images/rubin-not-buy-image.png'
    ).convert_alpha()
]

EMERALD_ARMOR_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/armor-btn-images/emerald-armor-btn-image.png'
    ).convert_alpha(),
    pygame.image.load(
        'assets/buttons/armor-btn-images/emerald-not-buy-image.png'
    ).convert_alpha()
]

DIAMOND_ARMOR_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/armor-btn-images/diamond-armor-btn-image.png'
    ).convert_alpha(),
    pygame.image.load(
        'assets/buttons/armor-btn-images/diamond-not-buy-image.png'
    ).convert_alpha()
]


SILVER_SWORD_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/weapon-btn-images/silver-sword-btn-image.png'
    ).convert_alpha()
]

GOLD_SWORD_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/weapon-btn-images/gold-sword-btn-image.png'
    ).convert_alpha(),
    pygame.image.load(
        'assets/buttons/weapon-btn-images/gold-sword-not-buy-image.png'
    ).convert_alpha()
]

RUBIN_SWORD_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/weapon-btn-images/rubin-sword-btn-image.png'
    ).convert_alpha(),
    pygame.image.load(
        'assets/buttons/weapon-btn-images/rubin-sword-not-buy-image.png'
    ).convert_alpha()
]

EMERALD_SWORD_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/weapon-btn-images/emerald-sword-btn-image.png'
    ).convert_alpha(),
    pygame.image.load(
        'assets/buttons/weapon-btn-images/emerald-sword-not-buy-image.png'
    ).convert_alpha()
]

DIAMOND_SWORD_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/weapon-btn-images/diamond-sword-btn-image.png'
    ).convert_alpha(),
    pygame.image.load(
        'assets/buttons/weapon-btn-images/diamond-sword-not-buy-image.png'
    ).convert_alpha()
]


HEAL_BUFF_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/buff-btn-images/heal-buff-btn-image.png'
    ).convert_alpha()
]

SPEED_BUFF_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/buff-btn-images/speed-buff-btn-image.png'
    ).convert_alpha()
]

ARMOR_BUFF_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/buff-btn-images/armor-buff-btn-image.png'
    ).convert_alpha()
]

DAMAGE_BUFF_BTN_IMAGES = [
    pygame.image.load(
        'assets/buttons/buff-btn-images/damage-buff-btn-image.png'
    ).convert_alpha()
]


START_GAME_BTN_IMAGE = pygame.image.load(
    'assets/buttons/start-game-btn-image.png'
).convert_alpha()

ARENA_BTN_IMAGE = pygame.image.load(
    'assets/buttons/arena-btn-image.png'
).convert_alpha()

SHOP_BTN_IMAGE = pygame.image.load(
    'assets/buttons/shop-btn-image.png'
).convert_alpha()

BACK_BTN_IMAGE = pygame.image.load(
    'assets/buttons/back-btn-image.png'
).convert_alpha()

CONTINUE_GAME_BTN_IMAGE = pygame.image.load(
    'assets/buttons/continue-game-btn-image.png'
).convert_alpha()

LEAVE_GAME_BTN_IMAGE = pygame.image.load(
    'assets/buttons/leave-game-btn-image.png'
).convert_alpha()

LEAVE_ARENA_BTN_IMAGE = pygame.image.load(
    'assets/buttons/leave-arena-btn-image.png'
).convert_alpha()

SETTINGS_BTN_IMAGE = pygame.image.load(
    'assets/buttons/settings-btn-image.png'
).convert_alpha()


SKELETON_STAYING_IMAGES = cut_sheet(pygame.image.load(
    'assets/skeleton-animation/skeleton-staying-sheet.png'
).convert_alpha(),   11,   1,    72,   96)

SKELETON_MOVE_LEFT_IMAGES = cut_sheet(pygame.image.load(
    'assets/skeleton-animation/skeleton-move-left-sheet.png'
).convert_alpha(),   13,   1,    66,   99)[::-1]

SKELETON_MOVE_RIGHT_IMAGES = cut_sheet(pygame.image.load(
    'assets/skeleton-animation/skeleton-move-right-sheet.png'
).convert_alpha(),   13,   1,    66,   99)

SKELETON_ATTACK_LEFT_IMAGES = cut_sheet(pygame.image.load(
    'assets/skeleton-animation/skeleton-attack-left-sheet.png'
).convert_alpha(),   18,   1,    129,  111)[::-1]

SKELETON_ATTACK_RIGHT_IMAGES = cut_sheet(pygame.image.load(
    'assets/skeleton-animation/skeleton-attack-right-sheet.png'
).convert_alpha(),   18,   1,    129,  111)

SKELETON_DIE_IMAGES = cut_sheet(pygame.image.load(
    'assets/skeleton-animation/skeleton-die-sheet.png'
).convert_alpha(),   15,   1,    99,   96)


BOSS_STAYING_IMAGES = cut_sheet(pygame.image.load(
    'assets/boss-animation/boss-staying-sheet.png'
).convert_alpha(),   8,   1,    600,   208)

BOSS_MOVE_LEFT_IMAGES = cut_sheet(pygame.image.load(
    'assets/boss-animation/boss-move-left-sheet.png'
).convert_alpha(),   8,   1,    600,   208)[::-1]

BOSS_MOVE_RIGHT_IMAGES = cut_sheet(pygame.image.load(
    'assets/boss-animation/boss-move-right-sheet.png'
).convert_alpha(),   8,   1,    600,   208)

BOSS_ATTACK_LEFT_IMAGES = cut_sheet(pygame.image.load(
    'assets/boss-animation/boss-attack-left-sheet.png'
).convert_alpha(),   6,   1,    600,  208)[::-1]

BOSS_ATTACK_RIGHT_IMAGES = cut_sheet(pygame.image.load(
    'assets/boss-animation/boss-attack-right-sheet.png'
).convert_alpha(),   6,   1,    600,  208)

BOSS_DIE_IMAGES = cut_sheet(pygame.image.load(
    'assets/boss-animation/boss-die-sheet.png'
).convert_alpha(),   6,   1,    600,   208)


COIN_IMAGES = cut_sheet(pygame.image.load(
    'assets/coin.png'
).convert_alpha(),   9,    1,    16,   16)

BACKGROUND_IMAGE = pygame.image.load(
    'assets/background-image.png'
).convert_alpha()

PAUSE_MENU_IMAGE = pygame.image.load(
    'assets/pause-menu.png'
).convert_alpha()


BORDER_IMAGE = \
    pygame.Surface((1450, 650), pygame.SRCALPHA, 32)

PLAYER_RECT_IMAGE = \
    pygame.Surface((150, 111))


SKELETON_IMAGES = [
    SKELETON_MOVE_LEFT_IMAGES,
    SKELETON_MOVE_RIGHT_IMAGES,
    SKELETON_STAYING_IMAGES,
    SKELETON_ATTACK_LEFT_IMAGES,
    SKELETON_ATTACK_RIGHT_IMAGES,
    SKELETON_DIE_IMAGES
]

BOSS_IMAGES = [
    BOSS_MOVE_LEFT_IMAGES,
    BOSS_MOVE_RIGHT_IMAGES,
    BOSS_STAYING_IMAGES,
    BOSS_ATTACK_LEFT_IMAGES,
    BOSS_ATTACK_RIGHT_IMAGES,
    BOSS_DIE_IMAGES
]
