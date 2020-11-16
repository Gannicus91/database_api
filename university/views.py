from django.http import JsonResponse
from django.shortcuts import render, redirect
import psycopg2
from contextlib import closing
from django.views.decorators.csrf import csrf_exempt
import json


def teachers(request):
    db_login = request.COOKIES.get('db-login')
    db_password = request.COOKIES.get('db-password')
    try:
        with closing(
                psycopg2.connect(dbname='university', user=db_login, password=db_password, host='localhost')) as conn:
            cursor = conn.cursor()
            template_id = "'.*" + request.GET.get('id', '') + ".*'"
            template_first_name = "'.*" + request.GET.get('first_name', '') + ".*'"
            template_last_name = "'.*" + request.GET.get('last_naame', '') + ".*'"
            cursor.execute("SELECT id, first_name, last_naame FROM teachers "
                           "WHERE to_char(id, '9999') ~ {0} OR  first_name ~* {1} OR last_naame ~* {2} "
                           "ORDER BY id ".format(template_id, template_first_name, template_last_name))
            teachers_list = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
            data = {
                "table": 'teachers',
                "items": teachers_list,
                "headers": headers,
                "title": "Преподаватели",
            }
            return render(request, 'table.html', context=data)
    except Exception as e:
        return render(request, 'error.html', context={'message': e})


def subjects(request):
    db_login = request.COOKIES.get('db-login')
    db_password = request.COOKIES.get('db-password')
    try:
        with closing(
                psycopg2.connect(dbname='university', user=db_login, password=db_password, host='localhost')) as conn:
            cursor = conn.cursor()
            template_id = "'.*" + request.GET.get('id', '') + ".*'"
            template_name = "'.*" + request.GET.get('name', '') + ".*'"
            cursor.execute("SELECT id, name FROM subjects "
                           "WHERE to_char(id, '9999') ~ {0} OR  name ~* {1} "
                           "ORDER BY id ".format(template_id, template_name))
            teachers_list = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
            data = {
                "table": 'subjects',
                "items": teachers_list,
                "headers": headers,
                "title": "Предметы",
            }
            return render(request, 'table.html', context=data)
    except Exception as e:
        return render(request, 'error.html', context={'message': e})


def academic_plan(request):
    db_login = request.COOKIES.get('db-login')
    db_password = request.COOKIES.get('db-password')
    try:
        with closing(
                psycopg2.connect(dbname='university', user=db_login, password=db_password, host='localhost')) as conn:
            cursor = conn.cursor()
            template_id = "'.*" + request.GET.get('id', '') + ".*'"
            template_group = "'.*" + request.GET.get('group', '') + ".*'"
            template_subject = "'.*" + request.GET.get('subject', '') + ".*'"
            template_hours = "'.*" + request.GET.get('hours', '') + ".*'"
            cursor.execute(
                "SELECT academic_plan.id, groups.name AS group, subjects.name AS subject, academic_plan.hours "
                "FROM academic_plan "
                "JOIN subjects ON subjects.id = academic_plan.subject_id "
                "JOIN groups ON groups.id = academic_plan.group_id "
                "WHERE to_char(academic_plan.id, '9999') ~ {0} "
                "OR groups.name ~* {1} "
                "OR subjects.name ~* {2} "
                "OR to_char(academic_plan.hours, '9999') ~ {3} "
                "ORDER BY id".format(template_id, template_group, template_subject, template_hours))
            teachers_list = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
            data = {
                "table": 'academic_plan',
                "items": teachers_list,
                "headers": headers,
                "title": "Учебный план",
            }
            return render(request, 'table.html', context=data)
    except Exception as e:
        return render(request, 'error.html', context={'message': e})


def groups(request):
    db_login = request.COOKIES.get('db-login')
    db_password = request.COOKIES.get('db-password')
    try:
        with closing(
                psycopg2.connect(dbname='university', user=db_login, password=db_password, host='localhost')) as conn:
            cursor = conn.cursor()
            template_id = "'.*" + request.GET.get('id', '') + ".*'"
            template_name = "'.*" + request.GET.get('name', '') + ".*'"
            cursor.execute("SELECT * FROM groups "
                           "WHERE to_char(id, '9999') ~ {0} OR  name ~* {1} "
                           "ORDER BY id".format(template_id, template_name))
            teachers_list = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
            data = {
                "table": 'groups',
                "items": teachers_list,
                "headers": headers,
                "title": "Академические группы",
            }
            return render(request, 'table.html', context=data)
    except Exception as e:
        return render(request, 'error.html', context={'message': e})


