class SnmpAddOn:

    def get_indexed_system_sensor(self, index, sensor_name,
                                  unit_of_measurement, precision=0, scale=None,
                                  minimum=0, maximum=100):
        module_name = self.get_module_name()
        oid = str(self.nodes[sensor_name].oid) + '.' + str(index)
        internal_name = '{}.{}'.format(sensor_name, str(index)) if index > 0 else sensor_name
        description = internal_name
        result = dict(
            mib=module_name,
            oid=oid,
            name=internal_name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=precision,
            scale=scale,
            minimum=minimum,
            maximum=maximum
        )
        return result

    def get_system_sensor(self, sensor_name,
                          unit_of_measurement, precision=0, scale=None,
                          minimum=0, maximum=100):
        result = self.get_indexed_system_sensor(0, sensor_name,
                                                unit_of_measurement, precision, scale,
                                                minimum, maximum)
        return result

    def get_port_sensor(self, port, sensor_name,
                        unit_of_measurement, precision=0, scale=None,
                        minimum=0, maximum=100):
        module_name = self.get_module_name()
        oid = str(self.nodes[sensor_name].oid) + '.' + str(port)
        internal_name = '{}.{}'.format(sensor_name, str(port))
        description = internal_name
        result = dict(
            mib=module_name,
            oid=oid,
            ifindex=port,
            name=internal_name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=precision,
            scale=scale,
            minimum=minimum,
            maximum=maximum
        )
        return result

    def get_grouped_port_sensor(self, group, port, sensor_name,
                                unit_of_measurement, precision=0, scale=None,
                                minimum=0, maximum=100):
        module_name = self.get_module_name()
        oid = str(self.nodes[sensor_name].oid) + '.' + str(group) + '.' + str(port)
        internal_name = '{}.{}.{}'.format(sensor_name, str(group), str(port))
        description = internal_name
        result = dict(
            mib=module_name,
            oid=oid,
            ifindex=port,
            name=internal_name,
            internal_name=internal_name,
            description=description,
            unit_of_measurement=unit_of_measurement,
            precision=precision,
            scale=scale,
            minimum=minimum,
            maximum=maximum
        )
        return result
