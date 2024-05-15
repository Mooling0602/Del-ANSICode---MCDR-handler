import parse
from strip_ansi import strip_ansi
from mcdreforged.handler.impl.bukkit_handler import BukkitHandler

class LeavesHandler(BukkitHandler):
    def get_name(self) -> str:
        return 'leaves_handler'

    def pre_parse_server_stdout(self, text: str) -> str:
        rtext = strip_ansi(text)
        return rtext
