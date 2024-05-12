from datetime import datetime

from sqlalchemy import delete, insert

from courses.models import Course, Topic
from database import session_maker
from games.models import Game
from users.models import User


async def insert_courses_and_topics():
    async with session_maker() as session:
        # Вставляем данные в таблицу course
        stmt = insert(Course).values([
            {'title': 'Physics', 'is_active': True, 'is_life': True},
            {'title': 'Mathematics', 'is_active': True, 'is_life': True},
            {'title': 'Python Programming', 'is_active': True, 'is_life': True}
        ])
        await session.execute(stmt)

        # Вставляем данные в таблицу topic для курса "Physics"
        stmt = insert(Topic).values([
            {'title': 'Classical Mechanics', 'text': 'Introduction to classical mechanics.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 10,
             'cost': 0, 'course_id': 1},
            {'title': 'Thermodynamics', 'text': 'Basic principles of thermodynamics.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 15,
             'cost': 0, 'course_id': 1},
            {'title': 'Electromagnetism', 'text': 'Introduction to electromagnetism.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 20,
             'cost': 0, 'course_id': 1},
            {'title': 'Quantum Mechanics', 'text': 'Basic concepts of quantum mechanics.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 12,
             'cost': 0, 'course_id': 1},
            {'title': 'Relativity', 'text': 'Introduction to relativity theory.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 8,
             'cost': 0, 'course_id': 1},
            {'title': 'Optics', 'text': 'Basic principles of optics.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 18,
             'cost': 0, 'course_id': 1},
            {'title': 'Nuclear Physics', 'text': 'Introduction to nuclear physics.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 14,
             'cost': 0, 'course_id': 1},
            {'title': 'Astrophysics', 'text': 'Basic principles of astrophysics.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 16,
             'cost': 0, 'course_id': 1},
            {'title': 'Particle Physics', 'text': 'Introduction to particle physics.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 11,
             'cost': 0, 'course_id': 1},
            {'title': 'Fluid Dynamics', 'text': 'Basic principles of fluid dynamics.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 9,
             'cost': 0, 'course_id': 1}
        ])
        await session.execute(stmt)

        # Вставляем данные в таблицу topic для курса "Mathematics"
        stmt = insert(Topic).values([
            {'title': 'Algebra Basics', 'text': 'Introduction to algebraic concepts.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 10,
             'cost': 0, 'course_id': 2},
            {'title': 'Geometry Fundamentals', 'text': 'Basic principles of geometry.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 15,
             'cost': 0, 'course_id': 2},
            {'title': 'Trigonometry Essentials', 'text': 'Introduction to trigonometric functions.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 20,
             'cost': 0, 'course_id': 2},
            {'title': 'Calculus Fundamentals', 'text': 'Basic concepts of calculus.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 12,
             'cost': 0, 'course_id': 2},
            {'title': 'Linear Algebra', 'text': 'Study of linear equations and matrices.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 8,
             'cost': 0, 'course_id': 2},
            {'title': 'Probability Theory', 'text': 'Introduction to probability concepts.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 18,
             'cost': 0, 'course_id': 2},
            {'title': 'Statistics Basics', 'text': 'Basic principles of statistics.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 14,
             'cost': 0, 'course_id': 2},
            {'title': 'Differential Equations', 'text': 'Introduction to differential equations.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 16,
             'cost': 0, 'course_id': 2},
            {'title': 'Mathematical Logic', 'text': 'Study of mathematical logic principles.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 11,
             'cost': 0, 'course_id': 2},
            {'title': 'Number Theory', 'text': 'Introduction to number theory.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 9,
             'cost': 0, 'course_id': 2}
        ])
        await session.execute(stmt)

        # Вставляем данные в таблицу topic для курса "Python Programming"
        stmt = insert(Topic).values([
            {'title': 'Introduction to Python', 'text': 'Introduction to Python programming language.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 10,
             'cost': 0, 'course_id': 3},
            {'title': 'Python Basics', 'text': 'Basic concepts of Python programming language.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 15,
             'cost': 0, 'course_id': 3},
            {'title': 'Data Structures in Python', 'text': 'Learn about data structures in Python.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 20,
             'cost': 0, 'course_id': 3},
            {'title': 'Object-Oriented Programming in Python',
             'text': 'Understand object-oriented programming in Python.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 12,
             'cost': 0, 'course_id': 3},
            {'title': 'File Handling in Python', 'text': 'Learn to handle files in Python.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 8,
             'cost': 0, 'course_id': 3},
            {'title': 'Error Handling in Python', 'text': 'Learn about error handling in Python.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 18,
             'cost': 0, 'course_id': 3},
            {'title': 'Modules and Packages in Python', 'text': 'Understand modules and packages in Python.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 14,
             'cost': 0, 'course_id': 3},
            {'title': 'Advanced Python Topics', 'text': 'Explore advanced topics in Python programming.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 16,
             'cost': 0, 'course_id': 3},
            {'title': 'Python Projects', 'text': 'Work on Python projects to apply your skills.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 11,
             'cost': 0, 'course_id': 3},
            {'title': 'Python Libraries', 'text': 'Introduction to popular Python libraries.',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg', 'time_learn': 9,
             'cost': 0, 'course_id': 3}
        ])
        await session.execute(stmt)

        await session.commit()


