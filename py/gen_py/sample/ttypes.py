#
# Autogenerated by Thrift Compiler (0.12.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class PhoneType(object):
    MOBILE = 0
    HOME = 1
    WORK = 2

    _VALUES_TO_NAMES = {
        0: "MOBILE",
        1: "HOME",
        2: "WORK",
    }

    _NAMES_TO_VALUES = {
        "MOBILE": 0,
        "HOME": 1,
        "WORK": 2,
    }


class AddressBook(object):
    """
    Attributes:
     - people

    """


    def __init__(self, people=None,):
        self.people = people

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.people = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = Person()
                        _elem5.read(iprot)
                        self.people.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('AddressBook')
        if self.people is not None:
            oprot.writeFieldBegin('people', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.people))
            for iter6 in self.people:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.people is None:
            raise TProtocolException(message='Required field people is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Person(object):
    """
    Attributes:
     - name
     - id
     - email
     - money
     - work_status
     - phones
     - maps

    """


    def __init__(self, name=None, id=None, email=None, money=None, work_status=None, phones=None, maps=None,):
        self.name = name
        self.id = id
        self.email = email
        self.money = money
        self.work_status = work_status
        self.phones = phones
        self.maps = maps

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.email = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.DOUBLE:
                    self.money = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.work_status = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.phones = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = PhoneNumber()
                        _elem12.read(iprot)
                        self.phones.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.maps = MyMessage()
                    self.maps.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Person')
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.I32, 2)
            oprot.writeI32(self.id)
            oprot.writeFieldEnd()
        if self.email is not None:
            oprot.writeFieldBegin('email', TType.STRING, 3)
            oprot.writeString(self.email.encode('utf-8') if sys.version_info[0] == 2 else self.email)
            oprot.writeFieldEnd()
        if self.money is not None:
            oprot.writeFieldBegin('money', TType.DOUBLE, 4)
            oprot.writeDouble(self.money)
            oprot.writeFieldEnd()
        if self.work_status is not None:
            oprot.writeFieldBegin('work_status', TType.BOOL, 5)
            oprot.writeBool(self.work_status)
            oprot.writeFieldEnd()
        if self.phones is not None:
            oprot.writeFieldBegin('phones', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.phones))
            for iter13 in self.phones:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.maps is not None:
            oprot.writeFieldBegin('maps', TType.STRUCT, 7)
            self.maps.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.name is None:
            raise TProtocolException(message='Required field name is unset!')
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class PhoneNumber(object):
    """
    Attributes:
     - number
     - type

    """


    def __init__(self, number=None, type=None,):
        self.number = number
        self.type = type

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.number = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('PhoneNumber')
        if self.number is not None:
            oprot.writeFieldBegin('number', TType.STRING, 1)
            oprot.writeString(self.number.encode('utf-8') if sys.version_info[0] == 2 else self.number)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 2)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.number is None:
            raise TProtocolException(message='Required field number is unset!')
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class MyMessage(object):
    """
    Attributes:
     - mapfield

    """


    def __init__(self, mapfield=None,):
        self.mapfield = mapfield

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.MAP:
                    self.mapfield = {}
                    (_ktype15, _vtype16, _size14) = iprot.readMapBegin()
                    for _i18 in range(_size14):
                        _key19 = iprot.readI32()
                        _val20 = iprot.readI32()
                        self.mapfield[_key19] = _val20
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('MyMessage')
        if self.mapfield is not None:
            oprot.writeFieldBegin('mapfield', TType.MAP, 1)
            oprot.writeMapBegin(TType.I32, TType.I32, len(self.mapfield))
            for kiter21, viter22 in self.mapfield.items():
                oprot.writeI32(kiter21)
                oprot.writeI32(viter22)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class UserInfo(object):
    """
    Attributes:
     - name
     - id
     - email
     - money
     - work_status
     - phones
     - maps

    """


    def __init__(self, name=None, id=None, email=None, money=None, work_status=None, phones=None, maps=None,):
        self.name = name
        self.id = id
        self.email = email
        self.money = money
        self.work_status = work_status
        self.phones = phones
        self.maps = maps

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.id = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.email = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.DOUBLE:
                    self.money = iprot.readDouble()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.work_status = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.phones = []
                    (_etype26, _size23) = iprot.readListBegin()
                    for _i27 in range(_size23):
                        _elem28 = PhoneNumber()
                        _elem28.read(iprot)
                        self.phones.append(_elem28)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.maps = MyMessage()
                    self.maps.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('UserInfo')
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.I32, 2)
            oprot.writeI32(self.id)
            oprot.writeFieldEnd()
        if self.email is not None:
            oprot.writeFieldBegin('email', TType.STRING, 3)
            oprot.writeString(self.email.encode('utf-8') if sys.version_info[0] == 2 else self.email)
            oprot.writeFieldEnd()
        if self.money is not None:
            oprot.writeFieldBegin('money', TType.DOUBLE, 4)
            oprot.writeDouble(self.money)
            oprot.writeFieldEnd()
        if self.work_status is not None:
            oprot.writeFieldBegin('work_status', TType.BOOL, 5)
            oprot.writeBool(self.work_status)
            oprot.writeFieldEnd()
        if self.phones is not None:
            oprot.writeFieldBegin('phones', TType.LIST, 6)
            oprot.writeListBegin(TType.STRUCT, len(self.phones))
            for iter29 in self.phones:
                iter29.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.maps is not None:
            oprot.writeFieldBegin('maps', TType.STRUCT, 7)
            self.maps.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.name is None:
            raise TProtocolException(message='Required field name is unset!')
        if self.id is None:
            raise TProtocolException(message='Required field id is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(AddressBook)
AddressBook.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'people', (TType.STRUCT, [Person, None], False), None, ),  # 1
)
all_structs.append(Person)
Person.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'name', 'UTF8', None, ),  # 1
    (2, TType.I32, 'id', None, None, ),  # 2
    (3, TType.STRING, 'email', 'UTF8', None, ),  # 3
    (4, TType.DOUBLE, 'money', None, None, ),  # 4
    (5, TType.BOOL, 'work_status', None, None, ),  # 5
    (6, TType.LIST, 'phones', (TType.STRUCT, [PhoneNumber, None], False), None, ),  # 6
    (7, TType.STRUCT, 'maps', [MyMessage, None], None, ),  # 7
)
all_structs.append(PhoneNumber)
PhoneNumber.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'number', 'UTF8', None, ),  # 1
    (2, TType.I32, 'type', None, None, ),  # 2
)
all_structs.append(MyMessage)
MyMessage.thrift_spec = (
    None,  # 0
    (1, TType.MAP, 'mapfield', (TType.I32, None, TType.I32, None, False), None, ),  # 1
)
all_structs.append(UserInfo)
UserInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'name', 'UTF8', None, ),  # 1
    (2, TType.I32, 'id', None, None, ),  # 2
    (3, TType.STRING, 'email', 'UTF8', None, ),  # 3
    (4, TType.DOUBLE, 'money', None, None, ),  # 4
    (5, TType.BOOL, 'work_status', None, None, ),  # 5
    (6, TType.LIST, 'phones', (TType.STRUCT, [PhoneNumber, None], False), None, ),  # 6
    (7, TType.STRUCT, 'maps', [MyMessage, None], None, ),  # 7
)
fix_spec(all_structs)
del all_structs
