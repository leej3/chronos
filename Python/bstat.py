#!/usr/bin/env python
import sys
import serial
import time
from pymodbus.exceptions import ModbusException
from pymodbus.client.sync import ModbusSerialClient

method = "rtu"
baudrate = 9600
parity = "E"
port = "/dev/ttyUSB0"
timeout = 0.3

# Connecting to boiler via modbus protocol
def get_boiler_stats():
    boiler_stats = {"system_supply_temp": 0,
                    "outlet_temp": 0,
                    "inlet_temp": 0,
                    "flue_temp": 0,
                    "cascade_current_power": 0,
                    "lead_firing_rate": 0}
    try:
        modbus_client = ModbusSerialClient(method=method,
                                           baudrate=baudrate,
                                           parity=parity,
                                           port=port,
                                           timeout=timeout)
        modbus_client.connect()
    except (ModbusException, OSError) as e:
        return boiler_stats

    c_to_f = lambda t: round(((9.0/5.0)*t + 32.0), 1)
    for i in range(3):
        try:
            # Read one register from 40006 address to get System Supply Temperature
            # Memory map for the boiler is here on page 8:
            # http://www.lochinvar.com/_linefiles/SYNC-MODB%20REV%20H.pdf
            hregs = modbus_client.read_holding_registers(6, count=1, unit=1)
            # Read 9 registers from 30003 address
            iregs = modbus_client.read_input_registers(3, count=9, unit=1)
            boiler_stats = {"system_supply_temp": c_to_f(hregs.getRegister(0)/10.0),
                            "outlet_temp": c_to_f(iregs.getRegister(5)/10.0),
                            "inlet_temp": c_to_f(iregs.getRegister(6)/10.0),
                            "flue_temp": c_to_f(iregs.getRegister(7)/10.0),
                            "cascade_current_power": float(iregs.getRegister(3)),
                            "lead_firing_rate": float(iregs.getRegister(8))}
        except (OSError, serial.SerialException, ModbusException, AttributeError, IndexError) as e:
            time.sleep(0.7)
        else:
            break
    modbus_client.close()  
    return boiler_stats

if __name__ == '__main__':
    print(";".join([str(v) for v in get_boiler_stats().values()]))