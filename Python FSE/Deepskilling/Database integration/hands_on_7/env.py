# A generic, single database configuration.

[alembic]
script_location = migrations

prepend_sys_path = .

sqlalchemy.url = postgresql://postgres:password@localhost:234j2/college_db_orm
