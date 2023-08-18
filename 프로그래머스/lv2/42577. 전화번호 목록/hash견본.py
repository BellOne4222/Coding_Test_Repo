# 해시맵 생성
hash_map = {}

# 데이터 삽입
hash_map["key1"] = "value1"
hash_map["key2"] = "value2"

# 데이터 조회
print(hash_map["key1"])  # 출력: "value1"
print(hash_map["key2"])  # 출력: "value2"

# 존재하지 않는 키 조회 (KeyError 예외 처리 필요)
print(hash_map["key3"])  # KeyError 발생

# 존재 여부 확인
if "key1" in hash_map:
    print("key1 exists!")  # 출력: "key1 exists!"

# 데이터 삭제
del hash_map["key1"]

# 데이터 삭제 (KeyError 예외 처리 필요)
del hash_map["key3"]  # KeyError 발생