# -*- coding: utf-8 -*-

import six

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

base_path = '/app/routers'


DefinitionsSchemaactivity = {'required': ['url', 'title', 'abstract', 'watch', 'regislation'], 'properties': {'url': {'type': 'string'}, 'title': {'type': 'string'}, 'abstract': {'type': 'string'}, 'watch': {'type': 'integer'}, 'regislation': {'type': 'integer'}}}
DefinitionsSchemeactivities = {'type': 'array', 'items': {'required': ['url', 'title', 'abstract', 'watch', 'regislation'], 'properties': {'url': {'type': 'string'}, 'title': {'type': 'string'}, 'abstract': {'type': 'string'}, 'watch': {'type': 'integer'}, 'regislation': {'type': 'integer'}}}}

validators = {
    ('user', 'POST'): {'args': {'required': ['username', 'password'], 'properties': {'username': {'description': '用户名', 'type': 'string'}, 'password': {'description': '密码', 'type': 'string'}}}},
    ('user', 'PUT'): {'args': {'required': ['username', 'password'], 'properties': {'username': {'description': '用户名', 'type': 'string'}, 'password': {'description': '密码', 'type': 'string'}}}},
    ('user_info', 'PUT'): {'args': {'required': ['phone', 'email', 'name', 'realName', 'gender', 'bornDate', 'detailLocation', 'marriage', 'friend', 'hometown', 'schoolLevel', 'company', 'livingPlace', 'job', 'housingCondition', 'enconomyCondition'], 'properties': {'phone': {'description': '电话', 'type': 'string'}, 'email': {'description': '邮箱', 'type': 'string'}, 'name': {'description': '昵称', 'type': 'string'}, 'realName': {'description': '真实姓名', 'type': 'string'}, 'gender': {'description': '性别', 'type': 'string'}, 'bornDate': {'description': '出生日期', 'type': 'Date'}, 'detailLocation': {'description': '具体地点', 'type': 'string'}, 'marriage': {'description': '婚姻情况', 'type': 'string'}, 'friend': {'description': '交友要求', 'type': 'string'}, 'hometown': {'description': '家乡', 'type': 'string'}, 'schoolLevel': {'description': '学历', 'type': 'string'}, 'company': {'description': '公司名称', 'type': 'string'}, 'livingPlace': {'description': '居住地点', 'type': 'string'}, 'job': {'description': '工作', 'type': 'string'}, 'housingCondition': {'description': '住房情况', 'type': 'string'}, 'enconomyCondition': {'description': '经济情况', 'type': 'string'}}}},
    ('user_info', 'GET'): {'args': {'required': ['uID'], 'properties': {'uID': {'description': '用户编号', 'type': 'string'}}}},
    ('user_info_uID', 'POST'): {'args': {'required': ['result'], 'properties': {'result': {'description': '审核结果', 'type': 'string'}}}},
    ('activity', 'PUT'): {'args': {'required': ['activityName', 'location', 'registerBeginTime', 'registerEndTime', 'selectBeginTime', 'selectEndTime', 'chargeRule', 'boyBeginAge', 'girlBeginAge', 'increment', 'wechat', 'realName'], 'properties': {'activityName': {'description': '活动名称', 'type': 'string'}, 'location': {'description': '活动地点', 'type': 'string'}, 'registerBeginTime': {'description': '注册开始时间', 'type': 'date'}, 'registerEndTime': {'description': '注册结束时间', 'type': 'date'}, 'selectBeginTime': {'description': '互选开始时间', 'type': 'date'}, 'selectEndTime': {'description': '互选结束时间', 'type': 'date'}, 'chargeRule': {'description': '收费标准', 'type': 'string'}, 'boyBeginAge': {'description': '男生开始收费年龄', 'type': 'integer'}, 'girlBeginAge': {'description': '女生开始收费年龄', 'type': 'integer'}, 'increment': {'description': '根据年龄递增的收费', 'type': 'integer'}, 'wechat': {'description': '发起人微信号', 'type': 'string'}, 'realName': {'description': '是否需要真实信息', 'type': 'bool'}}}},
    ('activity', 'POST'): {'args': {'required': ['aID'], 'properties': {'aID': {'description': '活动的ID', 'type': 'string'}}}},
    ('activity', 'GET'): {'args': {'required': ['begin', 'isCurrent'], 'properties': {'begin': {'description': '开始的编号，分页使用', 'type': 'integer'}, 'isCurrent': {'description': '是否是历史活动', 'type': 'bool'}}}},
    ('pool', 'GET'): {'args': {'required': ['begin'], 'properties': {'begin': {'description': '分页开始编号', 'type': 'integer'}}}},
    ('pool', 'POST'): {'args': {'required': ['pID'], 'properties': {'pID': {'description': '候选池编号', 'type': 'string'}}}},
    ('pool', 'PUT'): {'args': {'required': ['createTime', 'city', 'realRequired', 'initChance', 'removeTime', 'baseCharge', 'boyBegin', 'girlBegin', 'ageIncrement', 'sexIncrement', 'requirement'], 'properties': {'createTime': {'description': '创建时间', 'type': 'date'}, 'city': {'description': '城市', 'type': 'string'}, 'realRequired': {'description': '是否需要真实信息', 'type': 'bool'}, 'initChance': {'description': '初始的允许成功次数', 'type': 'integer'}, 'removeTime': {'description': '自动到期时间', 'type': 'integer'}, 'baseCharge': {'description': '基础费用', 'type': 'float'}, 'boyBegin': {'description': '男生开始征收', 'type': 'integer'}, 'girlBegin': {'description': '女生开始征收', 'type': 'integer'}, 'ageIncrement': {'description': '每小一岁的增加', 'type': 'float'}, 'sexIncrement': {'description': '每多一位异性的增加', 'type': 'float'}, 'requirement': {'description': '加入要求', 'type': 'string'}}}},
    ('pool_love', 'GET'): {'args': {'required': ['begin'], 'properties': {'begin': {'description': '开始号', 'type': 'integer'}}}},
}

