#!/usr/bin/env python
from __future__ import print_function
import sys
import json
import logging
from argparse import ArgumentParser

from util import get_url, post_and_wait



def get_images(imageName=None):
    i = 0
    if imageName:
        url='image/importation?imageName={0}'.format(imageName)
    else:
        url='image/importation'
    response = []
    response = get_url(url)


    for image in response['response']:
        i = i + 1

    return i


if __name__ ==  "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('--pattern', type=str, required=False,
                        help="show devices that match pattern")

    args = parser.parse_args()
    get_images(args.pattern)
