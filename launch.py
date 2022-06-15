from potens import Potens, Node


def read_nodes():
    nodes = [Node(line.split(':')[0], line.split(':')[1][:-1]) for line in open('ips.txt').readlines()]
    return nodes


if __name__ == '__main__':
    nodes = read_nodes()
    for node in nodes:
        print(node)
    experiment = Potens()
    experiment.init_system(nodes)
    experiment.upload_app()
    experiment.start_nodes()
    experiment.send_bang()