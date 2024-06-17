#!/bin/bash

set -e

WEBHOOK=https://docker.manoel.dev/api/webhooks/639c74db-f5ea-4d7d-b4ea-5e27f2e5cd71

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
    curl -f -L -X POST \
         -H "CF-Access-Client-Id: ${CF_ACCESS_CLIENT_ID}" \
         -H "CF-Access-Client-Secret: ${CF_ACCESS_CLIENT_SECRET}" \
         ${WEBHOOK}
    echo "Deployed to the server cancer.manoel.dev"
}

check-auth
deploy-by-webhook
