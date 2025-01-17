class Account:
    '''Represents Account entity.

    This class holds user-specific information and is used
    for authorization.

    :param str id: account id
    :param dict details: additional details of an account
    '''

    def __init__(
            self, id, username, permissions, is_admin=False, **details):
        self.id = id
        self.username = username
        self.permissions = permissions
        self.is_admin = is_admin
        self.details = details

    def can_read(self, collection_name):
        _permission = self.permissions.get(str(collection_name))
        if self.is_admin:
            return self.is_admin
        if isinstance(_permission, (list, set)):
            return 'read' in _permission
        if isinstance(_permission, str):
            return _permission in ('read', 'modify')
        return False

    def can_modify(self, collection_name):
        _permission = self.permissions.get(str(collection_name))
        if self.is_admin:
            return self.is_admin
        if isinstance(_permission, (list, set)):
            return 'write' in _permission
        if isinstance(_permission, str):
            return _permission == 'modify'
        return False

    def __repr__(self):
        return (
            'Account(username={}, is_admin={})'
            .format(self.username, self.is_admin))
