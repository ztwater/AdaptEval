import importlib

TWO_FACTOR_BACKENDS = (
    'id.backends.AllowToBeDisabled', # Disable this to enforce Two Factor Authentication
    'id.backends.TOTPBackend',
    'id.backends.HOTPBackend',
    #'id.backends.YubikeyBackend',
    #'id.backends.OneTimePadBackend',
    #'id.backends.EmailBackend',
)

backends = [getattr(importlib.import_module(mod), cls) for (mod, cls) in (backend.rsplit(".", 1) for backend in TWO_FACTOR_BACKENDS)]
