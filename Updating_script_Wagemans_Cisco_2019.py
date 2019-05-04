#!/usr/bin/env python
from __future__ import print_function
import sys
import json
import os

from dnac_config import DNAC_DEVICE_TYPE, DNAC_NEW_VERSION, DNAC_UPDATE_TAG
from util import get_url, tagmapping
from tag import add_tag, device2id
from distribute import distribute, validate, imageName2id, activate
from list_images import get_images



def list_single_device(ip):
    return get_url("network-device/ip-address/%s" % ip)

def list_network_devices():
    return get_url("network-device")

deviceIP_to_update = []



if __name__ == "__main__":
    os.system('clear')



    if len(sys.argv) > 1:
        response = list_single_device(sys.argv[1])
        print(json.dumps(response, indent=2))
    else:
        print("Device type : {0}\n".format(DNAC_DEVICE_TYPE))
        print("Update Name {0}\n".format(DNAC_NEW_VERSION))

        response = list_network_devices()
        print("{0:35}{1:50}{2:17}{3:12}{4:18}{5:20}{6:12}{7:16}{8:15}".
                  format("hostname", "type","mgmt IP","serial",
                         "platformId","SW Version","SW Type","role","Uptime"))
        
        
        
        for device in response['response']:
            uptime = "N/A" if device['upTime'] is None else device['upTime']
            print('{0:35}{1:50}{2:17}{3:12}{4:18}{5:20}{6:12}{7:16}{8:15}'.
                  format(device['hostname'],
                         device['type'],
                         device['managementIpAddress'],
                         device['serialNumber'],
                         device['platformId'],
                         device['softwareVersion'],
                         device['softwareType'],
                         device['role'],uptime))


            #corresponding type ?
            if device['type'] == DNAC_DEVICE_TYPE:
                # do the nevice need to be update ?
                if device['softwareVersion'] == DNAC_NEW_VERSION:
                    deviceIP_to_update.append(device['managementIpAddress'])


        imageFound = get_images(imageName = DNAC_NEW_VERSION) 

        # does the version exists ?
        if (imageFound == 1):
            # adding a tag to each device needing an update
            add_tag(DNAC_UPDATE_TAG, deviceIP_to_update)
        else:
            print("\nThe image name does not exist")


        #All the devices that must be update are now tagged -> distribute the image
        if(imageFound == 1):
            deviceIds = tagmapping(DNAC_UPDATE_TAG)
            imageId = imageName2id(DNAC_NEW_VERSION)
            validate(imageId, *deviceIds)
            distribute(imageId, *deviceIds)
            activate (imageId, *deviceIds)




