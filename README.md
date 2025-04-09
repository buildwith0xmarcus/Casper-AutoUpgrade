

This guide is prepared for the test network. Different configurations may be required for the Mainnet.

## Install Python3:
<code>sudo apt-get update </code>  <br>
<code>sudo apt-get install python3 </code> 
## Create the project folder and move into it:

<code>mkdir casper-upgrade </code> <br>
<code>cd casper-upgrade </code> 
## Create the .env file and enter NODE_IP address:

<code>echo "NODE_IP=<node_ip_address>" > .env </code>  <br>
* Note: Replace <node_ip_address> with your own node IP address.

## Download and run the get_peers.py file:

<code>wget https://raw.githubusercontent.com/NetworkStake/Casper-AutoUpgrade/main/get_peers.py</code>  <br>
<code>python3 get_peers.py </code>  <br>
* This command will create a file named peers.json. <br>

## Download and run the upgrade.py file:


<code>wget https://raw.githubusercontent.com/NetworkStake/Casper-AutoUpgrade/main/upgrade.py </code>  <br>
<code>python3 upgrade.py</code>  <br>
* This command will check the version of other peers and automatically update if necessary. <br>

* The upgrade.py file uses the peers.json file to check the versions of other peers. You don't need to update this file manually. The file is automatically updated by get_peers.py. <br>

* When you follow these steps, the upgrade.py file will check the versions of other peers and automatically update if necessary.
