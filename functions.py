from meraki import meraki

#Pull API Key from file
file = open("api_key.txt", "r")
api_key = file.read()
#api_key = [insert here]
#print(api_key)

#pull Org ID from file
file = open("org_id.txt", "r")
org_id = file.read()
#org_id = '316511'
#print(org_id)

#Retrieve list of networks in organization
def get_networks(api_key, org_id) :
    networks = meraki.getnetworklist(api_key, org_id, suppressprint=True)
    return networks


#networks = meraki.getnetworklist(api_key, org_id, suppressprint=True)

#Create output file named output.txt
#output_file = open("output.txt", "w")

#iterate through each device in each network, check status of device/uplink and set variable 'network_status' to "Down" if applicable
#if device/uplink is down, skip rest of loop, print findings, and continue with next network
def get_network_status(network) :
    network_status = "Up";
    devices = meraki.getnetworkdevices(api_key, network['id'], suppressprint=True)
    for device in devices:
        if network_status == "Down": return network_status
        uplinks = meraki.getdeviceuplink(api_key, network['id'], device['serial'], suppressprint=True)
        for uplink in uplinks:
            if (uplink['status'] == "Failed"):
                network_status = "Down"
                return network_status
    return network_status


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