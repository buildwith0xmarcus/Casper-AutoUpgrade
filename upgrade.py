import json
import time
import requests
import subprocess
import os

currentVersion = None

while True:
    try:
        with open('peers.json', 'r') as f:
            data = json.load(f)
            data_length = len(data)

            for peer in data:
                id = peer['node_id']
                ip = peer['address'].split(':')[0]
                url = 'http://{}:8888/status'.format(ip)
                response = requests.get(url)

                if response.status_code != 200:
                    print(f"Request failed with status code {response.status_code}")
                    continue

                try:
                    peer_ = json.loads(response.content)
                except json.JSONDecodeError as e:
                    print(f"Failed to decode JSON: {e}")
                    continue

                api = peer_["api_version"]
                newpeers = peer_["peers"]
                nextUpgrade = peer_["next_upgrade"]

                message = f'Checking version in node: {ip}'
                peer_id = f'Node Id: {id}'
                peer_api = f'Api Version: {api}'
                peer_upgrade = f'Upgrade : {nextUpgrade}'

                print(message)
                print(peer_id)
                print(peer_api)

                if nextUpgrade != None:
                    print(nextUpgrade)
                    print("Update Already Staged...")
                if nextUpgrade == None:
                    print("Latest Version")
                else:
                    if currentVersion != nextUpgrade["protocol_version"]:
                        version_ = nextUpgrade["protocol_version"]
                        version_ = version_.replace(".", "_")
                        url = f'https://genesis.casperlabs.io/casper/{version_}/stage_upgrade.sh'
                        response = requests.get(url)
                        with open('stage_upgrade.sh', 'wb') as f:
                            f.write(response.content)

                        subprocess.run(['sudo','bash', 'stage_upgrade.sh'])
                        currentVersion = nextUpgrade["protocol_version"]
                        print("Update Success")

                        if os.path.isfile('stage_upgrade.sh'):
                            os.remove('stage_upgrade.sh')
                            with open('peers.json', 'w') as f:
                                json.dump(peer_["peers"], f)
                                print("Peer data update...")

                time.sleep(1)
                print(f'Current Version : {currentVersion}')
                print("*/*/*/*/*/*/*/*/*/*/")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        print("*/*/*/*/*/*/*/*/*/*/")
        continue

    time.sleep(5)
