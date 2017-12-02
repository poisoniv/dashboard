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


def get_network_status(network):
    """
    Iterate through each device in each network, check status of device/uplink and set variable 'network_status' to
    "Down" if applicable if device/uplink is down, skip rest of loop, print findings, and continue with next network

    Args:
        network:

    Returns:
        A dictionary containing the network name and status.
    """
    network_status = "Up"
    devices = meraki.getnetworkdevices(config['api_key'], network['id'], suppressprint=True)
    for device in devices:
        if network_status == "Down":
            break
        uplinks = meraki.getdeviceuplink(config['api_key'], network['id'], device['serial'], suppressprint=True)
        for uplink in uplinks:
            if uplink['status'] == "Failed":
                network_status = "Down"
                break
    return {"name": network['name'], "status": network_status}