import os

DNAC=os.environ.get('DNAC','sandboxdnac.cisco.com')
DNAC_PORT=os.environ.get('DNAC_PORT',443)
DNAC_USER=os.environ.get('DNAC_USER','devnetuser')
DNAC_PASSWORD=os.environ.get('DNAC_PASSWORD','Cisco123!')

DNAC_DEVICE_TYPE=os.environ.get('DNAC_UPDATE','Cisco Catalyst 9300 Switch')
DNAC_NEW_VERSION=os.environ.get('DNAC_NEW_VERSION','cat9k_iosxe.16.09.02.SPA.bin')
DNAC_UPDATE_TAG=os.environ.get('DNAC_UPDATE_TAG','cat9k_update')