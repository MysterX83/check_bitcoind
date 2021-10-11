#!/usr/bin/env python3

""" CheckMK agent plugin

    Checks if the bitcoin deamon is running.

    @author: mysterx
"""
import sys
import os
import argparse

# *************************************************************************** #
# Constants
# *************************************************************************** #

# check mk constants
CHECK_MK_OK      = '0'
CHECK_MK_WARN    = '1'
CHECK_MK_CRIT    = '2'
CHECK_MK_UNKNOWN = '3'

SERVICE_NAME = 'node-check-deamon'

EXPECTED_CONTENT = 'Nr of POLL commands failed'

# *************************************************************************** #
# Global Variables
# *************************************************************************** #


# *************************************************************************** #
# Functions
# *************************************************************************** #

# *************************************************************************** #
#   _parseargs
#
def _parseargs():
    """ Checks if the needed arguments are present and valid. Otherwise default
        values are used.
        return  the (updated) arguments
    """

    parser = argparse.ArgumentParser(description='Retrieves the deamon to be checked')
    parser.add_argument("-D", "--deamon", dest="deamonname", default="bitcoind",
                      help="The name of the deamon to be checked")

    args = parser.parse_args()
    return args


def _runcommand(deamonName):

    stat = os.system('service ' + deamonName + ' status > /dev/null')
    return stat

# *************************************************************************** #
#   main

def main():
    metrics = '-'
    details = ''
    status  = CHECK_MK_OK

    options = _parseargs()
    result = _runcommand(options.deamonname)
    details = 'Deamon ' + options.deamonname + ' is running.'

    if result != 0:
        status = CHECK_MK_CRIT
        details = 'Deamon ' + options.deamonname + ' not running.'

    print ('%s \"%s\" %s %s' %(status, SERVICE_NAME, metrics, details))

if __name__ == "__main__":
    main()
