ARG PYTHON_BASE=3.10-slim
# BUILD stage
FROM python:$PYTHON_BASE AS builder

# install PDM
RUN pip install -U pdm
# disable update check
ENV PDM_CHECK_UPDATE=false
# copy files
COPY pyproject.toml pdm.lock README.md /app/
COPY cancer_estimator_application/ /app/cancer_estimator_application

# install dependencies and app into the local packages directory
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache pdm install --check --prod --no-editable

### RUN stage
FROM python:$PYTHON_BASE

# retrieve packages from build stage
COPY --from=builder /app/.venv/ /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
# set command/entrypoint, adapt to fit your needs
COPY cancer_estimator_application /app/cancer_estimator_application
COPY templates /app/templates
EXPOSE 8000
CMD ["fastapi", "run", "cancer_estimator_application/main.py"]
