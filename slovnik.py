from translate import Translator

vyber = input('pro preklad do nemciny zadejte 1 pro preklad do anglictiny zadejte 2: ')

if vyber == ('1'): 
    word = input('zadejte slovo pro preklad: ')
    translator = Translator(from_lang='ENG', to_lang='DE')
    translation = translator.translate(word)

    print(translation)

elif vyber == ('2'):
    word = input('zadejte slovo pro preklad: ')
    translator = Translator(from_lang='DE', to_lang='ENG')
    translation = translator.translate(word)

    print(translation)

else:
    print('jeste neumim ')