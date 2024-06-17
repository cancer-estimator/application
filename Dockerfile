ARG PYTHON_BASE=3.10-slim
# BUILD stage
FROM python:$PYTHON_BASE AS builder

# install PDM
RUN pip install -U pdm
RUN apt-get update \
     && apt-get install -y --no-install-recommends git \
     && apt-get purge -y --auto-remove \
     && rm -rf /var/lib/apt/lists/*

# disable update check
ENV PDM_CHECK_UPDATE=false
# copy files
COPY pyproject.toml pdm.lock README.md /app/
COPY cancer_estimator_application/ /app/cancer_estimator_application
# install dependencies and app into the local packages directory
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache pdm install --check --prod --no-editable

FROM builder as test
RUN chmod 777 /app
COPY templates /app/templates
COPY static /app/static
COPY tests /app/tests
COPY models /app/models
RUN --mount=type=cache,target=/root/.cache pdm install --dev
ENTRYPOINT ["pdm"]

### PROD stage
FROM python:$PYTHON_BASE as prod

# retrieve packages from build stage
WORKDIR /app
COPY --from=builder /app/.venv/ /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
# set command/entrypoint, adapt to fit your needs
COPY cancer_estimator_application /app/cancer_estimator_application
COPY templates /app/templates
COPY static /app/static
COPY scripts /app/scripts
COPY models /app/models
RUN bash /app/scripts/bump_static.sh
EXPOSE 8000
CMD ["fastapi", "run", "/app/cancer_estimator_application/main.py"]
