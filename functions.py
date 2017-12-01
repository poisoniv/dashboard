from meraki import meraki
from config import *


def fetch():
    networks = get_networks()
    network_statuses = []
    for network in networks:
        network_statuses.append(get_network_status(network))
    return network_statuses


def get_networks():
    networks = meraki.getnetworklist(config['api_key'], config['org_id'], suppressprint=True)
    return networks


# Create output file named output.txt
# output_file = open("output.txt", "w")

# iterate through each device in each network, check status of device/uplink and set variable 'network_status' to
# "Down" if applicable if device/uplink is down, skip rest of loop, print findings, and continue with next network
def get_network_status(network):
    network_status = "Up";
    devices = meraki.getnetworkdevices(config['api_key'], network['id'], suppressprint=True)
    for device in devices:
        if network_status == "Down": return (network['name'], network_status)
        uplinks = meraki.getdeviceuplink(config['api_key'], network['id'], device['serial'], suppressprint=True)
        for uplink in uplinks:
            if uplink['status'] == "Failed":
                network_status = "Down"
                return {"name": network['name'], "status": network_status}
    return {"name": network['name'], "status": network_status}


# for network in networks :
#     network_status = "Up";
#     devices = meraki.getnetworkdevices(api_key, network['id'], suppressprint=True)
#     for device in devices:
#         if network_status == "Down" : break
#         uplinks = meraki.getdeviceuplink(api_key, network['id'], device['serial'],suppressprint=True)
#         for uplink in uplinks :
#             if (uplink['status'] == "Failed") :
#                 network_status = "Down"
#                 break

    #print status of each network to console and output.txt
#     print(network['name'] + " - " + network_status)
#     output_file.write(network['name'] + " - " + network_status + "\n")
#
# output_file.close()

#print("Executed successfully...")

#print(fetch())