from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

class TransliterateLanguage:
    def __init__(self, lanuage, original_text):
        self.language=lanuage
        self.languageSet = {
            "Hindi": sanscript.DEVANAGARI,
            "Gujarati": sanscript.GUJARATI,
            "Kannada": sanscript.KANNADA,
            "Bengali": sanscript.BENGALI,
            #"Gurmukhi": sanscript.GURMUKHI,
            "malayalam": sanscript.MALAYALAM,
            "oriya": sanscript.ORIYA,
            "tamil": sanscript.TAMIL,
            "telugu": sanscript.TELUGU,
        }
        self.original_text=original_text
    
    def convertTo(self):
        return transliterate(self.original_text, self.languageSet[self.language] ,sanscript.ITRANS) 