# coding=utf-8
# auth: evan xu
# file: client.py
# date: 2020/1/20 4:13 PM

from websocket import create_connection
from gen_py.sample.ttypes import *
from gen_py.user_info.ttypes import *
from gen_py.user.ttypes import *
import json
import msgpack
from thrift.TSerialization import serialize, deserialize
import threading
import time

class ThriftJSONEncoder(json.JSONEncoder):

    def default(self, o):
        if not hasattr(o, 'thrift_spec'):
            return super(ThriftJSONEncoder, self).default(o)

        spec = getattr(o, 'thrift_spec')
        ret = {}
        for field in spec:
            if field is None:
                continue
            (tag, field_ttype, field_name, field_ttype_info, default) = field
            if field_name in o.__dict__:
                val = o.__dict__[field_name]
                if val != default:
                    ret[field_name] = val
        return ret
class ThriftJSONDecoder(json.JSONDecoder):

    def __init__(self, *args, **kwargs):
        self._thrift_class = kwargs.pop('thrift_class')
        super(ThriftJSONDecoder, self).__init__(*args, **kwargs)

    def decode(self, json_str):
        if isinstance(json_str, dict):
            dct = json_str
        else:
            dct = super(ThriftJSONDecoder, self).decode(json_str)
        return self._convert(dct, TType.STRUCT,
                             (self._thrift_class, self._thrift_class.thrift_spec))

    def _convert(self, val, ttype, ttype_info):
        if ttype == TType.STRUCT:
            (thrift_class, thrift_spec) = ttype_info
            ret = thrift_class()
            for field in thrift_spec:
                if field is None:
                    continue
                (tag, field_ttype, field_name, field_ttype_info, dummy) = field
                if field_name not in val:
                    continue
                converted_val = self._convert(val[field_name], field_ttype, field_ttype_info)
                setattr(ret, field_name, converted_val)
        elif ttype == TType.LIST:
            if len(ttype_info)>2:
                ttype_info=ttype_info[0:2]
            (element_ttype, element_ttype_info) = ttype_info
            ret = [self._convert(x, element_ttype, element_ttype_info) for x in val]
        elif ttype == TType.SET:
            if len(ttype_info)>2:
                ttype_info=ttype_info[0:2]
            (element_ttype, element_ttype_info) = ttype_info
            ret = [self._convert(x, element_ttype, element_ttype_info) for x in val]
            (element_ttype, element_ttype_info) = ttype_info
            ret = set([self._convert(x, element_ttype, element_ttype_info) for x in val])
        elif ttype == TType.MAP:
            if len(ttype_info)>4:
                print ttype_info
                ttype_info=ttype_info[0:4]
            (key_ttype, key_ttype_info, val_ttype, val_ttype_info) = ttype_info
            ret = dict([(self._convert(k, key_ttype, key_ttype_info),
                         self._convert(v, val_ttype, val_ttype_info)) for (k, v) in val.iteritems()])
        elif ttype == TType.STRING:
            if isinstance(val, unicode):
                ret = val.encode("utf8")
            else:
                ret = str(val)
        elif ttype == TType.DOUBLE:
            ret = float(val)
        elif ttype == TType.I64:
            ret = long(val)
        elif ttype == TType.I32 or ttype == TType.I16 or ttype == TType.BYTE:
            ret = int(val)
        elif ttype == TType.BOOL:
            ret = bool(val)
        else:
            raise TypeError('Unrecognized thrift field type: %d' % ttype)
        return ret

def json2thrift(json_str, thrift_class):
    return json.loads(json_str, cls=ThriftJSONDecoder, thrift_class=thrift_class)


if __name__ == '__main__':

    addr="ws://192.168.20.114:8013/?base64=0&mask=0&binary=1"
    ws = create_connection(addr)

    a = UserInfo()
    a.userId=12321
    a.gameId=9999
    a.clientId="H5_2.0_weixin.weixin.0-hall20418.weixin.dasfs"

    binStr=serialize(a)
    bindDict = {
        "cmd": "bind_user5",
        "subproto": [
            "param/thrift/user.UserInfo"
        ],
        "param": binStr
    }
    packer = msgpack.packb(bindDict, use_bin_type=True)
    # 先建立用户连接
    ws.send(packer)
    retData =  ws.recv()
    print retData
    # 发送第一条消息
    b = Action()
    b.userId= 12321
    b.gameId= 11111
    b.clientId="H5_2.0_weixin.weixin.0-hall20418.weixin.dasfs"

    bodyBin = serialize(b)
    bodyDict={
        "cmd": "helloUT",
        "subproto": [
            "param/thrift/user.Action"
        ],
        "param": bodyBin
    }
    body = msgpack.packb(bodyDict, use_bin_type=True)
    ws.send(body)
    print time.strftime('%Y-%m-%d %H:%M:%S')
    body = ws.recv()
    body=body[4:]
    msgDict = msgpack.unpackb(body)
    print msgDict
    binStr=msgDict.get("result")
    protoObj = Action()
    x = deserialize(protoObj, binStr)
    print x
    print x.userId, x.gameId, x.clientId, x.resCmd
    ws.close()
