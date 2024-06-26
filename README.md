![test](https://github.com/cancer-estimator/application/actions/workflows/test.yml/badge.svg?branch=main)
![deploy](https://github.com/cancer-estimator/application/actions/workflows/deploy.yml/badge.svg?branch=main)

# Cancer Estimator Application

This application implements the following document designs of an
Electronic Health Record System to help estimate the risk of patients
having lung cancer. [Presentation]

[Presentation]: https://docs.google.com/presentation/d/e/2PACX-1vT9qdlz5h49znwlLyCpQco9YnZ6oemkGKMMz6vmC8yDJU_jz5ahVmtpEuk47WxGew/pub?start=false&loop=false&delayms=60000#slide=id.p1
# Technologies

- [FastAPI] is a library used to create the HTTP server.
- [HTMX] is used to handle front-end capabilities at the server-side.
- [SQLAlchemy] is used to manage SQL data persistence and query capabilities through ORM[^1].

[FastAPI]: https://fastapi.tiangolo.com/
[HTMX]: https://htmx.org/
[SQLAlchemy]: https://www.sqlalchemy.org/
[^1]: We use SQLite for simplicity, but PostgreSQL can be used in production.

# How to Run

Please ensure you have a Unix-like environment with [Python] and [Make] installed.

Use the following command to install the necessary libraries in a
python virtual environment managed by [pdm]:

```shell
make install
```

You will need to sync model files (trained) from remote repository too, so:

```
pdm run dvc pull
```

Use this command to run:

```shell
make run-local
```

If you have [Docker] installed and encounter problems running the
system with the above commands, you can use this:

```shell
make run
```

How to run tests:

```
make check
```

[Python]: https://www.python.org/
[Make]: https://www.gnu.org/software/make/manual/make.html
[Docker]: https://www.docker.com/
[pdm]: https://pdm-project.org/

# Deployment

## CI/CD

The software is automatically deployed as a Docker container via
GitHub Actions on the main branch, contingent upon the successful
completion of automated tests. The application is self-hosted on an
on-premises server located in Pará, Brazil, and is accessible through
the domain https://cancer.manoel.dev, utilizing Cloudflare Tunnels for
internet exposure.

## Manual deployment

If you have the proper cloudflare credentials exported as environment variables:

- `CF_ACCESS_CLIENT_ID`
- `CF_ACCESS_CLIENT_SECRET`

And you have write access to the docker hub repository
[ryukinix/cancer-estimator-application] you can deploy the application with:

```
make deploy
```

[ryukinix/cancer-estimator-application]: https://hub.docker.com/r/ryukinix/cancer-estimator-application

# Design

## Login Page

![](docs/wireframe/login.png)

## Search Patient Page

![](docs/wireframe/main.png)

## Add/Update Patient Page

![](docs/wireframe/add_or_edit_user.png)
