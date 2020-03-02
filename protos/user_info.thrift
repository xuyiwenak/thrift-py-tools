struct result {
  1:i32 gameId;
  2:i64 userId;
  3:UDATA udata;
  4:string loc;
  5:GDATA gdata;
}
struct UDATA {
    1: string pdevid;
    2: string mdevid;
    3: double isbind;
    4: string snsId;
    5: string name;
    6: string source;
    7: double diamond;
    8: string address;
    9: double sex;
    10: double state ;
    11:double payCount;
    12:string snsinfo;
    13:double vip;
    14:double dayang;
    15:string idcardno;
    16:string phonenumber;
    17:string truename;
    18:string detect_phonenumber;
    19:string lang;
    20:string country;
    21:string signature;
    22:double set_name_sum;
    23:double coupon ;
    24:string purl ;
    25:double beauty ;
    26:double charm ;
    27:string password ;
    28:string bindMobile ;
    29:string createTime ;
    30:double coin ;
    31:double chip ;
    32:bool isBeauty ;
    33:VIPINFO vipInfo;
    34:ASSISTANCE assistance;
    35:string email;
}

 struct VIPINFO {
   1:double level;
   2:string name;
   3:double exp;
   4:double expCurrent;
   5:double expNext;
 }

 struct ASSISTANCE {
   1:double count;
   2:double limit;
  }
  struct GDATA {
    1:double lastRoleId;
    2:double serverId;
    3:double isNewRoleId;
    4:string headUrl;
    5:double serverTimestamp;
  }