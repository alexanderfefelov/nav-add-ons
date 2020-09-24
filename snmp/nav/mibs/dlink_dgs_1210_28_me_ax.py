from nav.mibs.dlink_dgs_1210_xx import DLink_DGS_1210_XX
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib


class DLink_DGS_1210_28_ME_AX_Mib(MibRetriever, DLink_DGS_1210_XX):
    mib = get_mib('D_Link_DGS_1210_28ME_AX_6_14_001_mib')
    ROOT_OID = 'dgs-1210-28meax'
    GET_DDM_SENSORS = 'get_ddm_sensors'
    GET_FAN_SENSORS = 'empty'
    GET_PORTS_POE_SENSORS = 'empty'
    GET_POWER_SENSORS = 'empty'
    GET_SYSTEM_POE_SENSORS = 'empty'
    GET_TEMPERATURE_SENSORS = 'empty'
