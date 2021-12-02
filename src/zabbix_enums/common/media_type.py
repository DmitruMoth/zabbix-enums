from . import _NoYes, _EntityStatus, _ObjectSource, _ZabbixEnum


MediaTypeSMTPSVerifyHost = _NoYes
MediaTypeSMTPSVerifyPeer = _NoYes
MediaTypeStatus = _EntityStatus
MediaTypeProcessTags = _NoYes
MediaTypeShowEventMenu = _NoYes
MediaTypeEventSource = _ObjectSource


class MediaType(_ZabbixEnum):
    EMAIL = 0
    SCRIPT = 1
    SMS = 2
    WEBHOOK = 4


class MediaTypeSMTPSecurity(_ZabbixEnum):
    NONE = 0
    STARTTLS = 1
    SSL_TLS = 2


class MediaTypeSMTPAuthentication(_ZabbixEnum):
    NONE = 0
    PASSWORD = 1


class MediaTypeContentType(_ZabbixEnum):
    PLAIN_TEXT = 0
    HTML = 1


class MediaTypeRecovery(_ZabbixEnum):
    OPERATIONS = 0
    RECOVERY = 1
    RECOVERY_OPERATIONS = 1
    UPDATE = 2
    UPDATE_OPERATIONS = 2
