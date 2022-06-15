from typing import List
from execo import Remote, Process, Host, Put, config

class Node:
    def __init__(self, ip, port) -> None:
        self.ip = ip
        self.port = port
    
    def __str__(self) -> str:
        return "Node[ip={}, port={}]".format(self.ip, self.port)


class Potens:
    def __init__(self) -> None:
        self.nodes = []
        self.hosts = []
        self.instances = []
        self.initialized = False

    def init_system(self, nodes: List[Node]) -> None:
        self.nodes = nodes
        self.initialized= True
        for node in nodes:
            host = Host(node.ip, port=node.port)
            self.hosts = self.hosts + [host]

    def upload_app(self, location = './app/') -> bool:
        params = config.default_connection_params
        # Put(self.hosts, [location+'genesis', location+'potens_new']).run()

    def start_nodes(self) -> bool:
        self.instances = Remote("ls", self.hosts)
        self.instances.start()

    def send_bang(self) -> bool:
        self.instances.processes[0].write(b'bang\n');