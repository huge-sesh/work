from work import O, Component
import physics, player

prefabs = {
    'player' : [physics.Physics, player.Player]
}

def make(name):
    obj = O()
    for item in prefabs[name]: 
        if type(item) == 'tuple': item[0](obj, **item[1])
        else: item(obj)
    return obj

