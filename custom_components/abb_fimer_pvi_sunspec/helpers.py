"""Helper functions for ABB FIMER PVI SunSpec."""

import logging


def log_debug(logger: logging.Logger, context: str, message: str, **kwargs) -> None:
    """Log debug message with context."""
    extra = " ".join(f"{k}={v}" for k, v in kwargs.items())
    logger.debug("%s: %s %s", context, message, extra)


def log_info(logger: logging.Logger, context: str, message: str, **kwargs) -> None:
    """Log info message with context."""
    extra = " ".join(f"{k}={v}" for k, v in kwargs.items())
    logger.info("%s: %s %s", context, message, extra)


def log_warning(logger: logging.Logger, context: str, message: str, **kwargs) -> None:
    """Log warning message with context."""
    extra = " ".join(f"{k}={v}" for k, v in kwargs.items())
    logger.warning("%s: %s %s", context, message, extra)


def log_error(logger: logging.Logger, context: str, message: str, **kwargs) -> None:
    """Log error message with context."""
    extra = " ".join(f"{k}={v}" for k, v in kwargs.items())
    logger.error("%s: %s %s", context, message, extra)
