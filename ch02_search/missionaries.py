from __future__ import annotations
from typing import List, Optional
from generic_search import bfs, Node, node_to_path

MAX_NUM: int = 15


class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm: int = missionaries
        self.wc: int = cannibals
        self.em: int = MAX_NUM - self.wm
        self.ec: int = MAX_NUM - self.wc
        self.boat: bool = boat

    def __str__(self) -> str:
        return f"서쪽 강둑에는 {self.wm}의 선교사와 {self.wc}명의 식인종이 있다.\n동쪽 강둑에는 {self.em}의 선교사와 {self.ec}명의 식인종이 있다.\n배는 {'서쪽' if self.boat else '동쪽'} 강둑에 있다."

    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM

    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True

    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []
        if self.boat:
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else:
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
            if (self.ec > 0) and (self.em > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))
        return [x for x in sucs if x.is_legal]


def display_solution(path: List[MCState]):
    if len(path) == 0:
        return
    old_state: MCState = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print(
                f"{old_state.em - current_state.em}명의 선교사와 {old_state.ec - current_state.ec} 명의 식인종이 동쪽 강둥에서 서쪽 강둑으로 갔다.\n"
            )
        else:
            print(
                f"{old_state.wm - current_state.wm}명의 선교사와 {old_state.wc - current_state.wc} 명의 식인종이 서쪽 강둑에서 동쪽 강둑으로 갔다.\n"
            )
        print(current_state)
        old_state = current_state


if __name__ == "__main__":
    start: MCState = MCState(MAX_NUM, MAX_NUM, True)
    solution: Optional[Node[MCState]] = bfs(
        start, MCState.goal_test, MCState.successors
    )
    if solution is None:
        print("답을 찾을 수 없네요")
    else:
        path: List[MCState] = node_to_path(solution)
        display_solution(path)
