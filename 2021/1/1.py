def __main__():
    depths = [int(depth) for depth in open('input.txt').read().removesuffix('\n').split('\n')]
    print(len([current for previous, current in zip(depths, depths[1:]) if current > previous]))


if __name__ == '__main__':
    __main__()