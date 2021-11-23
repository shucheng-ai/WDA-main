### install

```
sh setup.sh
```

### init wda object

``` 
from wda_decorators import WDA
wda = WDA(
    db_host="127.0.0.1",
    db_port=5432,
    db_username="admin",
    db_password="admin",
)
```


### get auth user
``` 
@wda.wda_auth
def func(**kwargs):
    user = kwargs['wda_user']
```

### get user groups
``` 
@wda.wda_auth
@wda.wda_group_required()
def func(**kwargs):
    user_groups = kwargs.get("wda_user_groups")
```

### get permission
``` 
@wda.wda_auth
@wda.wda_permission_required(permission="some_permission")
def func(**kwargs):
    has_permission = kwargs['wda_has_permissions']
    user_permissions = kwargs.get("wda_user_permissions")
```

### flask demo

`cat demo.py`
