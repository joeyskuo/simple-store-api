FROM postgres:9.5-alpine
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_USER postgres
ENV POSTGRES_DB postgres
COPY create_db.sql /docker-entrypoint-initdb.d/
