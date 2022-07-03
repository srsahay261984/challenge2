#!/usr/bin/env python
import requests
import json
import sys


def get_metadata(userkey):
    awsurl = 'http://169.254.169.254/latest/meta-data/'
    metadata = {}
    trav_data(awsurl, metadata, userkey)
    return metadata


def trav_data(awsurl, metadata, userkey):
    req = requests.get(awsurl)
    if req.status_code == 404:
        return

    for line in req.text.split('\n'):
        if not line:
            continue

        newurl = '{0}{1}'.format(awsurl, line)
        if line.endswith('/'):
            newsection = line.split('/')[-2]
            if userkey is None:
                metadata[newsection] = {}
                trav_data(newurl, metadata[newsection], userkey)
            else:
                trav_data(newurl, metadata, userkey)
        else:
            req = requests.get(newurl)
            if req.status_code != 404:
                if userkey is not None:
                    if userkey==line:
                        metadata[line] = req.text
                        break
                else:
                    try:
                        metadata[line] = json.loads(req.text)
                    except ValueError:
                        metadata[line] = req.text
            else:
                metadata[line] = None

if __name__ == "__main__":
    arguments = sys.argv
    arglength = len(arguments)
    userkey = None
    if arglength > 1:
        userkey = arguments[1]
    print(json.dumps(get_metadata(userkey)))
