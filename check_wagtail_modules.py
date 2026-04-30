import importlib

for mod in ['wagtail.contrib.modeladmin', 'wagtail.admin', 'wagtail.contrib.settings']:
    try:
        importlib.import_module(mod)
        print(f'{mod}: OK')
    except Exception as e:
        print(f'{mod}: {type(e).__name__}: {e}')
