#!/bin/bash

OPENSSL=`which openssl`

if [ -z "${OPENSSL}" ] ; then
    echo "Could not find openssl"
    exit
fi

CERTDIR=`dirname $0`
COV_KEY="${CERTDIR}/covenant.key"
COV_CERT="${CERTDIR}/covenant.crt"
COV_PEM="${CERTDIR}/covenant.pem"
COV_PFX="${CERTDIR}/covenant.pfx"
COV_PASS="${CERTDIR}/covenant.pass"

function show_covenant_config {
    echo "Use the following configuration to access this certificate:"
    echo ""
    PASSPHRASE=`cat ${COV_PASS}`
    PEM=`cat  ${COV_PFX} | base64 -w 0`
    HASH=`openssl x509 -in ${COV_CRT} -fingerprint | grep SHA | cut -f2 -d "=" | tr -d ":"`

    echo -e "\t\tsslCertificate: \"${PEM}\""
    echo -e "\t\tsslCertificatePassword: \"${PASSPHRASE}\""
    echo -e "\t\tsslCertHash: \"${HASH}\""
    exit
}

function generate_passphrase {
    # Generate 8 character alpha-num passphrase
    cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1 > ${COV_PASS}

}

function create_self_signed_cert {
    PASSPHRASE=`cat ${COV_PASS}`
    # COUNTRY="US"
    # STATE="Oregon"
    # LOCATION="Portland"
    # ORG_NAME="Company Name"
    # ORG_UNIT="Org"
    # CN="kali"
    COUNTRY=""
    STATE=""
    LOCATION=""
    ORG_NAME=""
    ORG_UNIT=""
    CN="kali"

    openssl req -x509 -newkey rsa:4096 -keyout ${COV_KEY} -out ${COV_CERT} -days 365 -sha256 -nodes -subj "/C=${COUNTRY}/ST=${STATE}/L=${LOCATION}/O=${ORG_NAME}/OU=${ORG_UNIT}/CN=${CN}"

    cat ${COV_KEY} ${COV_CERT} > ${COV_PEM}
    openssl pkcs12 -export -out ${COV_PFX} -inkey ${COV_KEY} -in ${COV_CERT} -passout "pass:${PASSPHRASE}"
}

function make_covenant_cert {
    generate_passphrase;
    create_self_signed_cert;
    show_covenant_config;
}

if [[ -f "${COV_PFX}" ]] || [[ -f "${COV_PASS}" ]] ;  then
    echo "Files already exist.."
    show_covenant_config;
else
    echo "No files detected, will build you a certificate!"
    make_covenant_cert;
fi
