from dataclasses import dataclass
from random import Random
import numpy as np


@dataclass
class TreeNode:
    keys = [None] * 3
    childs = [None] * 4
    key_length = 0
    has_child = False


def search_node(root, key):
    if root.has_child:
        child_index = 0
        for idx, _key in enumerate(root.keys):
            if _key
        pass
    else:
        return root


def insert_node(root: TreeNode, key: int):
    if root is None:
        return TreeNode([key], [None])

    if root.has_child:
        pass
    else:
        # insertは葉ノードの場合のみ発生する
        if root.key_length < 3:
            root.keys = sorted(root.keys.append(key))
        else:
            # rotationが発生する

            pass

    return root


if __name__ == "__main__":
    r = Random()
    keys = [i for i in range(10)]
    r.shuffle(keys)

    print(keys)
