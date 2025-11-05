def is_valid(self, raise_exception=False):
    try:
        return super(ClientSerializer, self).is_valid(raise_exception)
    except exceptions.ValidationError as e:
        if 'email' in e.detail:
            for i in range(len(e.detail['email'])):
                if e.detail['email'][i] == UniqueValidator.message:
                    e.detail['email'][i] = {'code': 'not-unique'}
        raise e
