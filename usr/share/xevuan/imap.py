#!/usr/bin/env python

import imaplib

IMAPSERVER = ''
USER = ''
PASSWORD = ''

try:
    mail = imaplib.IMAP4_SSL(IMAPSERVER)
    mail.login(USER, PASSWORD)
    mail.select('inbox')
    return_code, mail_ids = mail.search(None, 'UNSEEN')
    count = len(mail_ids[0].split())
except:
    count = 0

print count
