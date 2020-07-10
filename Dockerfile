  
FROM mysql

COPY CreateTable.sql ./docker-entrypoint-initdb.d
