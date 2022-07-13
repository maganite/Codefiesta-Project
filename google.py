# from google.transliteration import transliterate_text
# result = transliterate_text('Hello comrade!', lang_code='ru')
# print(result)

from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

# original_text='चलो चलते हैं'

# print(transliterate(original_text, sanscript.DEVANAGARI, sanscript.ITRANS))


data = 'வணக்கம்'

print(transliterate(data, sanscript.TAMIL, sanscript.HK))
