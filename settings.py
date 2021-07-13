from os import environ

SESSION_CONFIGS = [
dict(
         name='Graal',
         app_sequence=['graal'],
         num_demo_participants=1,
     ),
dict(
         name='Urn',
         app_sequence=['ellsberg'],
         num_demo_participants=1,
     ),
dict(
         name='Radio',
         app_sequence=['fields_custom_display'],
         num_demo_participants=1,
     ),
dict(
         name='bubble',
         app_sequence=['bubble'],
         num_demo_participants=1,
     ),

     dict(
         name='dictator',
         app_sequence=['dictator'],
         num_demo_participants=4,
     ),
dict(
         name='TrustGame',
         app_sequence=['my_trust'],
         num_demo_participants=2,
     ),

dict(
         name='Survey',
         app_sequence=['my_simple_survey'],
         num_demo_participants=3,
     ),
dict(
         name='Public_Goods',
         app_sequence=['my_public_goods'],
         num_demo_participants=3,
     ),
dict(
         name='Dictatorship',
         app_sequence=['dictatorship'],
         num_demo_participants=2,
     ),

dict(
         name='Live_pages_basic',
         app_sequence=['live_pages_basic'],
         num_demo_participants=2,
     ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4244626231335'
