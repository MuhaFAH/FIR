from screens import first_screen, second_screen, third_screen, shop


if __name__ == '__main__':
    first_screen()
    while True:
        [third_screen, shop][second_screen()]()
