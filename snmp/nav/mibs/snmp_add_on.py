from twisted.internet import defer
import inspect


class SnmpAddOn:

    def get_indexed_system_sensor(self, index, mib_object, unit_of_measurement, precision=0, scale=None, minimum=0, maximum=100):
        module_name = self.get_module_name()
        oid = '{}.{}'.format(str(self.nodes[mib_object].oid), str(index))
        internal_name = '{}.{}'.format(str(index), mib_object) if index > 0 else mib_object
        name = internal_name
        description = internal_name
        result = dict(
            mib=module_name,
            oid=oid,
            name=name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=precision,
            scale=scale,
            minimum=minimum,
            maximum=maximum
        )
        return result

    def get_double_indexed_system_sensor(self, index1, index2, mib_object, unit_of_measurement, precision=0, scale=None, minimum=0, maximum=100):
        module_name = self.get_module_name()
        oid = '{}.{}.{}'.format(str(self.nodes[mib_object].oid), str(index1), str(index2))
        internal_name = '{}.{}.{}'.format(str(index1), str(index2), mib_object)
        name = internal_name
        description = internal_name
        result = dict(
            mib=module_name,
            oid=oid,
            name=name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=precision,
            scale=scale,
            minimum=minimum,
            maximum=maximum
        )
        return result

    def get_system_sensor(self, mib_object, unit_of_measurement, precision=0, scale=None, minimum=0, maximum=100):
        result = self.get_indexed_system_sensor(0, mib_object, unit_of_measurement, precision, scale, minimum, maximum)
        return result

    def get_port_sensor(self, port, mib_object, unit_of_measurement, precision=0, scale=None, minimum=0, maximum=100):
        module_name = self.get_module_name()
        oid = '{}.{}'.format(str(self.nodes[mib_object].oid), str(port))
        internal_name = '{}.{}'.format(str(port), mib_object)
        name = internal_name
        description = internal_name
        result = dict(
            mib=module_name,
            oid=oid,
            ifindex=port,
            name=name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=precision,
            scale=scale,
            minimum=minimum,
            maximum=maximum
        )
        return result

    def get_grouped_port_sensor(self, group, port, mib_object, unit_of_measurement, precision=0, scale=None, minimum=0, maximum=100):
        module_name = self.get_module_name()
        oid = '{}.{}.{}'.format(str(self.nodes[mib_object].oid), str(group), str(port))
        internal_name = '{}.{}.{}'.format(str(group), str(port), mib_object)
        name = internal_name
        description = internal_name
        result = dict(
            mib=module_name,
            oid=oid,
            ifindex=port,
            name=name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=precision,
            scale=scale,
            minimum=minimum,
            maximum=maximum
        )
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno, type(this).__name__, inspect.stack()[1].function)
