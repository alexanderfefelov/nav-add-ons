#!/bin/sh

# Exit immediately if a pipeline, which may consist of a single simple command,
# a list, or a compound command returns a non-zero status
set -e

NAV_HOME=${NAV_HOME:?undefined}
readonly NAV_VERSION=90d9a11

echo Patching NAV $NAV_VERSION at $NAV_HOME...
patch $NAV_HOME/ipdevpoll/neighbor.py           /nav-add-ons/snmp/patches/nav/ipdevpoll/neighbor.py-$NAV_VERSION.patch
patch $NAV_HOME/ipdevpoll/plugins/interfaces.py /nav-add-ons/snmp/patches/nav/ipdevpoll/plugins/interfaces.py-$NAV_VERSION.patch
patch $NAV_HOME/ipdevpoll/plugins/sensors.py    /nav-add-ons/snmp/patches/nav/ipdevpoll/plugins/sensors.py-$NAV_VERSION.patch
patch $NAV_HOME/ipdevpoll/plugins/statsystem.py /nav-add-ons/snmp/patches/nav/ipdevpoll/plugins/statsystem.py-$NAV_VERSION.patch
patch $NAV_HOME/ipdevpoll/shadows/__init__.py   /nav-add-ons/snmp/patches/nav/ipdevpoll/shadows/__init__.py-$NAV_VERSION.patch
patch $NAV_HOME/mibs/if_mib.py                  /nav-add-ons/snmp/patches/nav/mibs/if_mib.py-$NAV_VERSION.patch
echo ...done
