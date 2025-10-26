"""Exceptions for async-sunspec-client."""


class SunSpecClientError(Exception):
    """Base exception for SunSpec client."""


class SunSpecConnectionError(SunSpecClientError):
    """Connection error."""


class SunSpecDiscoveryError(SunSpecClientError):
    """Model discovery error."""


class SunSpecModelError(SunSpecClientError):
    """Model loading/parsing error."""


class SunSpecParseError(SunSpecClientError):
    """Data parsing error."""