def lessons(request):
    db_login = request.COOKIES.get('db-login')
    db_password = request.COOKIES.get('db-password')
    try:
        with closing(
                psycopg2.connect(dbname='university', user=db_login, password=db_password, host='localhost')) as conn:
            cursor = conn.cursor()
            template_id = "'.*" + request.GET.get('id', '') + ".*'"
            template_teacher = "'.*" + request.GET.get('teacher', '') + ".*'"
            template_group = "'.*" + request.GET.get('group', '') + ".*'"
            template_subject = "'.*" + request.GET.get('subject', '') + ".*'"
            cursor.execute(
                "SELECT lessons.id, teachers.last_naame AS teacher, groups.name AS group, subjects.name AS subject "
                "FROM lessons "
                "JOIN teachers ON teachers.id = lessons.teacher_id "
                "JOIN subjects ON subjects.id = lessons.subject_id "
                "JOIN groups ON groups.id = lessons.group_id "
                "WHERE to_char(lessons.id, '9999') ~ {0} "
                "OR teachers.last_naame ~* {1} "
                "OR groups.name ~* {2} "
                "OR subjects.name ~* {3} "
                "ORDER BY id".format(template_id, template_teacher, template_group, template_subject))
            teachers_list = cursor.fetchall()
            headers = [desc[0] for desc in cursor.description]
            data = {
                "table": 'lessons',
                "items": teachers_list,
                "headers": headers,
                "title": "Проведенные занятия",
            }
            return render(request, 'table.html', context=data)
    except Exception as e:
        return render(request, 'error.html', context={'message': e})


def login(request):
    return render(request, 'login.html')


def add_entity_page(request, table):
    db_login = request.COOKIES.get('db-login')
    db_password = request.COOKIES.get('db-password')
    try:
        with closing(
                psycopg2.connect(dbname='university', user=db_login, password=db_password, host='localhost')) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM {0} LIMIT 0".format(table))
            colnames = [desc[0] for desc in cursor.description]
            data = {
                "table": table,
                "colnames": colnames,
            }
            return render(request, 'add_entity.html', context=data)
    except Exception as e:
        return render(request, 'error.html', context={'message': e})


@csrf_exempt
def add_entity(request, table):
    if request.method == 'POST':
        db_login = request.COOKIES.get('db-login')
        db_password = request.COOKIES.get('db-password')
        try:
            with closing(
                    psycopg2.connect(dbname='university', user=db_login, password=db_password,
                                     host='localhost')) as conn:
                cursor = conn.cursor()
                data = json.loads(request.body)
                cols = ', '.join(data.keys())
                values = "'" + "', '".join(data.values()) + "'"
                query = "INSERT INTO {0} ({1}) values ({2})".format(table, cols, values)
                cursor.execute(query)
                conn.commit()
                return JsonResponse({'msg': 'success'})
        except Exception as e:
            return e


@csrf_exempt
def edit_delete_entity(request, table, item_id):
    db_login = request.COOKIES.get('db-login')
    db_password = request.COOKIES.get('db-password')
    if request.method == 'DELETE':
        try:
            with closing(
                    psycopg2.connect(dbname='university', user=db_login, password=db_password,
                                     host='localhost')) as conn:
                cursor = conn.cursor()
                query = "DELETE FROM {0} WHERE id={1}".format(table, item_id)
                cursor.execute(query)
                conn.commit()
                return JsonResponse({'msg': 'success'})
        except Exception as e:
            return e
    elif request.method == 'PATCH':
        try:
            with closing(
                    psycopg2.connect(dbname='university', user=db_login, password=db_password,
                                     host='localhost')) as conn:
                cursor = conn.cursor()
                data = json.loads(request.body)
                data.pop('id')
                set_part = []
                for key in data:
                    set_part.append(key + "='" + data[key] + "'")
                set_part = ", ".join(set_part)
                query = "UPDATE {0} SET {1} WHERE id={2}".format(table, set_part, item_id)
                cursor.execute(query)
                conn.commit()
                return JsonResponse({'msg': 'success'})
        except Exception as e:
            return e


def edit_entity_page(request, table, item_id):
    db_login = request.COOKIES.get('db-login')
    db_password = request.COOKIES.get('db-password')
    try:
        with closing(
                psycopg2.connect(dbname='university', user=db_login, password=db_password, host='localhost')) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM {0} WHERE id={1}".format(table, item_id))
            colnames = [desc[0] for desc in cursor.description]
            item = dict(zip(colnames, cursor.fetchall()[0]))
            data = {
                "table": table,
                "item": item,
                "item_id": item_id,
            }
            return render(request, 'edit_entity.html', context=data)
    except Exception as e:
        return render(request, 'error.html', context={'message': e})