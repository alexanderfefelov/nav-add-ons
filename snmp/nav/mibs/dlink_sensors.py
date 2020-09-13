from nav.mibs.dlink_ddm import DLinkDdmMib
from nav.mibs.dlink_dgs_1210_xx import (
    DLink_DGS_1210_10_ME_AX_Mib,
    DLink_DGS_1210_10_ME_BX_Mib,
    DLink_DGS_1210_10_P_CX_Mib,
    DLink_DGS_1210_10_P_ME_AX_Mib,
    DLink_DGS_1210_10_P_ME_BX_Mib,
    DLink_DGS_1210_12_TS_ME_BX_Mib,
    DLink_DGS_1210_28_ME_AX_Mib,
    DLink_DGS_1210_28_ME_BX_Mib,
    DLink_DGS_1210_28_XS_ME_BX_Mib,
    DLink_DGS_1210_52_ME_BX_Mib
)
from nav.mibs.dlink_equipment import DLinkEquipmentMib
from nav.mibs.mibretriever import MibRetriever
from nav.smidumps import get_mib
from twisted.internet import defer


class DLinkSensorsMib(MibRetriever):
    mib = get_mib('ENTITY-MIB')  # TODO FIXME Hack the "No known MIB implementation" error

    def __init__(self, agent_proxy):
        super(DLinkSensorsMib, self).__init__(agent_proxy)
        self.equipment_mib = DLinkEquipmentMib(agent_proxy)
        self.ddm_mib = DLinkDdmMib(agent_proxy)
        self.dgs_1210_10_me_ax_mib = DLink_DGS_1210_10_ME_AX_Mib(agent_proxy)
        self.dgs_1210_10_me_bx_mib = DLink_DGS_1210_10_ME_BX_Mib(agent_proxy)
        self.dgs_1210_10_p_cx_mib = DLink_DGS_1210_10_P_CX_Mib(agent_proxy)
        self.dgs_1210_10_p_me_ax_mib = DLink_DGS_1210_10_P_ME_AX_Mib(agent_proxy)
        self.dgs_1210_10_p_me_bx_mib = DLink_DGS_1210_10_P_ME_BX_Mib(agent_proxy)
        self.dgs_1210_12_ts_me_bx_mib = DLink_DGS_1210_12_TS_ME_BX_Mib(agent_proxy)
        self.dgs_1210_28_me_ax_mib = DLink_DGS_1210_28_ME_AX_Mib(agent_proxy)
        self.dgs_1210_28_me_bx_mib = DLink_DGS_1210_28_ME_BX_Mib(agent_proxy)
        self.dgs_1210_28_xs_me_bx_mib = DLink_DGS_1210_28_XS_ME_BX_Mib(agent_proxy)
        self.dgs_1210_52_me_bx_mib = DLink_DGS_1210_52_ME_BX_Mib(agent_proxy)

    @defer.inlineCallbacks
    def get_all_sensors(self):
        equipment_sensors = yield self.equipment_mib.get_all_sensors()
        ddm_sensors = yield self.ddm_mib.get_all_sensors()
        dgs_1210_10_me_ax_sensors = yield self.dgs_1210_10_me_ax_mib.get_all_sensors()
        dgs_1210_10_me_bx_sensors = yield self.dgs_1210_10_me_bx_mib.get_all_sensors()
        dgs_1210_10_p_cx_sensors = yield self.dgs_1210_10_p_cx_mib.get_all_sensors()
        dgs_1210_10_p_me_ax_sensors = yield self.dgs_1210_10_p_me_ax_mib.get_all_sensors()
        dgs_1210_10_p_me_bx_sensors = yield self.dgs_1210_10_p_me_bx_mib.get_all_sensors()
        dgs_1210_12_ts_me_bx_sensors = yield self.dgs_1210_12_ts_me_bx_mib.get_all_sensors()
        dgs_1210_28_me_ax_sensors = yield self.dgs_1210_28_me_ax_mib.get_all_sensors()
        dgs_1210_28_me_bx_sensors = yield self.dgs_1210_28_me_bx_mib.get_all_sensors()
        dgs_1210_28_xs_me_bx_sensors = yield self.dgs_1210_28_xs_me_bx_mib.get_all_sensors()
        dgs_1210_52_me_bx_sensors = yield self.dgs_1210_52_me_bx_mib.get_all_sensors()
        result = []
        result.extend(equipment_sensors)
        result.extend(ddm_sensors)
        result.extend(dgs_1210_10_me_ax_sensors)
        result.extend(dgs_1210_10_me_bx_sensors)
        result.extend(dgs_1210_10_p_cx_sensors)
        result.extend(dgs_1210_10_p_me_ax_sensors)
        result.extend(dgs_1210_10_p_me_bx_sensors)
        result.extend(dgs_1210_12_ts_me_bx_sensors)
        result.extend(dgs_1210_28_me_ax_sensors)
        result.extend(dgs_1210_28_me_bx_sensors)
        result.extend(dgs_1210_28_xs_me_bx_sensors)
        result.extend(dgs_1210_52_me_bx_sensors)
        defer.returnValue(result)
