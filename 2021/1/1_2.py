def __main__():
    depths = [int(depth) for depth in open('input.txt').read().removesuffix('\n').split('\n')]
    windows = [sum([first, second, third]) for first, second, third in zip(depths, depths[1:], depths[2:])]
    print(len([current for previous, current in zip(windows, windows[1:]) if current > previous]))


if __name__ == '__main__':
    __main__()
