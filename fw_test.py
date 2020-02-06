import unittest
from firewall import Firewall


class TestFirewall(unittest.TestCase):
    fw = Firewall('fw.csv')

    def test0(self):
        self.assertTrue(self.fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"), "Rule not found, permission denied")

    def test1(self):
        self.assertTrue(self.fw.accept_packet("inbound", "udp", 53, "192.168.2.1"), "Rule not found, permission denied")

    def test2(self):
        self.assertTrue(self.fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"), "Rule not found, permission denied")

    def test3(self):
        self.assertFalse(self.fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"), "Rule not found, permission denied")

    def test4(self):
        self.assertFalse(self.fw.accept_packet("inbound", "udp", 24, "52.12.48.92"), "Rule not found, permission denied")