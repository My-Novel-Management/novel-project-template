# -*- coding: utf-8 -*-
"""Main story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import DAYS, ITEMS, LAYERS, PERSONS, RUBIS, STAGES, TIMES, WORDS
from src.demo.main import ep_demo


## main
def ch_main(w: World):
    return w.chapter("main",
            ep_demo(w),
            )

def world():
    """Create a world.
    """
    w = World("title")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.buildDB(PERSONS,
            STAGES, ITEMS, DAYS, TIMES, WORDS,
            RUBIS, LAYERS)
    w.entryBlock(
            )
    return w


def main(): # pragma: no cover
    w = world()
    return w.build(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

