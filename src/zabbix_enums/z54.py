from .common.audit_log import AuditLogAction
from .common.dashboard import *
from .common.event import *
from .common.host import *
from .common.host_group import *
from .common.host_interface import *
from .common.item_preprocessing import PreprocessingErrorHandler
from .common.item import *
from .common.problem import *
from .common.snmp import *
from .common.trigger import *
from .common.user_group import *


DashboardStartSlideshow = NoYes


class ItemType(IntEnum):
    ZABBIX_AGENT = 0
    ZABBIX_TRAPPER = 2
    SIMPLE_CHECK = 3
    ZABBIX_INTERNAL = 5
    ZABBIX_AGENT_ACTIVE = 7
    WEB_ITEM = 9
    EXTERNAL_CHECK = 10
    DATABASE_MONITOR = 11
    IPMI_AGENT = 12
    SSH_AGENT = 13
    TELNET_AGENT = 14
    CALCULATED = 15
    JMX_AGENT = 16
    SNMP_TRAP = 17
    DEPENDENT_ITEM = 18
    HTTP_AGENT = 19
    SNMP_AGENT = 20
    SCRIPT = 21


class MacroType(IntEnum):
    TEXT = 0
    SECRET = 1
    VAULT = 2


class AuditLogResourceType(IntEnum):
    USER = 0
    CONFIGURATION_OF_ZABBIX = 2
    MEDIA_TYPE = 3
    HOST = 4
    ACTION = 5
    GRAPH = 6
    GRAPH_ELEMENT = 7
    USER_GROUP = 11
    TRIGGER = 13
    HOST_GROUP = 14
    ITEM = 15
    IMAGE = 16
    VALUE_MAP = 17
    SERVICE = 18
    MAP = 19
    WEB_SCENARIO = 22
    DISCOVERY_RULE = 23
    SCRIPT = 25
    PROXY = 26
    MAINTENANCE = 27
    REGULAR_EXPRESSION = 28
    MACRO = 29
    TEMPLATE = 30
    TRIGGER_PROTOTYPE = 31
    ICON_MAPPING = 32
    DASHBOARD = 33
    EVENT_CORRELATION = 34
    GRAPH_PROTOTYPE = 35
    ITEM_PROTOTYPE = 36
    HOST_PROTOTYPE = 37
    AUTOREGISTRATION = 38
    MODULE = 39
    SETTINGS = 40
    HOUSEKEEPING = 41
    AUTHENTICATION = 42
    DASHBOARD_TEMPLATE = 43
    USER_ROLE = 44
    AUTH_TOKEN = 45
    SCHEDULED_REPORT = 46


class DashboardWidgetType(str, Enum):
    ACTION_LOG = "actionlog"
    CLOCK = "clock"
    DATA_OVERVIEW = "dataover"
    DISCOVERY_STATUS = "discovery"
    FAVORITE_GRAPHS = "favgraphs"
    FAVORITE_MAPS = "favmaps"
    GRAPH_CLASSIC = "graph"
    GRAPH_PROTOTYPE = "graphprototype"
    HOST_AVAILABILITY = "hostavail"
    MAP = "map"
    MAP_NAVIGATION_TREE = "navtree"
    PLAIN_TEXT = "plaintext"
    PROBLEM_HOSTS = "problemhosts"
    PROBLEMS = "problems"
    PROBLEMS_BY_SEVERITY = "problemsbysv"
    GRAPH = "svggraph"
    SYSTEM_INFORMATION = "systeminfo"
    TRIGGER_OVERVIEW = "trigover"
    URL = "url"
    WEB_MONITORING = "web"


class ItemPreprocessingType(IntEnum):
    CUSTOM_MULTIPLIER = 1
    RIGHT_TRIM = 2
    LEFT_TRIM = 3
    TRIM = 4
    REGULAR_EXPRESSION = 5
    BOOLEAN_TO_DECIMAL = 6
    OCTAL_TO_DECIMAL = 7
    HEXADECIMAL_TO_DECIMAL = 8
    SIMPLE_CHANGE = 9
    CHANGE_PER_SECOND = 10
    XML_XPATH = 11
    JSONPATH = 12
    IN_RANGE = 13
    MATCHES_REGULAR_EXPRESSION = 14
    DOES_NOT_MATCH_REGULAR_EXPRESSION = 15
    CHECK_FOR_ERROR_IN_JSON = 16
    CHECK_FOR_ERROR_IN_XML = 17
    CHECK_FOR_ERROR_USING_REGULAR_EXPRESSION = 18
    DISCARD_UNCHANGED = 19
    DISCARD_UNCHANGED_WITH_HEARTBEAT = 20
    JAVASCRIPT = 21
    PROMETHEUS_PATTERN = 22
    PROMETHEUS_TO_JSON = 23
    CSV_TO_JSON = 24
    REPLACE = 25
    CHECK_UNSUPPORTED = 26
    XML_TO_JSON = 27
