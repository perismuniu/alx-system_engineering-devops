0x07. Networking basics #0

Tasks

0. OSI model

Questions:

What is the OSI model?

	1. Set of specifications that network hardware manufacturers must respect
	2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
	3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

How is the OSI model organized?

	1. Alphabetically
	2. From the lowest to the highest level
	3. Randomly

1. Types of network

Questions:

What type of network a computer in local is connected to?

	1. Internet
	2. WAN
LAN

What type of network could connect an office in one building to another office in a building a few streets away?

	1. Internet
	2. WAN
	3. LAN

What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

	1. Internet
	2. WAN
	3. LAN

2. MAC and IP address

Questions:

What is a MAC address?

	1. The name of a network interface
	2. The unique identifier of a network interface
	3. A network interface

What is an IP address?

	1. Is to devices connected to a network what postal address is to houses
	2. The unique identifier of a network interface
	3. Is a number that network devices use to connect to networks

3. UDP and TCP

Questions:

	Which statement is correct for the TCP box:
		1. It is a protocol that is transferring data in a slow way but surely
		2. It is a protocol that is transferring data in a fast way and might loss data along in the process

	Which statement is correct for the UDP box:

		1. It is a protocol that is transferring data in a slow way but surely
		2. It is a protocol that is transferring data in a fast way and might loss data along in the process

	Which statement is correct for the TCP worker:
		1. Have you received boxes x, y, z?
		2. May I increase the rate at which I am sending you boxes?

4. TCP and UDP ports

Write a Bash script that displays listening ports:

	That only shows listening sockets
	That shows the PID and name of the program to which each socket belongs

5. Is the host on the network

The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command ping uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.

Write a Bash script that pings an IP address passed as an argument.

Requirements:

	Accepts a string as an argument
	Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
	Ping the IP 5 times
