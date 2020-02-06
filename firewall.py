from fw_helper import FirewallHelper


class Firewall:
    ruleMap = {'inbound': {'tcp': {}, 'udp': {}}, 'outbound': {'tcp': {}, 'udp': {}}}

    def __init__(self, path: str):
        FirewallHelper(path, self.ruleMap)

    def accept_packet(self, direction: str, protocol: str, port: int, ip_address: str) -> bool:
        try:
            if ip_address in self.ruleMap[direction][protocol][port]: #O(ipList)
                return True
        except KeyError:
            return False