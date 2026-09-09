# /home/kamusc/myproject/myproject/__init__.py
import django.db.backends.mysql.base

# Store the original class initialization method
original_init = django.db.backends.mysql.base.DatabaseWrapper.__init__

def patched_init(self, *args, **kwargs):
    original_init(self, *args, **kwargs)
    # Force override the internal CPython database engine version tuple
    self.get_database_version = lambda: (8, 4, 0)

# Overwrite the standard initialization routine with our patch
django.db.backends.mysql.base.DatabaseWrapper.__init__ = patched_init
