#!/bin/bash

set -e

WEBHOOK=https://docker.manoel.dev/api/webhooks/64005ef6-09c0-43c8-ab41-ab61d1695bd3

err () {
    >&2 echo $@
    exit 1
}

check-auth () {
    if [[ -z "${CF_ACCESS_CLIENT_ID}" || -z "${CF_ACCESS_CLIENT_SECRET}" ]]; then
        err "error: credentials CF_ACCESS_CLIENT_ID and CF_ACCESS_CLIENT_SECRET are required to deploy."
    fi
}

deploy-by-webhook () {
    curl -L -X POST \
         -H "CF-Access-Client-Id: ${CF_ACCESS_CLIENT_ID}" \
         -H "CF-Access-Client-Secret: ${CF_ACCESS_CLIENT_SECRET}" \
         ${WEBHOOK}
    echo "Deployed to the server cancer.manoel.dev"
}

check-auth
deploy-by-webhook
