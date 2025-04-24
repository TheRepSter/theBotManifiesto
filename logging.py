import logging

class LoggingMixin:
    logging_prefix = None
    logging_suffix = None

    @property
    def logger(self):
        prefix = self._resolve_logging_prefix()
        suffix = self.logging_suffix or self.__class__.__name__
        return logging.getLogger(f"{prefix}.{suffix}")

    def _resolve_logging_prefix(self):
        for cls in self.__class__.__mro__:
            if 'logging_prefix' in cls.__dict__ and cls.logging_prefix:
                return cls.logging_prefix
        return self.__class__.__module__
