import inspect


class SnmpAddOn:

    def get_indexed_system_sensor(self, index, sensor_name,
                                  unit_of_measurement, precision=0, scale=None,
                                  display_minimum_user=0, display_maximum_user=100):
        self._logger.debug(here(self))
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
            display_minimum_user=display_minimum_user,
            display_maximum_user=display_maximum_user
        )
        self._logger.debug(str(result))
        return result

    def get_system_sensor(self, sensor_name,
                          unit_of_measurement, precision=0, scale=None,
                          display_minimum_user=0, display_maximum_user=100):
        self._logger.debug(here(self))
        result = self.get_indexed_system_sensor(0, sensor_name,
                                                unit_of_measurement, precision, scale,
                                                display_minimum_user, display_maximum_user)
        self._logger.debug(str(result))
        return result

    def get_port_sensor(self, port, sensor_name,
                        unit_of_measurement, precision=0, scale=None,
                        display_minimum_user=0, display_maximum_user=100):
        self._logger.debug(here(self))
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
            display_minimum_user=display_minimum_user,
            display_maximum_user=display_maximum_user
        )
        self._logger.debug(str(result))
        return result

    def get_grouped_port_sensor(self, group, port, sensor_name,
                                unit_of_measurement, precision=0, scale=None,
                                display_minimum_user=0, display_maximum_user=100):
        self._logger.debug(here(self))
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
            display_minimum_user=display_minimum_user,
            display_maximum_user=display_maximum_user
        )
        self._logger.debug(str(result))
        return result


here = lambda this: 'here: {}:{} {}.{}'.format(inspect.stack()[1].filename, inspect.stack()[1].lineno,
                                               type(this).__name__, inspect.stack()[1].function)
