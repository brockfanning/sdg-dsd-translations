import sdmx
import yaml
import os
from sdg.translations import TranslationInputSdmx

translation_input = TranslationInputSdmx(source='dsd.xml')
translation_input.execute()
translations = translation_input.get_translations()
for language in translations:
    for concept in translations[language]:
        filename = os.path.join('translations', language, concept) + '.yml'
        with open(filename, 'w', encoding='utf-8') as stream:
            yaml.dump(translations[language][concept], stream, allow_unicode=True, width=1000)
