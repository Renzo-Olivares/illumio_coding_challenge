# Illumio Coding Challenge
## Thought process
* For my implementation I decided to use nested dictionaries to store the firewall rules. I decided to do this because I realized that I did not need to create a new rule for every line because unlike the `port` and `ip_address` there was not much variation in `direction`, and `protocol`, so I made `inbound` and `outbound` the keys for the top level of my dictionary. Then inside those buckets I placed another dictionary with using the protocols `tcp` and `udp` as keys. Inside the protocol dictionary I would insert a new dictionary which would use `ports` as a key and a list of `ip_addresses` as the value. To figure out ranges for ports and ip_addresses I created helper functions that would return a list of ports or ip_addresses based on a start and end. 
* Using nested dictionaries was extremely helpful in building `accept_packet`. I simply needed to access the correct port in the dictionary in `O(1)` time and then iterate through the list of `ip_addresses` at the given port in `O(ip_addresses)` time.  

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

## Team Rank
    1. Platform Team
    2. Data Team
    3. Policy Team