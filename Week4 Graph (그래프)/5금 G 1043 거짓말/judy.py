# 과장할 수 있는 파티의 최대 수
# 과장할 때는 진실을 알고 있는 사람들이 존재하면 안된다.
# 사람들은 같은 이야기만 들어야한다.

# 각 파티의 사람들을 이진분류로 그룹 2개로 나누면 되겠다
# 한 파티에는 같은 그룹의 사람들만 존재해야한다.

people_N, party_M = map(int, input().split())
scary_people = int(input())
