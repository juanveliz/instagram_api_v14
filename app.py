##
#   Author:    Juan Jesus Veliz Godoy
#   Created:   06.08.2021
#   Software bajo licencia GPLv3.
#   API Graph de Instagram version: v14.0. ref: https://developers.facebook.com/docs/instagram-basic-display-api/changelog
#   Notion version : 2022-06-28. ref: https://developers.notion.com/reference/versioning
#   Google Sheets API : ref:https://developers.google.com/sheets/api/quickstart/python
#
#   This python application allows to automate Instagram posting using the official API.
# 

import src.funtions as fn

def main():
    #Publish a new instagram post - Max post per day is 25!-
    #sp.publish_container()
    fn.publish_container()


if __name__ == '__main__':
    print('Iniciando proceso espere un momento ...')
    main()
