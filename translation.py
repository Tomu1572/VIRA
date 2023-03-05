from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('translate_text.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        # Put the encoding parameter to save in a text file
        with open('text-ja.txt', mode='w', encoding="utf-8") as my_file2:
        	my_file2.write(translation)
except FileNotFoundError as err:
    print('file does not exist')