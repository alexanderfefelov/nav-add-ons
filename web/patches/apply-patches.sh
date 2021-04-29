#!/bin/sh

# Exit immediately if a pipeline, which may consist of a single simple command,
# a list, or a compound command returns a non-zero status
set -e

NAV_HOME=${NAV_HOME:?undefined}
readonly NAV_VERSION=90d9a11

echo Patching NAV $NAV_VERSION at $NAV_HOME...
patch $NAV_HOME/models/manage.py            /nav-add-ons/web/patches/nav/models/manage.py-$NAV_VERSION.patch
patch $NAV_HOME/web/info/searchproviders.py /nav-add-ons/web/patches/nav/web/info/searchproviders.py-$NAV_VERSION.patch
patch $NAV_HOME/web/info/room/views.py      /nav-add-ons/web/patches/nav/web/info/room/views.py-$NAV_VERSION.patch
echo ...done
