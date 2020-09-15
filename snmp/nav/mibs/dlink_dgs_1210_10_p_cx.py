from nav.mibs.dlink_dgs_1210_xx import _DLink_DGS_1210_XX_Mib
from nav.smidumps import get_mib


class DLink_DGS_1210_10_P_CX_Mib(_DLink_DGS_1210_XX_Mib):
    mib = get_mib('D_Link_DGS_1210_10P_CX_4_10_002_mib')

    def _get_ddm_columns(self):
        return []

    def _get_ddm_sensors(self, data):
        return []
