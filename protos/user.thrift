struct UserInfo {
  1: required i32 userId;
  2: required i32 gameId;
  3: optional string clientId;
  4: optional string authorCode;
}

struct Action {
  1: required i32 userId;
  2: required i32 gameId;
  3: optional string clientId;
  4: optional string resCmd;
}


