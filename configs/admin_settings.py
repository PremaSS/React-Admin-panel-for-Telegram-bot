from configs.base_language import Language
from configs.eng import English
from configs.ru import Russian
from configs.ukr import Ukrainian

language: Language
languages = {"ru", "ukr", "en"}
language_set = {Ukrainian(), Russian(), English()}
