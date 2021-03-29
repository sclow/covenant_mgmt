#!/usr/bin/python3

import sys
import argparse
from pprint import pprint
import os
import os.path
from os import path
import time
import datetime
import shutil
import subprocess
import sqlite3
import enquiries
from base64 import b64encode
import re

config = {
  "database": "/opt/Covenant/Covenant/Data/covenant.db",
  "systemd_name": "covenant",
  "systemd": False,
  "moron": False,
  "truncate": str(b64encode('TRUNCATED'.encode('UTF-16LE')), sys.stdout.encoding)
}

def check_root_user():
    if not os.geteuid() == 0:
        print("This script needs to be run as root / sudo.")
        exit()


def backup_database():
    timestamp = time.time()
    backup_date = datetime.datetime.fromtimestamp(timestamp).strftime("%Y%m%d%H%M%S")
    backup_filename = config["database"]  + "." + backup_date
    print("Attempting to backup: " + config["database"] + " with datestamp: " + backup_date)
    print("Backup filename: " + backup_filename)
    try:
        shutil.copy(config["database"], backup_filename)
        print("Backup Successful.")
    except err:
        print("ERROR: ", err)

    print()

def systemd_stop():
    print("Attempting to stop systemd unit: " + config["systemd_name"])
    try:
        cmd='/bin/systemctl stop {}.service'.format(config["systemd_name"])
        print("Attempting to run: " + cmd)
        runcommand = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE)
    except subprocess.CalledProcessError as err:
        print("ERROR: ", err)
 
            

def systemd_start():
    print("Attempting to start systemd unit: " + config["systemd_name"])

def manage_database():
    if config["systemd"]:
        systemd_stop()
    
    if not config["moron"]:
        backup_database()

    # Time to play with the DB
    connection = sqlite3.connect(config["database"])
    cursor = connection.cursor()
    
    # The risky part!
    fix_bad_things_menu(cursor)

    # Save our changes
    connection.commit()

    print()
    print("Total Changes made: " + str(connection.total_changes))

    if config["systemd"]:   
        systemd_start()

def fix_base64_decode_error(cursor):
    print("Fix Base64 Decode Error due to failed downloads")
    print()
    
    rows = cursor.execute("SELECT ID, Discriminator, FileName, length(FileContents) FROM Events WHERE Discriminator='DownloadEvent' AND FileContents like 'System.UnauthorizedAccessException%' ").fetchall()
    if len(rows):
        print("ID: Discriminator: FileName: Character Lengh of FileContents")
        options=[]

        terminal_rows, terminal_columns = os.popen('stty size', 'r').read().split()
        for row in rows:
            row_filename=f"{str(row[2])}"
            max_filename_length = (50 * int(terminal_columns)) // 100
            if len(row_filename) < max_filename_length:
                string_row = f"{str(row[0])}: {str(row[1])}: {row_filename}: ({str(row[3])}) Chars"
            else:
                shortened_filename="..." + row_filename[-max_filename_length:]
                string_row = f"{str(row[0])}: {str(row[1])}: {shortened_filename}: ({str(row[3])}) Chars" 

            options.append(string_row)

        choices = enquiries.choose("Select a record to truncate...", options, multi=True)

        for choice in choices:
            truncation_record = re.split(r':\s', choice)
            if enquiries.confirm('Do you want to resolve {} ({})?'.format(str(truncation_record[0]),str(truncation_record[2]))):  
                print("Attempt to fix record: " + str(truncation_record[0]) )
                update_downloads_in_events_table(cursor, truncation_record[0])
    else:
        print("Could not find any matching records showing evidence of stack trace where BASE64 should be.")

    print("")
    fix_bad_things_menu(cursor)

def fix_stack_trace_in_events(cursor):
    # This is different from Base64 as we can "null" string 
    print("Random Stacktrace")
    print("------------------------------------------")
    print("")
    print("This error is hard to track down.")
    print("If you get a stack trace that doesnt resolve when stopping/restarting Covenant.")
    print("Please can you dump your Events / CommandOutputs tables.")
    print("Ideally it would be great for you to share, but otherwise it would be great to understand where the error is.")
    print("------------------------------------------")

    fix_bad_things_menu(cursor)

def truncate_downloaded_files_events_table(cursor):
    print("Which Downloaded file do you wish to truncate?")
    print("")

    rows = cursor.execute("SELECT ID, Discriminator, FileName, length(FileContents) FROM Events WHERE Discriminator='DownloadEvent' ").fetchall()
    if len(rows):
        print("ID: Discriminator: FileName: Character Lengh of FileContents")
        options=[]

        terminal_rows, terminal_columns = os.popen('stty size', 'r').read().split()
        for row in rows:
            row_filename=f"{str(row[2])}"
            max_filename_length = (50 * int(terminal_columns)) // 100
            if len(row_filename) < max_filename_length:
                string_row = f"{str(row[0])}: {str(row[1])}: {row_filename}: ({str(row[3])}) Chars"
            else:
                shortened_filename="..." + row_filename[-max_filename_length:]
                string_row = f"{str(row[0])}: {str(row[1])}: {shortened_filename}: ({str(row[3])}) Chars" 

            options.append(string_row)

        choices = enquiries.choose("Select a record to truncate...", options, multi=True)

        for choice in choices:
            truncation_record = re.split(r':\s', choice)
            if enquiries.confirm('Do you want to truncate {} ({})?'.format(str(truncation_record[0]),str(truncation_record[2]))):  
                print("Truncated record: " + str(truncation_record[0]) )
                update_downloads_in_events_table(cursor, truncation_record[0])

    else:
        print("Currently no downloads in the database.")
        print("")
    
    fix_bad_things_menu(cursor)

