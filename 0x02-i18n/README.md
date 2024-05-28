0x02. i18n

Learning:

how to parametrize Flask templates to display different languages
how to infer the correct locale based on URL parameters,
user settings or request headers
how to localize timestamps

├── app.py # Main Flask application
├── babel.cfg # Babel configuration file
├── requirements.txt # Python dependencies
├── templates/
│ └── 5-index.html # HTML template with i18n support
└── translations/
├── en/
│ └── LC-MESSAGES/
│ ├── messages.po # English translation file
│ └── messages.mo # Compiled English translation file
└── fr/
└── LC-MESSAGES/
├── messages.po # French translation file
└── messages.mo # Compiled French translation file
