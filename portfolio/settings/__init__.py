import os

"""Select the active settings module for the portfolio project.

By default, this loads the development settings. Set DJANGO_ENV=prod or
DJANGO_ENV=production to load production settings instead.
"""

ENVIRONMENT = os.environ.get("DJANGO_ENV", "dev").strip().lower()

if ENVIRONMENT in {"prod", "production"}:
    from .prod import *
else:
    from .dev import *