def truncate_downloaded_files_commandoutputs_table(cursor):
    print("Which Downloaded file do you wish to truncate?")
    print("")

    sql = ''' SELECT CommandOutputs.Id, GruntTaskings.Parameters , length(CommandOutputs.Output) FROM CommandOutputs 
                INNER JOIN GruntCommands ON GruntCommands.CommandOutputId = CommandOutputs.Id 
                INNER JOIN GruntTaskings ON GruntTaskings.GruntCommandId = GruntCommands.Id 
                INNER JOIN GruntTasks ON GruntTaskings.GruntTaskId = GruntTasks.Id 
                WHERE GruntTasks.Name = 'Download'
              '''
    rows = cursor.execute(sql).fetchall()
    if len(rows):
        print("ID: Discriminator: FileName: Character Lengh of FileContents")
        options=[]

        terminal_rows, terminal_columns = os.popen('stty size', 'r').read().split()
        for row in rows:
            row_filename=f"{str(row[1])}"
            max_filename_length = (50 * int(terminal_columns)) // 100
            if len(row_filename) < max_filename_length:
                string_row = f"{str(row[0])}: {row_filename}: ({str(row[2])}) Chars"
            else:
                shortened_filename="..." + row_filename[-max_filename_length:]
                string_row = f"{str(row[0])}: {shortened_filename}: ({str(row[2])}) Chars" 

            options.append(string_row)

        choices = enquiries.choose("Select a record to truncate...", options, multi=True)

        for choice in choices:
            truncation_record = re.split(r':\s', choice)
            if enquiries.confirm('Do you want to truncate {} ({})?'.format(str(truncation_record[0]),str(truncation_record[1]))):  
                print("Truncated record: " + str(truncation_record[0]) )
                update_downloads_in_commandoutputs_table(cursor, truncation_record[0])

    else:
        print("Currently no downloads in the database.")
        print("")
    
    fix_bad_things_menu(cursor)


def fix_bad_things_menu(cursor):
    # Don't change the order of these without remapping the if statements
    options=[
        "Fix BASE64 decode error",
        "Fix Stack trace in event error",
        "Truncate downloaded files in Events table",
        "Truncate downloaded files in CommandOutputs table",
        "Exit, save and quit"
    ]

    response = enquiries.choose("How do you want to manage the Covenant database?", options)
    if response == options[0]:
        fix_base64_decode_error(cursor)
    elif response == options[1]:
        fix_stack_trace_in_events(cursor)
    elif response == options[2]:
        truncate_downloaded_files_events_table(cursor)
    elif response == options[3]:
        truncate_downloaded_files_commandoutputs_table(cursor)
    elif response == options[4]:
        print("Exiting....")

def update_downloads_in_events_table(cursor, id):
    sql = ''' UPDATE Events
              SET FileContents = ? 
              WHERE id = ?'''
    cursor.execute(sql, (str(config["truncate"]), id))    

def update_downloads_in_commandoutputs_table(cursor, id):
    sql = ''' UPDATE CommandOutputs
              SET Output = ? 
              WHERE id = ?'''
    cursor.execute(sql, (str(config["truncate"]), id))    
    
def main(argv):
    # Needs to run as root to start / stop services and access the root owned covenant.db
    check_root_user()

    parser = argparse.ArgumentParser(description='Covenant Database Management.')
    parser.add_argument("-d", "--database", help="Database to Manage (" + str(config["database"]) + ")")
    parser.add_argument("-s", "--systemd", help="Use systemd to stop/start Covenant instance and set the name of the unit: (" + str(config["systemd_name"]) + ")", nargs='?', action='store', default=False)
    parser.add_argument("-m", "--moron", help="Enables 'Moron Mode' no DB backups will be made.", action="count", default=0)
    
    args = parser.parse_args()

    if args.database:
        config["database"] = args.database
        if not path.isfile(config["database"]):
            print("Could not find Covenant database file: " + config["database"])
            exit()
    
    if args.systemd:
        config["systemd"] = True
        config["systemd_name"] = args.systemd
    elif args.systemd == None:
        config["systemd"] = True
    
    if args.moron:
        config["moron"] = True
        print("**********************WARNING!!!**********************")
        print("\tMoron mode active...")
        print("\tNo database backups will be made...")
        print("\tBest of luck, you may need it!")
        print("**********************WARNING!!!**********************")
        print("")
    
    manage_database()  
    #pprint(config)  
   
if __name__ == "__main__":
   main(sys.argv[1:])

