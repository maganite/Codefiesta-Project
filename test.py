from googletrans import Translator

abc = Translator()

out=abc.translate('hello', dest='ja')
print(out)
