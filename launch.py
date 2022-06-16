from execo import Process
from potens import Potens, Node


def generate_config_files(nodes=4, min=50000, max=100000, ip="192.168.100.100", p=8000):
    genesis = Process('./app/genesis -n {} -i "{}" -p {} -l {} -h {}'.format(nodes, ip, p, min, max))
    genesis.run()

def read_nodes():
    nodes = [Node(line.split(':')[1], line.split(':')[2][:-1], line.split(':')[0]) for line in open('ips.txt').readlines()]
    return nodes


if __name__ == '__main__':
    # generate_config_files()
    nodes = read_nodes()
    experiment = Potens()
    experiment.init_system(nodes)
    experiment.upload_app()
    experiment.start_nodes()
    # experiment.send_bang()