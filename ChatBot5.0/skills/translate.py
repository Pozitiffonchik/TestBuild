from translate import Translator

def handle(query):
    words = query.split()
    target_language = words[2]
    text_to_translate = ' '.join(words[3:])
    
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text_to_translate)
    return translation
