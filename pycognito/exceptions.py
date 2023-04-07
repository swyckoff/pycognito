class WarrantException(Exception):
    """Base class for all pyCognito exceptions"""


class ForceChangePasswordException(WarrantException):
    """Raised when the user is forced to change their password"""


class TokenVerificationException(WarrantException):
    """Raised when token verification fails."""


class ChallengeException(WarrantException):
    """Raised when a challenge token is encountered ."""

    def __init__(self, message, tokens, *args, **kwargs):
        super().__init__(message, tokens, *args, **kwargs)
        self.message = message
        self._tokens = tokens

    def get_challenge_tokens(self):
        return self._tokens


class NewPasswordChallengeException(ChallengeException):
    ...


class MFAChallengeException(ChallengeException):
    """Raised when MFA is required."""
    ...


class SoftwareTokenMFAChallengeException(MFAChallengeException):
    """Raised when Software Token MFA is required."""


class SMSMFAChallengeException(MFAChallengeException):
    """Raised when SMS MFA is required."""
