import json

def getStartObjests():
    objs = {
        'auto1': 
        {
            'enabled':'True',
            'number':'a777aa99',
            'model':'Mercedes Benz',
            'params':{
                'Скорость':'30км/ч',
                'Обороты':'3091',
                'Водитель':'Иванов',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
                'Камера#2':'https://localhost:8012',
                'Камера#3':'https://localhost:8012',
                'Камера#4':'https://localhost:8012',
                'Камера#5':'https://localhost:8012',
            },
            'position_n':'6977760.708997443',
            'position_e':'4016570.740906363',
        },
        'auto2':
        {
            'enabled':'True',
            'number':'e758op36',
            'model':'Volkswagen Jetta',
            'params':{
                'Скорость':'55км/ч',
                'Обороты':'2098',
                'Водитель':'Петров',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
                'Камера#2':'https://localhost:8012',
                'Камера#4':'https://localhost:8012',
                'Камера#5':'https://localhost:8012',
                'Камера#6':'https://localhost:8012',
                'Камера#7':'https://localhost:8012',
                'Камера#8':'https://localhost:8012',
            },
            'position_n':'6990748.408997443',
            'position_e':'4016499.440906363',
        },
        'auto3':
        {
            'enabled':'False',
            'number':'k918cc57',
            'model':'Nissan Juke',
            'params':{
                'Скорость':'51км/ч',
                'Обороты':'3012',
                'Водитель':'Сидоров',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
            },
            'position_n':'6960655.308997443',
            'position_e':'4035489.640906363',
        },
        'auto4':
        {
            'enabled':'True',
            'number':'k899ae57',
            'model':'Opel Astra',
            'params':{
                'Скорость':'45км/ч',
                'Обороты':'123',
                'Водитель':'Степанов',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
                'Камера#2':'https://localhost:8011',
                'Камера#3':'https://localhost:8011',
                'Камера#4':'https://localhost:8011',
            },
            'position_n':'6955499.308997443',
            'position_e':'4016601.840906363',
        },
        'auto5':
        {
            'enabled':'False',
            'number':'e817aa99',
            'model':'Chevrolet Cruze',
            'params':{
                'Скорость':'33км/ч',
                'Обороты':'4810',
                'Водитель':'Тимофеев',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
                'Камера#2':'https://localhost:8011',
                'Камера#3':'https://localhost:8011',
                'Камера#4':'https://localhost:8011',
            },
            'position_n':'6917515.708997443',
            'position_e':'4076666.640906363',
        },
        'auto6':
        {
            'enabled':'True',
            'number':'c832mm36',
            'model':'BMW X5',
            'params':{
                'Скорость':'90км/ч',
                'Обороты':'1098',
                'Водитель':'Титов',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
                'Камера#2':'https://localhost:8011',
            },
            'position_n':'6907781.308997443',
            'position_e':'4056477.640906363',
        },
        'auto7':
        {
            'enabled':'True',
            'number':'e239ea57',
            'model':'Lada Granta',
            'params':{
                'Скорость':'94км/ч',
                'Обороты':'2001',
                'Водитель':'Федоров',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
                'Камера#2':'https://localhost:8011',
                'Камера#3':'https://localhost:8011',
                'Камера#4':'https://localhost:8011',
                'Камера#5':'https://localhost:8011',
            },
            'position_n':'6928067.298997443',
            'position_e':'4006345.940906363',
        },
        'auto8':
        {
            'enabled':'True',
            'number':'a221ak36',
            'model':'Audi R8',
            'params':{
                'Скорость':'104км/ч',
                'Обороты':'2701',
                'Водитель':'Синицин',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
                'Камера#2':'https://localhost:8011',
                'Камера#3':'https://localhost:8011',
            },
            'position_n':'6957810.398997443',
            'position_e':'4046659.540906363',
        },
        'auto9':
        {
            'enabled':'True',
            'number':'o545ko55',
            'model':'Mitsubishi Lancer',
            'params':{
                'Скорость':'123км/ч',
                'Обороты':'5432',
                'Водитель':'Федосеев',
            },
            'stream_links':{
            },
            'position_n':'6958670.398997443',
            'position_e':'4048659.540906363',
        },
        'auto10':
        {
            'enabled':'True',
            'number':'k919ao57',
            'model':'Ford Focus',
            'params':{
                'Скорость':'174км/ч',
                'Обороты':'3009',
                'Водитель':'Пупкин',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
                'Камера#2':'https://localhost:8011',
                'Камера#3':'https://localhost:8011',
                'Камера#4':'https://localhost:8011',
                'Камера#5':'https://localhost:8011',
                'Камера#6':'https://localhost:8011',
            },
            'position_n':'6957810.398997443',
            'position_e':'4040659.540906363',
        },
        'auto11':
        {
            'enabled':'True',
            'number':'c654pc57',
            'model':'Cadillac Escalade',
            'params':{
                'Скорость':'187км/ч',
                'Обороты':'4093',
                'Водитель':'Воронин',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
            },
            'position_n':'6943810.398997443',
            'position_e':'4043659.540906363',
        },
        'auto12':
        {
            'enabled':'False',
            'number':'p112pc57',
            'model':'Jeep Compass',
            'params':{
                'Скорость':'20км/ч',
                'Обороты':'1987',
                'Водитель':'Поляков',
            },
            'stream_links':{
            },
            'position_n':'6945810.398997443',
            'position_e':'4053987.540906363',
        },
        'auto13':
        {
            'enabled':'False',
            'number':'o056cp777',
            'model':'Hummer EV',
            'params':{
                'Скорость':'98км/ч',
                'Обороты':'1098',
                'Водитель':'Букин',
            },
            'stream_links':{
            },
            'position_n':'6950810.398997443',
            'position_e':'4036659.540906363',
        },
        'auto14':
        {
            'enabled':'True',
            'number':'o002pe777',
            'model':'LADA XRay',
            'params':{
                'Скорость':'100км/ч',
                'Обороты':'3019',
                'Водитель':'Понарин',
            },
            'stream_links':{
                'Камера#1':'https://localhost:8011',
                'Камера#2':'https://localhost:8011',
                'Камера#3':'https://localhost:8011',
            },
            'position_n':'6933810.398997443',
            'position_e':'4076987.540906363',
        },
        'auto15':
        {
            'enabled':'True',
            'number':'e821ok67',
            'model':' LADA Niva',
            'params':{
                'Скорость':'89км/ч',
                'Обороты':'2376',
                'Водитель':'Петренко',
            },
            'stream_links':{
            },
            'position_n':'6945810.398997443',
            'position_e':'4026659.540906363',
        },
    }
    return objs

