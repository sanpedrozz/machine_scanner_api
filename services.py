# services.py

import serial.tools.list_ports
from typing import List, Union

from models import PortDescription
from utils import show_message
from logger import logger


class ComPortService:
    def __init__(self):
        self.virtual_com_ports_list = self._get_virtual_com_ports_list()
        self.api_com_port = self._select_com_port(0)
        self.machine_com_port = self._select_com_port(1)
        logger.info(f"Найденные порты. Для станка: {self.machine_com_port}. Для API: {self.api_com_port}")
        show_message(
            api_com_port=self.api_com_port,
            machine_com_port=self.machine_com_port
        )

    def send_to_com_port(self, message: Union[int, str]) -> bool:
        try:
            with serial.Serial(port=self.api_com_port, baudrate=9600, timeout=1) as port:
                if isinstance(message, int):
                    message = str(message)
                message += '\r\n'
                port.write(message.encode())
                logger.info(f"{message.encode()} отправлено в {self.api_com_port}")
            return True
        except serial.SerialException as e:
            logger.error(f"Ошибка при отправке в {self.api_com_port}: {e}")
            return False

    def _select_com_port(self, index: int, port_description: PortDescription = PortDescription()) -> Union[str, None]:
        ports = self._get_virtual_com_ports_list(port_description)
        if len(ports) > index:
            return ports[index]
        logger.error(f"Такого порта с index = {index} не существует. Найденные COM порты {ports}")
        return None

    @staticmethod
    def _get_virtual_com_ports_list(port_description: PortDescription = PortDescription()) -> List[str]:
        return [port.name for port in serial.tools.list_ports.comports() if
                port_description.description in port.description]


