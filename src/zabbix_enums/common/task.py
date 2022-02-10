from zabbix_enums.common import _ZabbixEnum


class TaskType(_ZabbixEnum):
    DIAGNOSTIC = 1
    CHECK_NOW = 6

class TaskStatus(_ZabbixEnum):
    NEW = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    EXPIRED = 4

class TaskStatisticResult(_ZabbixEnum):
    ERROR = -1
    CREATED = 0
