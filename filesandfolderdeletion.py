import os
import shutil
import schedule

# path to the directory to be deleted
path = '/Users/anubhav/.Trash/'


def empty_trash():
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        try:
            if os.path.isfile(filepath) or os.path.islink(filepath):
                os.unlink(filepath)
            elif os.path.isdir(filepath):
                shutil.rmtree(filepath)
        except Exception as exception:
            print('Failed to delete at %s. Reason: %s' % (filepath, exception))
            
            
# you can schdule it according to your need, I am setting it to once a week on sunday's
schedule.every().sunday.at("00:00").do(empty_trash())

while True:
    schedule.run_pending()
