import collections

# 해시맵 디자인
# 개별 체이닝 방식
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        # collections.defaultduct: 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성해줌
        self.h = collections.defaultdict(ListNode)

    def put(self, key, value):
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.h[index].value is None:
            self.h[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.h[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key):
        index = key % self.size
        if self.h[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.h[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key):
        index = key & self.size
        if self.h[index].value is None:
            return

        # 인덱스의 첫번째 노드일 때 삭제 처리
        p = self.h[index]
        if p.key == key:
            self.h[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


h = MyHashMap()
h.put(1,1)
h.put(2,2)
print(h.get(1))
print(h.get(3))
h.remove(1)
print(h.get(1))



