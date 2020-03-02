
struct AddressBook {
  1: required list<Person> people;
}
struct Person {
  1: required string name;
  2: required i32 id;
  3: optional string email;
  4: optional double money;
  5: optional bool work_status;
  6: optional list<PhoneNumber> phones;
  7: optional MyMessage maps;
}

struct PhoneNumber {
    1: required string number;
    2: required PhoneType type;
}

enum PhoneType {
    MOBILE = 0,
    HOME = 1,
    WORK = 2
}

struct MyMessage {
  1: map<i32, i32> mapfield;
}

struct UserInfo {
  1: required string name;
  2: required i32 id;
  3: optional string email;
  4: optional double money;
  5: optional bool work_status;
  6: optional list<PhoneNumber> phones;
  7: optional MyMessage maps;
}
