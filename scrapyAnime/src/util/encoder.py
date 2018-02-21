from datetime import datetime

import json


class CustomEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime):
            return {'__datetime__': o.replace(microsecond=0).isoformat()}

        return {'__{}__'.format(o.__class__.__name__): o.__dict__}
