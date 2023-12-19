from drawer import draw_solution
from layout import Layout


def main():
    grid = (53, 32)
    shapes = [(5, 7), (7, 5)]
    upper_bound = 46
    model = Layout(grid, shapes, upper_bound)
    blocks = model.solve()
    draw_solution(grid, blocks, 'layout')
    return


if __name__ == '__main__':
    main()
