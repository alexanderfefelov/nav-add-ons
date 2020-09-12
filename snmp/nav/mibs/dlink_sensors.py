from nav.mibs.dlink_ddm import DLinkDdmMib
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

    @defer.inlineCallbacks
    def get_all_sensors(self):
        equipment_sensors = yield self.equipment_mib.get_all_sensors()
        ddm_sensors = yield self.ddm_mib.get_all_sensors()
        result = equipment_sensors + ddm_sensors
        defer.returnValue(result)
