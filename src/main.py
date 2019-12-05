# -*- coding: utf-8 -*-
"""Main story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.common.times import COMMON_TIMES
from config import PERSONS, CHARAS, STAGES, DAYS, TIMES, ITEMS, WORDS


## main
def world():
    """Create a world.
    """
    w = World("")
    w.set_times(COMMON_TIMES)
    w.set_db(PERSONS, CHARAS,
            STAGES, DAYS, TIMES,
            ITEMS,
            WORDS)
    return w

def story(w: World):
    return w.story("Sample",
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

