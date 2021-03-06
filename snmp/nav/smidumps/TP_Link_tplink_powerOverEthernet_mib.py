# python version 1.0						DO NOT EDIT
#
# Generated by smidump version 0.4.8:
#
#   smidump -f python TPLINK-POWER-OVER-ETHERNET-MIB

FILENAME = "mibs/TP-Link/tplink-powerOverEthernet.mib"

MIB = {
    "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",

    "TPLINK-POWER-OVER-ETHERNET-MIB" : {
        "nodetype" : "module",
        "language" : "SMIv2",
        "organization" :    
            """TP-LINK""",
        "contact" : 
            """ www.tplink.com.cn""",
        "description" :
            """Private MIB for PoE module.""",
        "revisions" : (
            {
                "date" : "2013-07-03 00:00",
                "description" :
                    """Initial version of this MIB module.""",
            },
        ),
        "identity node" : "tplinkPowerOverEthernetMIB",
    },

    "imports" : (
        {"module" : "SNMPv2-SMI", "name" : "MODULE-IDENTITY"},
        {"module" : "SNMPv2-SMI", "name" : "OBJECT-TYPE"},
        {"module" : "SNMPv2-SMI", "name" : "MODULE-IDENTITY"},
        {"module" : "SNMPv2-SMI", "name" : "NOTIFICATION-TYPE"},
        {"module" : "TPLINK-MIB", "name" : "tplinkMgmt"},
    ),

    "nodes" : {
        "tplinkPowerOverEthernetMIB" : {
            "nodetype" : "node",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56",
            "status" : "current",
        }, # node
        "tplinkPoeMIBObjects" : {
            "nodetype" : "node",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1",
        }, # node
        "tpPoeConfig" : {
            "nodetype" : "node",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1",
        }, # node
        "tpPoeGlobal" : {
            "nodetype" : "node",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.1",
        }, # node
        "tpSystemPowerLimit" : {
            "nodetype" : "scalar",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.1.1",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "1",
                        "max" : "3200"
                    },
                    ],
                    "range" : {
                        "min" : "1",
                        "max" : "3200"
                    },
                },
            },
            "access" : "readwrite",
            "description" :
                """Define max power the PoE switch supply. The unit is 0.1W.""",
        }, # scalar
        "tpPowerDisconnectMethod" : {
            "nodetype" : "scalar",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.1.2",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Enumeration",
                    "deny-lower-priority" : {
                        "nodetype" : "namednumber",
                        "number" : "1"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """The PoE Switch use this method to offset the power 
limit being exceeded and keep the switch system using 
power at a usable level.""",
        }, # scalar
        "tpSystemPowerConsumption" : {
            "nodetype" : "scalar",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.1.3",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "1",
                        "max" : "3200"
                    },
                    ],
                    "range" : {
                        "min" : "1",
                        "max" : "3200"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Display the PoE switch's real time system power consumption. The unit is 0.1W.""",
        }, # scalar
        "tpSystemPowerRemain" : {
            "nodetype" : "scalar",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.1.4",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "1",
                        "max" : "3200"
                    },
                    ],
                    "range" : {
                        "min" : "1",
                        "max" : "3200"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Display the PoE switch's real time remaining system power. The unit is 0.1W.""",
        }, # scalar
        "tpPoePort" : {
            "nodetype" : "node",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2",
        }, # node
        "tpPoePortConfigTable" : {
            "nodetype" : "table",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1",
            "status" : "current",
            "description" :
                """A list of PoE entries.
Here you can configure the PoE feature on each port.""",
        }, # table
        "tpPoePortConfigEntry" : {
            "nodetype" : "row",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1",
            "status" : "current",
            "linkage" : [
                "tpPoePortIndex",
            ],
            "description" :
                """An entry contains of the configuration and information of poe port.""",
        }, # row
        "tpPoePortIndex" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.1",
            "status" : "current",
            "syntax" : {
                "type" : { "module" :"", "name" : "Integer32"},
            },
            "access" : "readonly",
            "description" :
                """The port number of the Switch.""",
        }, # column
        "tpPoePortStatus" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.2",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Enumeration",
                    "disable" : {
                        "nodetype" : "namednumber",
                        "number" : "0"
                    },
                    "enable" : {
                        "nodetype" : "namednumber",
                        "number" : "1"
                    },
                },
            },
            "access" : "readwrite",
            "description" :
                """Select to disable/enable the PoE feature
for the corresponding port. If set enable,
the corresponding port can supply power to
 the linked PD (Powered Device).""",
        }, # column
        "tpPoePriority" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.3",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Enumeration",
                    "high" : {
                        "nodetype" : "namednumber",
                        "number" : "0"
                    },
                    "middle" : {
                        "nodetype" : "namednumber",
                        "number" : "1"
                    },
                    "low" : {
                        "nodetype" : "namednumber",
                        "number" : "2"
                    },
                },
            },
            "access" : "readwrite",
            "description" :
                """Cooperates with the Power Disconnected Method
to decide the way to supply power to the new 
linked PD (Powered Device) when the surplus 
power is inadequate.""",
        }, # column
        "tpPoePowerLimit" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.4",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "1",
                        "max" : "300"
                    },
                    ],
                    "range" : {
                        "min" : "1",
                        "max" : "300"
                    },
                },
            },
            "access" : "readwrite",
            "description" :
                """Defines the max power the corresponding port can supply.The unit is 0.1W""",
        }, # column
        "tpPoePortTimeRangeName" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.5",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readwrite",
            "description" :
                """Select time range by entering its name.""",
        }, # column
        "tpPoePortProfileName" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.6",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readwrite",
            "description" :
                """Select profile by entering its name. """,
        }, # column
        "tpPoePower" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.7",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "1",
                        "max" : "300"
                    },
                    ],
                    "range" : {
                        "min" : "1",
                        "max" : "300"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """ Displays the port's real time power supply in 0.1W.""",
        }, # column
        "tpPoeCurrent" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.8",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "1",
                        "max" : "1000"
                    },
                    ],
                    "range" : {
                        "min" : "1",
                        "max" : "1000"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """ Displays the port's real time current in 1mA.""",
        }, # column
        "tpPoeVoltage" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.9",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "1",
                        "max" : "300"
                    },
                    ],
                    "range" : {
                        "min" : "1",
                        "max" : "300"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """ Displays the port's real time voltage in 0.1V.""",
        }, # column
        "tpPoeClass" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.10",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Enumeration",
                    "class0" : {
                        "nodetype" : "namednumber",
                        "number" : "0"
                    },
                    "class1" : {
                        "nodetype" : "namednumber",
                        "number" : "1"
                    },
                    "class2" : {
                        "nodetype" : "namednumber",
                        "number" : "2"
                    },
                    "class3" : {
                        "nodetype" : "namednumber",
                        "number" : "3"
                    },
                    "class4" : {
                        "nodetype" : "namednumber",
                        "number" : "4"
                    },
                    "class-not-defined" : {
                        "nodetype" : "namednumber",
                        "number" : "7"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """ Displays the class the linked PD (Powered Device) belongs to.""",
        }, # column
        "tpPoePowerStatus" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.1.2.1.1.11",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Enumeration",
                    "off" : {
                        "nodetype" : "namednumber",
                        "number" : "0"
                    },
                    "turning-on" : {
                        "nodetype" : "namednumber",
                        "number" : "1"
                    },
                    "on" : {
                        "nodetype" : "namednumber",
                        "number" : "2"
                    },
                    "overload" : {
                        "nodetype" : "namednumber",
                        "number" : "3"
                    },
                    "short" : {
                        "nodetype" : "namednumber",
                        "number" : "4"
                    },
                    "nonstandard-pd" : {
                        "nodetype" : "namednumber",
                        "number" : "5"
                    },
                    "voltage-high" : {
                        "nodetype" : "namednumber",
                        "number" : "6"
                    },
                    "voltage-low" : {
                        "nodetype" : "namednumber",
                        "number" : "7"
                    },
                    "hardware-fault" : {
                        "nodetype" : "namednumber",
                        "number" : "8"
                    },
                    "overtemperature" : {
                        "nodetype" : "namednumber",
                        "number" : "9"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """ Displays the port's real time power status.""",
        }, # column
        "tpPoeProfile" : {
            "nodetype" : "node",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.2",
        }, # node
        "tpPoeProfileTable" : {
            "nodetype" : "table",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.2.1",
            "status" : "current",
            "description" :
                """A list of PoE profile entries.
Here you can define the PoE profile.""",
        }, # table
        "tpPoeProfileEntry" : {
            "nodetype" : "row",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.2.1.1",
            "status" : "current",
            "linkage" : [
                "tpPoeProfileIndex",
            ],
            "description" :
                """An entry contains of the information of PoE profile.""",
        }, # row
        "tpPoeProfileIndex" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.2.1.1.1",
            "status" : "current",
            "syntax" : {
                "type" : { "module" :"", "name" : "Integer32"},
            },
            "access" : "readonly",
            "description" :
                """The index number of the Switch.""",
        }, # column
        "tpPoeProfileName" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.2.1.1.2",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """ the name of PoE profile.""",
        }, # column
        "tpPoeProfilePortStatus" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.2.1.1.3",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Enumeration",
                    "disable" : {
                        "nodetype" : "namednumber",
                        "number" : "0"
                    },
                    "enable" : {
                        "nodetype" : "namednumber",
                        "number" : "1"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Select to disable/enable the PoE feature
for the corresponding profile. If set enable,
the port selected the profile can supply power to
 the linked PD (Powered Device).""",
        }, # column
        "tpPoeProfilePriority" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.2.1.1.4",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Enumeration",
                    "high" : {
                        "nodetype" : "namednumber",
                        "number" : "0"
                    },
                    "middle" : {
                        "nodetype" : "namednumber",
                        "number" : "1"
                    },
                    "low" : {
                        "nodetype" : "namednumber",
                        "number" : "2"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Cooperates with the Power Disconnected Method
to decide the way to supply power to the new 
linked PD (Powered Device) when the surplus 
power is inadequate.""",
        }, # column
        "tpPoeProfilePowerLimit" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.2.1.1.5",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "1",
                        "max" : "300"
                    },
                    ],
                    "range" : {
                        "min" : "1",
                        "max" : "300"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Defines the max power the corresponding port can supply.The unit is 0.1W.""",
        }, # column
        "tpPoeTimeRange" : {
            "nodetype" : "node",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.3",
        }, # node
        "tpHolidayConfig" : {
            "nodetype" : "node",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.3.2",
        }, # node
        "tpHolidayConfigTable" : {
            "nodetype" : "table",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.3.2.1",
            "status" : "current",
            "description" :
                """A list of Holiday entries. Here you can configure the Holiday.""",
        }, # table
        "tpHolidayConfigEntry" : {
            "nodetype" : "row",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.3.2.1.1",
            "status" : "current",
            "linkage" : [
                "tpHolidayIndex",
            ],
            "description" :
                """An entry s of the information of holiday.""",
        }, # row
        "tpHolidayIndex" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.3.2.1.1.1",
            "status" : "current",
            "syntax" : {
                "type" : { "module" :"", "name" : "Integer32"},
            },
            "access" : "readonly",
            "description" :
                """Index of holiday name.""",
        }, # column
        "tpHolidayName" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.3.2.1.1.2",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """The name of PoE holiday name.""",
        }, # column
        "tpHolidayStartDate" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.3.2.1.1.3",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """The start date in the format MM/DD.""",
        }, # column
        "tpHolidayEndDate" : {
            "nodetype" : "column",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.1.3.2.1.1.4",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """The end date in the format MM/DD. """,
        }, # column
        "tplinkPoeNotifications" : {
            "nodetype" : "node",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.2",
        }, # node
    }, # nodes

    "notifications" : {
        "tpPoePortPowerChange" : {
            "nodetype" : "notification",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.2.1",
            "status" : "current",
            "objects" : {
                "tpPoePortIndex" : {
                    "nodetype" : "object",
                    "module" : "TPLINK-POWER-OVER-ETHERNET-MIB"
                },
                "tpPoePortStatus" : {
                    "nodetype" : "object",
                    "module" : "TPLINK-POWER-OVER-ETHERNET-MIB"
                },
            },
            "description" :
                """A poePortPowerChange notification is sent when the status of a port power changes.""",
        }, # notification
        "tpPoePortPowerOverLoading" : {
            "nodetype" : "notification",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.2.2",
            "status" : "current",
            "objects" : {
                "tpPoePortIndex" : {
                    "nodetype" : "object",
                    "module" : "TPLINK-POWER-OVER-ETHERNET-MIB"
                },
            },
            "description" :
                """A poePortPowerOverLoading notification is sent when a port is over loading.""",
        }, # notification
        "tpPoePortShortCircuit" : {
            "nodetype" : "notification",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.2.3",
            "status" : "current",
            "objects" : {
                "tpPoePortIndex" : {
                    "nodetype" : "object",
                    "module" : "TPLINK-POWER-OVER-ETHERNET-MIB"
                },
            },
            "description" :
                """A poePortShortCircuit notification is sent when short circuit occurs on a port.""",
        }, # notification
        "tpPoePortPowerOver30Watts" : {
            "nodetype" : "notification",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.2.4",
            "status" : "current",
            "objects" : {
                "tpPoePortIndex" : {
                    "nodetype" : "object",
                    "module" : "TPLINK-POWER-OVER-ETHERNET-MIB"
                },
            },
            "description" :
                """A poePortPowerOver30Watts notification is sent when a port's consumption is over 30W.""",
        }, # notification
        "tpPoePortPowerDeny" : {
            "nodetype" : "notification",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.2.5",
            "status" : "current",
            "objects" : {
                "tpPoePortIndex" : {
                    "nodetype" : "object",
                    "module" : "TPLINK-POWER-OVER-ETHERNET-MIB"
                },
            },
            "description" :
                """A poePowerDeny notification is sent when a port's power supply is denied.""",
        }, # notification
        "tpPoeThermalShutdown" : {
            "nodetype" : "notification",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.2.6",
            "status" : "current",
            "objects" : {
                "tpPoePortIndex" : {
                    "nodetype" : "object",
                    "module" : "TPLINK-POWER-OVER-ETHERNET-MIB"
                },
            },
            "description" :
                """A poeThermalShutdown notification is sent when the power supply shutdown occurs because temperature is too high.""",
        }, # notification
        "tpPoeOverMaxPowerBudget" : {
            "nodetype" : "notification",
            "moduleName" : "TPLINK-POWER-OVER-ETHERNET-MIB",
            "oid" : "1.3.6.1.4.1.11863.6.56.2.7",
            "status" : "current",
            "objects" : {
                "tpSystemPowerLimit" : {
                    "nodetype" : "object",
                    "module" : "TPLINK-POWER-OVER-ETHERNET-MIB"
                },
            },
            "description" :
                """A poeOverMaxPowerBudget notification is sent when the total power is over the budget.""",
        }, # notification
    }, # notifications

}
