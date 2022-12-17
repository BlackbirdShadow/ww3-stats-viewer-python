import graph_maker

def __launch_app():
    stats = [[13,18],[18,9],[35,6],[60,6],[80,0]]
    title = '12 Gauge Buckshot (MCS variant)'
    graph_maker.get_graph(stats, title)


if __name__ == '__main__':
    __launch_app()
