import busio
import board
import time


##
## INSIDE D:LIB
##

class RYLR896:
    __debug = None

    def __init__(self, tx=None, rx=None, timeout=.5, debug=False, name=None):
        if name is None:
            self.name = self.__class__.__name__
        else:
            self.name = name
        self.__debug = debug
        assert rx is not None and tx is not None
        self.timeout = timeout
        self.set_device_timeout()
        self.uart = busio.UART(rx=rx, tx=tx, baudrate=115200, receiver_buffer_size=2048, timeout=0.1)
        if self.test_device():
            self.factory_reset()
            print("{} is factory reset and ready to use".format(self.name))
            self.address = 0
            self.band = 915000000
            self.cpin = "No Password!"
            self.rf_power = 15
            self.mode = 0
            self.network_id = 0
            self.spread_factor = 12
            self.bandwidth = 7
            self.coding_rate = 1
            self.programmed_preamble = 4
        else:
            print("Failed to establish communication with {}".format(self.name))

    def set_device_timeout(self, timeout_to_use: float = .5):
        self.timeout = timeout_to_use

    def cmd(self, lora_cmd):
        self.uart.reset_input_buffer()
        self.uart.write(bytes(lora_cmd, "utf-8"))
        self.uart.write(b"\x0d\x0a")
        start = time.time()
        while True:
            now = time.time()
            data = self.uart.read()
            if data is not None:
                break
            if now - start > self.timeout:
                break
        try:
            data = data.decode().replace("\r\n", "")
            return data
        except Exception as e:

            print("{} had a failure".format(self.name))
            print(e)
            return None

    def read_from_device(self):
        data = None
        while True:
            data = self.uart.read()
            if data is not None:
                break
        try:
            data = data.decode().replace("\r\n", "")
            return data
        except:
            return data

    def set_address(self, address_to_use: int) -> bool:
        """
        Set the address of the device
        :param (int) address_to_use: 0-65535
        :return: True on success, False on failure
        """
        if address_to_use < 0:
            raise "{} -- Address not allowed".format(self.name)
        if address_to_use > 65535:
            raise "{} ++ Address not allowed".format(self.name)
        response = False
        cmd_to_use = "AT+ADDRESS={}".format(address_to_use)
        if self.__debug:
            print("{} set_address sending: {}".format(self.name, cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("{} set_address reply: {}".format(self.name, reply))
        if reply == "+OK":
            response = True
            self.address = address_to_use

        return response

    def get_address(self) -> int:
        """
        gets address of device.
        :return: int of address
        """

        response = -1
        cmd_to_use = "AT+ADDRESS?"
        if self.__debug:
            print("get_address sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("get_address reply: {}".format(reply))
        if reply.startswith("+ADDRESS="):
            addr = reply[len('+ADDRESS='):]
            response = int(addr)
            self.address = response
        return response

    def test_device(self):
        cmd_to_use = "AT"
        if self.__debug:
            print("test_device sending {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("test_device reply: {}".format(reply))
        if reply == "+OK":
            return True
        else:
            return False

    def set_band(self, band_to_use: int) -> bool:
        if band_to_use < 862000000:
            raise "Band not allowed"
        if band_to_use > 1020000000:
            raise "Band not allowed"
        cmd_to_use = "AT+BAND={}".format(band_to_use)
        if self.__debug:
            print("set_band sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("set_band reply: {}".format(reply))
        response = False
        if reply == "+OK":
            response = True
            self.band = band_to_use
        return response

    def get_band(self) -> int:
        response = -1
        cmd_to_use = "AT+BAND?"
        if self.__debug:
            print("get_band sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("get_band reply: {}".format(reply))
        if reply.startswith("+BAND="):
            band = reply[len('+BAND='):]
            response = int(band)
            self.band = response
        return response

    def set_cpin(self, cpin_to_use: str) -> bool:
        try:
            val = int(cpin_to_use, 16)
        except:
            raise "cpin is not hex string"
        if len(cpin_to_use) > 32:
            raise "cpin is too long"

        cmd_to_use = "AT+CPIN={}".format(cpin_to_use)
        if self.__debug:
            print("set_cpin sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("set_cpin reply: {}".format(reply))
        response = False
        if reply == "+OK":
            response = True
            self.cpin = cpin_to_use
        return response

    def get_cpin(self) -> str:
        response = -1
        cmd_to_use = "AT+CPIN?"
        if self.__debug:
            print("get_cpin sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("get_cpin reply: {}".format(reply))
        if reply.startswith("+CPIN="):
            band = reply[len('+CPIN='):]
            response = band
            self.cpin = response
        return response

    def set_rf_power_out(self, rf_power_to_use: int) -> bool:
        if rf_power_to_use < 0:
            raise "rf power not allowed"
        if rf_power_to_use > 15:
            raise "rf power not allowed"
        cmd_to_use = "AT+CRFOP={}".format(rf_power_to_use)
        if self.__debug:
            print("set_rf_power_out sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("set_rf_power_out reply: {}".format(reply))
        response = False
        if reply == "+OK":
            response = True
            self.rf_power = rf_power_to_use
        return response

    def get_rf_power_out(self) -> int:
        response = -1
        cmd_to_use = "AT+CRFOP?"
        if self.__debug:
            print("get_rf_power_out sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("get_rf_power_out reply: {}".format(reply))
        if reply.startswith("+CRFOP="):
            band = reply[len('+CRFOP='):]
            response = int(band)
            self.rf_power = response
        return response

    def factory_reset(self):
        cmd_to_use = "AT+FACTORY"
        if self.__debug:
            print("factory_reset sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("factory_reset reply: {}".format(reply))
        response = False
        if reply == "+FACTORY":
            response = True
        return response

    def sw_reset(self):
        cmd_to_use = "AT+RESET"
        if self.__debug:
            print("sw_reset sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("sw_reset reply: {}".format(reply))
        response = False
        if reply == b"+RESETx\00+READY":
            response = True
            return response
        return response

    def set_mode(self, mode_to_use: int) -> bool:
        if mode_to_use != 0 and mode_to_use != 1:
            raise "Mode is incorrect"
        cmd_to_use = "AT+MODE={}".format(mode_to_use)
        if self.__debug:
            print("set_mode sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("set_mode reply: {}".format(reply))
        response = False
        if reply == "+OK":
            response = True
            self.mode = mode_to_use
        return response

    def set_network_id(self, network_id_to_use: int) -> bool:
        if 0 <= network_id_to_use <= 16:
            pass
        else:
            raise "Bad network id. Must be 0-16"

        cmd_to_use = "AT+NETWORKID={}".format(network_id_to_use)
        if self.__debug:
            print("set_network_id sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("set_network_id reply: {}".format(reply))
        response = False
        if reply == "+OK":
            response = True
            self.network_id = network_id_to_use
        return response

    def get_network_id(self):
        response = -1
        cmd_to_use = "AT+NETWORKID?"
        if self.__debug:
            print("get_network_id sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("get_network_id reply: {}".format(reply))
        if reply.startswith("+NETWORKID="):
            netid = reply[len('+NETWORKID='):]
            response = int(netid)
            self.network_id = response
        return response

    def set_rf_parameters(self, sf_to_use: int, bw_to_use: int, cr_to_use: int, pp_to_use: int) -> bool:
        if 7 <= sf_to_use <= 12:
            pass
        else:
            raise "Bad spreadfactor. Must be 7-12"
        if 2 <= bw_to_use <= 9:
            pass
        else:
            raise "Bad bandwidth. Must be 0-9"
        if 1 <= cr_to_use <= 4:
            pass
        else:
            raise "Bad coding rate. Must be 1-4"
        if 4 <= pp_to_use <= 7:
            pass
        else:
            raise "Bad programmed preamble. Must be 4-7"
        cmd_to_use = "AT+PARAMETER={},{},{},{}".format(sf_to_use, bw_to_use, cr_to_use, pp_to_use)
        if self.__debug:
            print("set_rf_parameters sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("set_rf_parameters reply: {}".format(reply))
        response = False
        if reply == "+OK":
            response = True
            self.spread_factor = sf_to_use
            self.bandwidth = bw_to_use
            self.coding_rate = cr_to_use
            self.programmed_preamble = pp_to_use
        return response

    def get_rf_parameters(self):
        cmd_to_use = "AT+PARAMETER?"
        if self.__debug:
            print("get_rf_parameters sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("get_rf_parameters reply: {}".format(reply))
        if reply.startswith("+PARAMETER="):
            params = reply[len('+PARAMETER='):]
            sf, bw, cr, pp = params.split(',')
            self.spread_factor = sf
            self.bandwidth = bw
            self.coding_rate = cr
            self.programmed_preamble = pp
            return sf, bw, cr, pp
        else:
            return None

    def send(self, data: str = None, address: int = 0) -> bool:
        if 0 <= address <= 65535:
            pass
        else:
            raise "{} Bad address".format(self.name)
        if data is None:
            raise "{} Bad data, cannot be none".format(self.name)
        try:
            bytes(data, "utf-8")
        except:
            raise "{} Bad data".format(self.name)
        cmd_to_use = "AT+SEND={},{},{}".format(address, len(data), data)
        if self.__debug:
            print("{} send sending: {}".format(self.name, cmd_to_use))
        self.uart.reset_input_buffer()
        self.uart.write(bytes(cmd_to_use, "utf-8"))
        self.uart.write(b"\x0d\x0a")
        time.sleep(self.timeout)
        data = None
        start = time.time()
        while True:
            now = time.time()
            data = self.uart.read()
            if data is not None:
                break
            if now - start > 3:
                if self.__debug:
                    print("{} send reply timing out".format(self.name))
                break
        reply = data
        if self.__debug:
            print("{} send reply: {}".format(self.name, reply))

    def get_last_sent(self):
        cmd_to_use = "AT+SEND?"
        if self.__debug:
            print("get_last_sent sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("get_last_sent reply: {}".format(reply))
        if reply.startswith("+SEND="):
            params = reply[len('+SEND='):]
            addr, length, data = params.split(',')
            return addr, length, data
        else:
            return None

    def get_firmware_version(self):
        cmd_to_use = "AT+VER?"
        if self.__debug:
            print("get_firmware_version sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("get_firmware_version reply: {}".format(reply))
        if reply.startswith("+VER="):
            response = reply[len('+VER='):]
            return response
        else:
            return None

    def get_UID(self):
        cmd_to_use = "AT+UID?"
        if self.__debug:
            print("get_UID sending: {}".format(cmd_to_use))
        reply = self.cmd(cmd_to_use)
        if self.__debug:
            print("get_UID reply: {}".format(reply))
        if reply.startswith("+UID="):
            response = reply[len('+UID='):]
            return response
        else:
            return None
