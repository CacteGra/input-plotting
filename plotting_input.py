import csv
import os
import matplotlib.pylab as plt
from matplotlib.colors import is_color_like

def options(x_number, y_number):
    color = input('Please enter color name or color hex code: ').lower()
    while not is_color_like(color):
        if is_color_like('#{}'.format(color)):
            color = '#{}'.format(color)
            break
        color = input('Not a color.\nPlease enter color name or color hex code: ').lower()
    linewidth = input('Please enter line width (in px): ')
    while True:
        try:
            float(linewidth)
            break
        except ValueError:
            linewidth = input('Wrong answer. Please enter line width (in px): ')
    print(y_number)
    plt.plot(x_number, y_number, color=color, linewidth=linewidth)
    plt.ticklabel_format(style='plain',axis='x',useOffset=False)

def numbers(local_file, graph_number):
    if local_file:
        numbers_list = []
        x_numbers = []
        y_numbers = []
        graph = None
        with open('numbers.csv', 'r') as f:
            local_file = csv.DictReader(f)
            for row in local_file:
                print(row)
                if graph and graph != row['graph']:
                    numbers_list.append({'graph': graph, 'x_numbers': x_numbers, 'y_numbers': y_numbers})
                    x_numbers = []
                    y_numbers = []
                graph = row['graph']
                print(row['y'])
                x_numbers.append(row['x'])
                y_numbers.append(row['y'])
            numbers_list.append({'graph': graph, 'x_numbers': x_numbers, 'y_numbers': y_numbers})
            for numbers in numbers_list:
                print('a')
                options(list(map(int, numbers['x_numbers'])), list(map(int, numbers['y_numbers'])))
    else:
        x_number = []
        x_number.append(input('Please add x axis value (if you wish to add periodic x axis values just press [enter]): '))
        print(x_number)
        if x_number == ['']:
            x_number = []
        y_number = []
        y_number.append(input('Please add y axis value: '))
        last_number = 'has'
        while last_number:
            last_number = input('Please add y axis value (just press [enter] to quit): ')
            if last_number == '':
                break
            y_number.append(last_number)
        print('x = {0}\ny = {1}'.format(x_number, y_number))
        reverse = input('Reverse set numbers?(y/n) ')
        while reverse != 'y' and reverse != 'n':
            reverse = input('Wrong answer. Reverse set numbers?(y/n) ')
        if reverse == 'y':
            x_number = list(reversed(x_number))
            print(y_number)
            y_number = list(reversed(y_number))
            print(y_number)
        if not x_number:
            x_number = list(range(1, len(y_number) + 1))
        x_number = list(map(int, x_number))
        y_number = list(map(int, y_number))
        print('x = {0}\ny = {1}'.format(x_number, y_number))
        keys = {'graph': 0, 'x':0, 'y':0}.keys()
        with open('numbers.csv', 'a', newline='') as f:
            fieldnames = ['graph', 'x', 'y']
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not os.stat('numbers.csv').st_size > 0:
                dict_writer.writeheader()
            for r in zip(x_number, y_number):
                dict_writer.writerow({'graph': 'graph {}'.format(graph_number), 'x': r[0], 'y': r[1]})
        options(x_number, y_number)

def description():
    add_info = input('Do you wish to add grid, description?(y/n) ')
    while add_info != 'y' and add_info != 'n':
        add_info = input('Wrong answer.\nDo you wish to add grid, description?(y/n) ')
    if add_info == 'y':
        add_grid = input('Add grid?(y/n) ')
        while add_grid != 'y' and add_grid != 'n':
            add_grid = input('Wrong answer. Add grid?(y/n) ')
        if add_grid == 'y':
            plt.grid()
        add_title = input('Type in graph title (just press [enter to skip]): ')
        if add_title:
            plt.title(add_title)
        add_label = input('Type in x axis label (just press [enter to skip]): ')
        if add_label:
            plt.xlabel(add_label)
        add_label = input('Type in y axis label (just press [enter to skip]): ')
        if add_label:
            plt.ylabel(add_label)
        add_transparency = input('Add transparency?(y/n) ')
        while add_transparency != 'y' and add_transparency != 'n':
            add_transparency = input('Wrong answer. Add grid?(y/n) ')
        if add_transparency == 'y':
            plt.savefig('graph.png', transparent=True)
        else:
            plt.savefig('graph.png')
    else:
        plt.axis('off')
        plt.savefig('graph.png', transparent=True)

def main():
    try:
        with open('numbers.csv', 'r') as f:
            local_file = csv.DictReader(f)
    except FileNotFoundError:
        local_file = None
        with open('numbers.csv', 'w'):
            pass
    if local_file:
        import_numbers = input('Do you wish to import numbers from last session?(y/n) ')
        while import_numbers != 'y' and import_numbers != 'n':
            import_numbers = input('Wrong answer.\nDo you wish to import numbers from last session?(y/n) ')
        if import_numbers == 'n':
            with open('numbers.csv', 'w'):
                pass
            local_file = None
    graph_number = 0
    while True:
        graph_number += 1
        numbers(local_file, graph_number)
        another_one = input('Do you wish to add another graph?(y/n) ')
        while another_one != 'y' and another_one != 'n':
            another_one = input('Wrong answer.\nDo you wish to add another graph?(y/n) ')
        if another_one == 'n':
            break
        else:
            local_file = None
    description()

if __name__ == '__main__':
    main()
