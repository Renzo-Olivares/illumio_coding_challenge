## Thought process
* For my implementation I decided to use nested dictionaries.

## Classes
`Firewall`
* `accept_packet()` : accesses ruleMap like such `ruleMap[direction][protocol][port]`, and then iterates through the list of ip's at that port. If it finds the ip then return `True` if not then it will return `False`. If the port is not a valid key then return `False`.

`FirewallHelper`
* Helper class includes functions that Firewall utilizes to create a ruleMap
* `readRules()` : reads csv row by row grabbing a range of ip's and ports for each row and placing them into a HashMap in the following structure `ruleMap[direction][protocol][port]`, and then at each port we insert a list of valid ips
* `getIpRange()` : grabs a range of ip's given a start and ending ip using python's ipaddress library
* `getPortRange()` : grabs a range of ports given a start and ending port

`FirewallTest`
* Contains unit tests for firewall

## Testing
* I use python's built in unit test library in order to conduct my tests. You can find the unit tests in `fw_test.py` and you can run them with `unit_test`.py .