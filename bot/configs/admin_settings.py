from bot.configs.base_language import Language
from bot.configs.eng import English
from bot.configs.ru import Russian
from bot.configs.ukr import Ukrainian

language: Language
languages = {"ru", "ukr", "en"}
language_set = {Ukrainian(), Russian(), English()}