filters = {
    ('user', 'POST'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('user', 'PUT'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('user_info', 'PUT'): {200: {'headers': None, 'schema': None}},
    ('user_info', 'GET'): {200: {'headers': None, 'schema': None}},
    ('user_info_uID', 'POST'): {200: {'headers': None, 'schema': None}},
    ('activity_aID', 'GET'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('activity', 'PUT'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('activity', 'POST'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('activity', 'GET'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('pool_pID', 'GET'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('pool', 'GET'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('pool', 'POST'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('pool', 'PUT'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('pool_love', 'GET'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('pool_love_uID', 'GET'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
    ('pool_love_uID', 'POST'): {200: {'headers': {'x-next': {'type': 'string', 'description': 'A link to the next page of responses'}}, 'schema': None}},
}

scopes = {
}


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value, get_first=True):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    results = normalize(schema, value, type_defaults)
    if get_first:
        return results[0]
    return results


def normalize(schema, data, required_defaults=None):
    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            return getattr(self.data, key, default)

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

        def keys(self):
            if isinstance(self.data, dict):
                return list(self.data.keys())
            return list(getattr(self.data, '__dict__', {}).keys())

        def get_check(self, key, default=None):
            if isinstance(self.data, dict):
                value = self.data.get(key, default)
                has_key = key in self.data
            else:
                try:
                    value = getattr(self.data, key)
                except AttributeError:
                    value = default
                    has_key = False
                else:
                    has_key = True
            return value, has_key

    def _merge_dict(src, dst):
        for k, v in six.iteritems(dst):
            if isinstance(src, dict):
                if isinstance(v, dict):
                    r = _merge_dict(src.get(k, {}), v)
                    src[k] = r
                else:
                    src[k] = v
            else:
                src = {k: v}
        return src

    def _normalize_dict(schema, data):
        result = {}
        if not isinstance(data, DataWrapper):
            data = DataWrapper(data)

        for _schema in schema.get('allOf', []):
            rs_component = _normalize(_schema, data)
            _merge_dict(result, rs_component)

        for key, _schema in six.iteritems(schema.get('properties', {})):
            # set default
            type_ = _schema.get('type', 'object')

            # get value
            value, has_key = data.get_check(key)
            if has_key:
                result[key] = _normalize(_schema, value)
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                if type_ in required_defaults:
                    result[key] = required_defaults[type_]
                else:
                    errors.append(dict(name='property_missing',
                                       message='`%s` is required' % key))

        additional_properties_schema = schema.get('additionalProperties', False)
        if additional_properties_schema is not False:
            aproperties_set = set(data.keys()) - set(result.keys())
            for pro in aproperties_set:
                result[pro] = _normalize(additional_properties_schema, data.get(pro))

        return result

    def _normalize_list(schema, data):
        result = []
        if hasattr(data, '__iter__') and not isinstance(data, dict):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if schema is True or schema == {}:
            return data
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if type_ not in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors
