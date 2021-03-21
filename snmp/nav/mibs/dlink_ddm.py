from nav.mibs.dlink import DLink
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib


class DLink_Ddm_Mib(MibRetriever, DLink):
    mib = get_mib('D_Link_DDM_mib')
    GUARD_OID = 'swDdmTrapState'
    GET_DDM_SENSORS = 'get_ddm_sensors_old'
