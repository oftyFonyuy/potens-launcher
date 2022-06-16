from typing import List
from execo import Remote, Process, Host, Put, config

class Node:
    def __init__(self, ip, port, user) -> None:
        self.ip = ip
        self.port = int(port)
        self.user = user
    
    def __str__(self) -> str:
        return "Node[user={}, ip={}, port={}]".format(self.user, self.ip, self.port)


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
            host = Host(node.ip, user=node.user)
            self.hosts = self.hosts + [host]

    def upload_app(self, location = './app/') -> bool:
        params = config.default_connection_params
        Put(self.hosts, [location+'genesis', location+'potens_new', location+'config.toml', 'genesis.toml']).run()

    def start_nodes(self) -> bool:
        pipes = Remote("mkfifo /tmp/fp-input", self.hosts)
        logs = Remote("mkdir potens-logs", self.hosts)
        # self.instances = Remote("tail -f /tmp/fp-input | RUST_BACKTRACE=1 RUST_LOG=debug ./target/$mode/potens_new -g y -p $((i-1))  2> ./logs/potens_new_gen_$((i-1)).log", self.hosts)

        pipes.run()
        logs.run()
        # self.instances.start()


    def send_bang(self) -> bool:
        self.instances.processes[0].write(b'bang\n');