from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

original_text='मख्खन लाल'

print(transliterate(original_text, sanscript.DEVANAGARI ,sanscript.KOLKATA))

#print(transliterate(original_text, sanscript.TELUGU ,sanscript.KOLKATA))