position_n = 6977760.708997443
position_e = 4016570.740906363

def getCoordinatesObjests():
    global position_n, position_e
    coor = json.dumps({
        'auto1': 
        {
            'position_n': str(position_n + 11.0),
            'position_e': str(position_e + 181.0),
        },
        'auto2': 
        {
            'position_n': str(position_n + 1188.0),
            'position_e': str(position_e - 15717.0),
        },
        'auto3': 
        {
            'position_n': str(position_n + 14571.0),
            'position_e': str(position_e + 1134.0),
        },
        'auto4': 
        {
            'position_n': str(position_n - 1451.0),
            'position_e': str(position_e + 15721.0),
        },
        'auto5': 
        {
            'position_n': str(position_n - 1134.0),
            'position_e': str(position_e + 1451.0),
        },
        'auto6': 
        {
            'position_n': str(position_n - 8811.0),
            'position_e': str(position_e - 1541.0),
        },
        'auto7': 
        {
            'position_n': str(position_n + 121.0),
            'position_e': str(position_e + 1111.0),
        },
        'auto8': 
        {
            'position_n': str(position_n - 1211.0),
            'position_e': str(position_e + 12471.0),
        },
        'auto9': 
        {
            'position_n': str(position_n + 2141.0),
            'position_e': str(position_e - 45311.0),
        },
        'auto10': 
        {
            'position_n': str(position_n - 1156.0),
            'position_e': str(position_e - 42111.0),
        },
        'auto11': 
        {
            'position_n': str(position_n - 171.0),
            'position_e': str(position_e + 15631.0),
        },
        'auto12': 
        {
            'position_n': str(position_n - 1471.0),
            'position_e': str(position_e - 14571.0),
        },
        'auto13': 
        {
            'position_n': str(position_n + 11091.0),
            'position_e': str(position_e + 11231.0),
        },
        'auto14': 
        {
            'position_n': str(position_n - 143471.0),
            'position_e': str(position_e - 14571.0),
        },
        'auto15': 
        {
            'position_n': str(position_n + 15091.0),
            'position_e': str(position_e + 61231.0),
        },
    })
    position_e += 50.0
    position_n += 50.0
    return coor