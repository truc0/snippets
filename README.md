# Snippets

A pastebin app powered by [Django](https://djangoproject.org) and [Pygments](https://pygments.org).

## Deploy

Before deploying the app, you need to configure it first.
The configuration file is located in `pastebin/config.py`, you may have a look at 
`pastebin/config.example.py` as an reference.

The app use `postgresql` as the default database. You can only config `POSTGRESQL_NAME`
and other similar configuration part in `pastebin/config.py` instead of writing the 
whole DATABASES object manully.

### Docker

If you are using `postgresql` as your database, you can config your POSTGRESQL in
docker configuration file (see `docker-compose.yml`).

Check `docker-compose.yml` file and do some necessary change before you bring them up.

Then execute the following command to build and run the application.

```bash
docker-compose build
docker-compose up -d
```

The app is binding 28000 port by default.

### Deplay manually

This part is lack of documentation but it is the same as other `Django` app app.

Check [Django documentation](https://docs.djangoproject.com/en/4.0/howto/deployment/) for more information.

## About

This project is designed for personal usage, thus it contains some personal info and 
it is lack of documentation.

Any contribution to this project is welcome, just create a PR if you are interesting in this project.
If you are adding new features, it is suggested that opening an issue to describing your plan first.

