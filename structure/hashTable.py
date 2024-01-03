import collections


class HashMap:
    def __init__(self):
        self.size = 1000
        # collections.defaultdict(): 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성해줌
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # self.table[index]가 아닌 self.table[index].value로 비교하는 이유
        # -> 초기화에서 선언한 self.table이 collections.defaultdict(ListNode)이기 때문
        # -> defaultdict는 존재하지 않는 인덱스로 조회를 시도하면 에러를 발생시키지 않고 그 자리에서 바로 디폴트 객체를 생성
        # -> 해당 구문에서는 빈 ListNode 생성
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
        prev, p = p, p.next

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None