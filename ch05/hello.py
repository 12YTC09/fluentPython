#5-12 Bobo知道hello需要一個person引數,並且從HTTP請求拿取它

import bobo

@bobo.query('/')
def hello(person):
    return 'Hello %s!' %person
