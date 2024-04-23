<h1>These API is based on Django Rest Framework</h1>
<h3>We cannot GET in browser, It will only perform CURD operation by admin using POST</h3> <br>
<h4>Package Installation: pip install djangorestframework</h4>
<h4>
  Add 'rest_framework' to your INSTALLED_APPS setting: <br>
  INSTALLED_APPS = [ <br>
    'rest_framework', <br>
] <br>
</h4>

<h4>
  Allow read-only access for unauthenticated users: <br>
  REST_FRAMEWORK = { <br>
    'DEFAULT_PERMISSION_CLASSES': [ <br>
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly' <br>
    ]
}
</h4>
