import csv
from ipaddress import IPv4Address as ipv4add


class FirewallHelper:
    def __init__(self, path:str, ruleMap: dict):
        self.readRules(path, ruleMap)

    def readRules(self, path: str, ruleMap: dict):
        with open(path) as ruleset:
            readRules = csv.reader(ruleset, delimiter=',')
            for row in readRules: #O(ruleset)
                ipList = self.getIpRange(row[3])

                portList = self.getPortRange(row[2])

                for port in portList: #O(portList)
                    ruleMap[row[0]][row[1]][int(port)] = ipList #row[0] : direction,row[1] : protocol

    def getIpRange(self, addrrange: str) -> list:
        ipRange = addrrange.split('-')
        ipList = []
        if len(ipRange) > 1:
            start = ipv4add(ipRange[0])
            end = ipv4add(ipRange[1])
            while start <= end:
                ipList.append(str(start))
                start += 1
        else:
            ipList.extend(ipRange)

        return ipList

    def getPortRange(self, portrange: str) -> list:
        rangeList = portrange.split('-') #O(portrange)
        portList = []
        if len(rangeList) > 1:
            for i in range(int(rangeList[0]), int(rangeList[1]) + 1): #O(range)
                portList.append(i)
        else:
            portList = rangeList
        return portList