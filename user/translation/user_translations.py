from modeltranslation.translator import TranslationOptions, register
from user.models import User


class UserTranslationOptions(TranslationOptions):
    fields = ("name",)
