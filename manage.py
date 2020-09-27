#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
'''
0.通过表单或链接
<a href="/index/">index</a>
1.指定路径
http://127.0.0.1:8000/index/
2.打开urls配置文件 setting.py
ROOT_URLCONF = 'gest2.urls'
3.urls.py 找到views
path('index/',views.index)
4.index 函数  return HttpResponse 对象'''
# sessionid 7iq612wvg3nsd6g1dau6fw3yn4cixw2y
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gest2.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
