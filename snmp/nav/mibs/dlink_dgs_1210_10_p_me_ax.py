from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib


class DLink_DGS_1210_10_P_ME_AX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_10PME_AX_6_13_017_mib')
    ROOT_OID = 'dgs-1210-10pmeax'
    GET_DDM_SENSORS = 'get_ddm_sensors'
    GET_PORTS_POE_SENSORS = 'get_ports_poe_sensors'
    GET_SYSTEM_POE_SENSORS = 'get_system_poe_sensors'