async def insert_users():
    async with session_maker() as session:
        # Вставляем данные пользователей
        stmt = insert(User).values([
            {'firstname': 'John', 'lastname': 'Doe', 'role_in_company': 'Manager', 'email': 'john.doe@example.com',
             'password': 'hashed_password_1', 'is_active': True, 'balance': 1000, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'firstname': 'Alice', 'lastname': 'Smith', 'role_in_company': 'Developer',
             'email': 'alice.smith@example.com',
             'password': 'hashed_password_2', 'is_active': True, 'balance': 500, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'firstname': 'Bob', 'lastname': 'Johnson', 'role_in_company': 'Designer',
             'email': 'bob.johnson@example.com',
             'password': 'hashed_password_3', 'is_active': True, 'balance': 750, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'firstname': 'Emma', 'lastname': 'Brown', 'role_in_company': 'Marketing',
             'email': 'emma.brown@example.com',
             'password': 'hashed_password_4', 'is_active': True, 'balance': 300, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'firstname': 'Michael', 'lastname': 'Lee', 'role_in_company': 'Sales', 'email': 'michael.lee@example.com',
             'password': 'hashed_password_5', 'is_active': True, 'balance': 1200, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'firstname': 'Sophia', 'lastname': 'Garcia', 'role_in_company': 'HR', 'email': 'sophia.garcia@example.com',
             'password': 'hashed_password_6', 'is_active': True, 'balance': 800, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'firstname': 'William', 'lastname': 'Martinez', 'role_in_company': 'Analyst',
             'email': 'william.martinez@example.com',
             'password': 'hashed_password_7', 'is_active': True, 'balance': 950, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'firstname': 'Olivia', 'lastname': 'Lopez', 'role_in_company': 'Consultant',
             'email': 'olivia.lopez@example.com',
             'password': 'hashed_password_8', 'is_active': True, 'balance': 670, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'firstname': 'Ethan', 'lastname': 'Gonzalez', 'role_in_company': 'Engineer',
             'email': 'ethan.gonzalez@example.com',
             'password': 'hashed_password_9', 'is_active': True, 'balance': 1100, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'firstname': 'Ava', 'lastname': 'Rodriguez', 'role_in_company': 'Administrator',
             'email': 'ava.rodriguez@example.com',
             'password': 'hashed_password_10', 'is_active': True, 'balance': 400, 'date_created': datetime.now(),
             'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'}
        ])
        await session.execute(stmt)

        await session.commit()


async def insert_games():
    async with session_maker() as session:
        # Вставляем данные игр
        stmt = insert(Game).values([
            {'title': 'The Witcher 3: Wild Hunt',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'title': 'Red Dead Redemption 2',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'title': 'The Legend of Zelda: Breath of the Wild',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'title': 'God of War (2018)',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'title': 'Grand Theft Auto V',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'title': 'Dark Souls III',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'title': 'Persona 5',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'title': 'Bloodborne',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'title': 'Horizon Zero Dawn',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'},
            {'title': 'Mass Effect 2',
             'image_url': 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Flat_cross_icon.svg'}
        ])
        await session.execute(stmt)
        await session.commit()


async def delete_all_data():
    async with session_maker() as session:
        await session.execute(delete(User))

        await session.execute(delete(Topic))

        await session.execute(delete(Game))

        await session.execute(delete(Course))

        await session.commit()
