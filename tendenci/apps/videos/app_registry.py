from tendenci.apps.registry.sites import site
from tendenci.apps.registry.base import AppRegistry
from tendenci.apps.videos.models import Video


class VideoRegistry(AppRegistry):
    version = '1.0'
    author = 'Tendenci - The Open Source AMS for Associations'
    author_email = 'programmers@tendenci.com'
    description = 'Add video and display them in a grid format'

    event_logs = {
        'video':{
            'base':('1200000','993355'),
            'add':('1200100','119933'),
            'edit':('1200200','EEDD55'),
            'delete':('1200300','AA2222'),
            'search':('1200400','CC55EE'),
            'view':('1200500','55AACC'),
        }
    }

site.register(Video, VideoRegistry)
