#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Currency',
    'name_de_DE': 'Währung',
    'name_es_CO': 'Moneda',
    'name_es_ES': 'Divisa',
    'name_fr_FR': 'Devise',
    'version': '1.6.0',
    'author': 'B2CK',
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    'description': '''Define currencies and exchange rate.
Allow to customize the formatting of the currency amount.
''',
    'description_de_DE': ''' - Ermöglicht die Eingabe von Währungen und Wechselkursen.
 - Erlaubt die beliebige Formatierung von Währungsbeträgen.
''',
    'description_es_CO': '''Define las monedas y la tasa de cambio.
Permite personalizar el formato de visualización de la moneda.
''',
    'description_es_ES': '''Define las divisas y la tasa de cambio.
 - Permite personalizar el formato de visualización de la divisa.
''',
    'description_fr_FR': '''Défini les devises et leurs taux de change.
Permet de formater les montants en fonction de la devise.
''',
    'depends': [
        'ir',
        'res',
    ],
    'xml': [
        'currency.xml',
    ],
    'translation': [
        'de_DE.csv',
        'es_CO.csv',
        'es_ES.csv',
        'fr_FR.csv',
    ]
}
