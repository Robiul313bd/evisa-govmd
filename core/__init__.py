from django.template.context import BaseContext


def _patched_basecontext_copy(self):
    """Fix Django BaseContext copy on environments with broken template context support."""
    duplicate = object.__new__(type(self))
    duplicate.__dict__.update(self.__dict__)
    duplicate.dicts = self.dicts[:]
    return duplicate


BaseContext.__copy__ = _patched_basecontext_copy
