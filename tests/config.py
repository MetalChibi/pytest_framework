class Config:
    def __init__(self, env):

        if env.lower() not in ['dev', 'qa']:
            raise Exception(f'{env} is not a supported environment')

        self.base_url = {
            'dev': 'https://mydevenv.com',
            'qa': 'https://myqaenv.com'
        }[env]

        self.app_port = {
            'dev': 8080,
            'qa': 80
        }[env]

        