from django.shortcuts import render
import psycopg2
from contextlib import closing


def index(request):
    return render(request, 'index.html')


def teachers(request):
    with closing(psycopg2.connect(dbname='university', user='maxim', password='password', host='localhost')) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, first_name, last_name FROM teachers ORDER BY id ")
        teachers_list = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]
        data = {
            "teachers_list": teachers_list,
            "headers": headers,
            "title": "Преподаватели",
        }
        return render(request, 'table.html', context=data)


def subjects(request):
    with closing(psycopg2.connect(dbname='university', user='maxim', password='password', host='localhost')) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM subjects ORDER BY id")
        teachers_list = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]
        data = {
            "teachers_list": teachers_list,
            "headers": headers,
            "title": "Предметы",
        }
        return render(request, 'table.html', context=data)


def academic_plan(request):
    with closing(psycopg2.connect(dbname='university', user='maxim', password='password', host='localhost')) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT academic_plan.id, groups.name AS group, subjects.name AS subject, academic_plan.hours "
            "FROM academic_plan "
            "JOIN subjects ON subjects.id = academic_plan.subject_id "
            "JOIN groups ON groups.id = academic_plan.group_id "
            "ORDER BY id")
        teachers_list = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]
        data = {
            "teachers_list": teachers_list,
            "headers": headers,
            "title": "Учебный план",
        }
        return render(request, 'table.html', context=data)


def groups(request):
    with closing(psycopg2.connect(dbname='university', user='maxim', password='password', host='localhost')) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM groups ORDER BY id")
        teachers_list = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]
        data = {
            "teachers_list": teachers_list,
            "headers": headers,
            "title": "Академические группы",
        }
        return render(request, 'table.html', context=data)


def lessons(request):
    with closing(psycopg2.connect(dbname='university', user='maxim', password='password', host='localhost')) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT lessons.id, teachers.last_name AS teacher, groups.name AS group, subjects.name AS subject "
            "FROM lessons "
            "JOIN teachers ON teachers.id = lessons.teacher_id "
            "JOIN subjects ON subjects.id = lessons.subject_id "
            "JOIN groups ON groups.id = lessons.group_id "
            "ORDER BY id")
        teachers_list = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description]
        data = {
            "teachers_list": teachers_list,
            "headers": headers,
            "title": "Проведенные занятия",
        }
        return render(request, 'table.html', context=data)
