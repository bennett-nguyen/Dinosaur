import src.preload.assets as assets
from random import choice
from typing import Callable
from src.comp.export.pool_comp.cactus import Cactus
from src.comp.export.pool_comp.pteranodon import Pteranodon

class Pool:
    '''Manage pool objects'''
    
    def __init__(self, init_object_function: Callable[[], list[Cactus | Pteranodon]]):
        self._objects = init_object_function()

    def get_object(self) -> Cactus | Pteranodon:
        return self._objects.pop(self._objects.index(choice(self._objects)))

    def release_object(self, obj: Cactus | Pteranodon):
        self._objects.append(obj)

_one_small_cactus = [assets.Gallery.SMALL_CACTUS_1]
_two_small_cacti = [assets.Gallery.SMALL_CACTUS_1, assets.Gallery.SMALL_CACTUS_2]
_three_small_cacti = [assets.Gallery.SMALL_CACTUS_1, assets.Gallery.SMALL_CACTUS_4, assets.Gallery.SMALL_CACTUS_3]

_one_big_cactus = [assets.Gallery.BIG_CACTUS_1]
_two_big_cacti = [assets.Gallery.BIG_CACTUS_2, assets.Gallery.BIG_CACTUS_3]
_three_big_cacti = [assets.Gallery.BIG_CACTUS_2, assets.Gallery.BIG_CACTUS_WITH_SMALL_CACTUS, assets.Gallery.BIG_CACTUS_4]

_cacti_images = (_one_small_cactus, _two_small_cacti, _three_small_cacti, _one_big_cactus, _two_big_cacti, _three_big_cacti)

def _init_cactus():
    return [Cactus(cactus_image) for cactus_image in _cacti_images]

def _init_pteranodon():
    return [Pteranodon() for _ in range (5)]

cacti_pool = Pool(_init_cactus)
pteranodon_pool = Pool(_init_pteranodon)