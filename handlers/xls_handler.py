from aiogram import Bot
from openpyxl.styles import NamedStyle, Font, PatternFill, Side, Border

from handlers.base_handler import BaseProjectHandler


class XlsHandlers(BaseProjectHandler):

    def __init__(self, bot: Bot) -> None:
        super().__init__(bot)

    __side_border = Side(style="double", color="00333333")
    __horizontal_left = "left"
    __vertical_center = "vcenter"

    async def _get_header_format(self, workbook):
        header_format = workbook.add_format()
        header_format.set_bold()
        header_format.set_font_color("00003300")
        header_format.set_font_size(14)
        header_format.set_bg_color("FFFF99")
        header_format.set_border()
        return header_format

    async def _get_cell_format(self, workbook):
        cell_format = workbook.add_format()
        cell_format.set_align(self.__horizontal_left)
        cell_format.set_valign(self.__vertical_center)
        cell_format.set_text_wrap()
        cell_format.set_border()
        return cell_format

    @staticmethod
    def __get_header_style():
        header_style = NamedStyle(name="header_style")
        header_style.font = Font(b=True, size=14, color="00003300")
        header_style.fill = PatternFill("solid", fgColor="FFFF99")
        side = Side(style="medium", color="00000080")
        header_style.border = Border(bottom=side)
        return header_style
