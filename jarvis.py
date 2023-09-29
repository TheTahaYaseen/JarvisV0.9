# Kivy Imports
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.metrics import dp

from kivy.uix.label import Label

# Module Imports
import pyttsx3
import speech_recognition

import datetime
import time

import random
 
from threading import Thread

import json

import requests
from bs4 import BeautifulSoup

import pandas

from quote import quote
from random_word import RandomWords

from pywhatkit import playonyt

import webbrowser

import random

from browser_history.browsers import Brave
import webbrowser

site_extensions = [".com", ".org", ".net", ".edu", ".gov", ".mil", ".int", ".co", ".io", ".biz", ".info", ".me", ".tv", ".online", ".store", ".blog", ".news", ".shop", ".app", ".club"]

def fetch_visited_sites():
  browser = Brave()
  output_fetched = browser.fetch_history()

  history_found = output_fetched.histories
  urls_found = [history_record[1] for history_record in history_found]
  return urls_found

def open_rootsite(website_to_open):
  known_sites = fetch_visited_sites()
  if "google" in website_to_open:
    webbrowser.open("google.com")
  else:
    for known_site in known_sites:
      website_to_open_split = website_to_open.split()
      iteration = 0
      for word in website_to_open_split:
        if word in known_site and "google" not in known_site:
          iteration = iteration + 1
      if iteration == len(website_to_open_split):
        webbrowser.open(known_site)
        break


def open_site(website_to_open):
  known_sites = fetch_visited_sites()
  if "google" in website_to_open:
    webbrowser.open("google.com")
  else:
    site_opening = 0
    for known_site in known_sites:
      website_to_open_split = website_to_open.split()
      iteration = 0
      for word in website_to_open_split:
        if word in known_site and "google" not in known_site:
          iteration = iteration + 1
      if iteration == len(website_to_open_split):
        for site_extension in site_extensions:
          if site_extension in known_site:
            site_opening = known_site.split(site_extension)[0] + site_extension
            webbrowser.open(site_opening)
            break
      if site_opening:
        break

# Global Variables 

rock_paper_scissor_options = ["paper", "rock", "scissor"]
rock_paper_scissor_going_on = False
rock_paper_scissors_my_choice = ""

numbers_game_going_on = False
numbers_game_my_choice = 0

# Maths Related

def round_to_nearest_base(num, base=5):
    return int(base * round(num/base))

# Datetime Related

def get_datetime():

    current_datetime = datetime.datetime.now()

    date = f"{current_datetime.strftime('%A')}, {current_datetime.strftime('%d')} {current_datetime.strftime('%B')} {current_datetime.strftime('%Y')}"
    time = f"{current_datetime.strftime('%H')}:{current_datetime.strftime('%M')}:{current_datetime.strftime('%S')}"

    return [date, time]

"""

# Routine For File Management
  > Scheduled Every Week
  > Create A Folder For Each Category

    # Go Through Each File In Each Folder    
    # Identify The Type Of File By Extension

    # Move The File To Its Category Folder

"""

import os
import shutil

file_extensions = {
    'Documents': ['doc', 'docx', 'pdf', 'csv', 'xml', 'txt', 'md', 'xls', 'xlsx', 'sln', 'suo'],
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'svg', 'bmp', 'tiff', 'webp', 'jfif', 'ico', 'JPG'],
    'Audio-Video': ['mp3', 'mp4', 'm4a'],
    'Code': ['py', 'java', 'cpp', 'c', 'cs', 'js', 'html', 'css', 'php', 'pl', 'ini', 'cfg', 'rst', 'ipynb', 'cmake', 'sh', 'ahk', 'sb3', 'f90', 'S', 'h'],
    'Archives-Compressed files': ['zip', 'gz', 'rar', 'tar', '7z', 'pkg', 'whl'],
    'Executables': ['exe', 'msi', 'dll', 'bin'],
    'Fonts': ['ttf', 'otf', 'woff', 'woff2'],
    'Configuration files': ['config', 'htaccess', 'manifest', 'editorconfig', 'props', 'stylelintignore', 'gitattributes', 'yaml'],
    'Databases': ['db', 'sql'],
    'Other': ['1', 'F', 'sample', 'map', 'lnk', 'url', 'pickle', 'enc', 'pdb', 'lock', 'klc', 'vcf', 'rdp', 'vsidx', 'reg', 'klm2000', 'pyz', 'la', 'yml', 'eot', 'npy', 'for', 'msl', 'scss', 'pkl', 'toc', 'pyd', 'pc', 'csproj', 'PNG', 'json', 'psd', 'mvg', 'spec', 'BuildWithSkipAnalyzers', 'v2', 'dj', 'cu', 'targets', 'xltx', 'htm', 'kv', 'URL', 'cshtml', 'CopyComplete', 'user', 'h5', 'a', 'gitignore', 'pnm', 'cache', 'crt', 'fig', 'f', 'pyc', 'in', 'pyw', 'check_cache']
}

root_directory = "C:/Users/T&C"
root_sorted = "C:/Users/T&C/Desktop/Sorted"

directories_to_go_through = ["3D Objects", "Desktop", "Documents", "Downloads", "Music", "Pictures", "Videos"]
directories_to_go_through = [f"{root_directory}/{directory}/" for directory in directories_to_go_through]

files = []

def get_path_of_all_files_present():

  while True:

    if directories_to_go_through:

      for directory in directories_to_go_through:

        try:
          files_and_folders_in_directory = os.listdir(directory)

          for file_or_folder in files_and_folders_in_directory:

              file_or_folder_path = f"{directory}{file_or_folder}"
              
              if os.path.isdir(file_or_folder_path):
                  directories_to_go_through.append(f"{file_or_folder_path}/")
              else:
                  files.append(file_or_folder_path)

        except WindowsError: 
          pass
        
        del directories_to_go_through[directories_to_go_through.index(directory)]

    else:
      return files  

def for_measure_get_extensions_of_all_files():
   
  files = get_path_of_all_files_present()

  file_extensions = []  

  for file in files:
    extension = file.rsplit(".", 1)
    try:
      if "/" not in extension[1]: 
        file_extensions.append(extension[1])
      else:
        del files[files.index(file)]
    except IndexError:
      del files[files.index(file)]

  file_extensions = set(file_extensions)
  return files
  
def check_if_all_extensions_are_in_sorted():

  extensions = for_measure_get_extensions_of_all_files()[1]

  file_extension_keys = list(file_extensions.keys())
  for extension in extensions:
    for file_extension_key in file_extension_keys:
      extensions_found = file_extensions[file_extension_key]
      if extension in extensions_found:
        break
    else:
      print(f'Extension "{extension}" not found in sorted dictionary...')

def sort_files_by_category():
  
  files = for_measure_get_extensions_of_all_files()
  sorted_folders = list(file_extensions.keys())

  for file in files:
    
    extension = file.rsplit(".", 1)[1]

    for sorted_folder in sorted_folders:
      extensions_to_go_in_folder = file_extensions[sorted_folder]
      if extension in extensions_to_go_in_folder:
        new_file_path = file.replace("C:/Users/T&C/", "")
        new_file_path = new_file_path.replace("/", "-")
        path_of_folder_to_go_in = f"{root_sorted}/{sorted_folder}/{new_file_path}"
        shutil.copy(file, path_of_folder_to_go_in)
        print(f"Copied {file} to {path_of_folder_to_go_in}")

# sorted_folders = list(file_extensions.keys())
# for x in sorted_folders:
#   os.system(f'mkdir "{root_sorted}/{x}/"')

sort_files_by_category_thread = Thread(target=sort_files_by_category)
    

# Related To Speaking

hold_thing_to_be_said, skip_thing_to_be_said, repeat_thing_to_be_said, slow_down_talking_speed, clear_things_to_be_said = False, False, False, False, False

witty_dialogues_csv = pandas.read_csv("main_data.csv")
witty_dialogues = witty_dialogues_csv["line"]

things_to_be_said = ["At Your Service Sir!", "How May I Help You?"] 
things_said = []

saying_engine = pyttsx3.init("sapi5")
voices = saying_engine.getProperty("voices")
saying_engine.setProperty("voice", voices[0].id)

saying_engine.setProperty("rate", 200)

def say(thing_to_say):
    saying_engine.say(thing_to_say)
    saying_engine.runAndWait()

def saying_things_back_to_back():
    
    global things_to_be_said, witty_reply, aura_source, skip_thing_to_be_said, slow_down_talking_speed, hold_thing_to_be_said, repeat_thing_to_be_said

    while True:
        if things_to_be_said:
            for thing_to_say in things_to_be_said:
                
                while True:

                    if slow_down_talking_speed:
                        saying_engine.setProperty("rate", "175")
                    else:
                        saying_engine.setProperty("rate", "200")

                    if hold_thing_to_be_said:
                        time.sleep(1)
                    
                    elif skip_thing_to_be_said:
                        skip_thing_to_be_said = False
                        break
                    
                    else:
                        aura_source = "Content\Jarvis Aura.gif"
                        witty_reply = str(thing_to_say) 
                        say(thing_to_say)  
                        break
                            
                    if repeat_thing_to_be_said:
                        aura_source = "Content\Jarvis Aura.gif"
                        witty_reply = str(thing_to_say) 
                        say(thing_to_say)  
                        repeat_thing_to_be_said = False

                del things_to_be_said[things_to_be_said.index(thing_to_say)]
                things_said.append(thing_to_say)
                aura_source = "Content\Jarvis Aura.png"
    
saying_thread = Thread(target=saying_things_back_to_back)

def get_random_joke():
    header = {  
        "Accept":"application/json"
    }
    response = requests.get("https://icanhazdadjoke.com/", headers=header).json()
    joke = response['joke']
    return joke

def get_random_advice():
    response = requests.get("https://api.adviceslip.com/advice").json()
    advice = response['slip']['advice']
    return advice

def get_random_quote():
    while True:
        random_words = RandomWords()
        topic = random_words.get_random_word()
        resulting_quotes = quote(topic)
        for i in range(len(resulting_quotes)):
            quota = resulting_quotes[i]
            quota = quota["quote"]
            if len(quota) < 100:
                return quote 
                break       

def get_movie_dialogue():
        
    movie_line = None

    while movie_line != None:

        # Get Movie Dialogue
        movie_dialogue = random.choice(witty_dialogues)

        square_bracket_count = movie_dialogue.count("[")

        for i in range(square_bracket_count):
            
            opening_square_bracket_in_movie_dialogue = movie_dialogue.find("[")
            closing_square_bracket_in_movie_dialogue = movie_dialogue.find("]", opening_square_bracket_in_movie_dialogue)
            
            square_bracket_content = movie_dialogue[opening_square_bracket_in_movie_dialogue:closing_square_bracket_in_movie_dialogue+1]
            movie_dialogue = movie_dialogue.replace(square_bracket_content, "")

        round_bracket_count = movie_dialogue.count("(")

        for i in range(round_bracket_count):
            
            opening_round_bracket_in_movie_dialogue = movie_dialogue.find("(")
            closing_round_bracket_in_movie_dialogue = movie_dialogue.find(")", opening_round_bracket_in_movie_dialogue)
            
            round_bracket_content = movie_dialogue[opening_round_bracket_in_movie_dialogue:closing_round_bracket_in_movie_dialogue+1]
            movie_dialogue = movie_dialogue.replace(round_bracket_content, "")

        angle_bracket_count = movie_dialogue.count("<")

        for i in range(angle_bracket_count):
            
            opening_angle_bracket_in_movie_dialogue = movie_dialogue.find("<")
            closing_angle_bracket_in_movie_dialogue = movie_dialogue.find(">", opening_angle_bracket_in_movie_dialogue)
            
            angle_bracket_content = movie_dialogue[opening_angle_bracket_in_movie_dialogue:closing_angle_bracket_in_movie_dialogue+1]
            movie_dialogue = movie_dialogue.replace(angle_bracket_content, "")

        movie_lines = movie_dialogue.split(".")
        movie_line = random.choice(movie_lines)

    return movie_line

def get_witty_reply():
    
    wit_source_int = random.randint(0, 10)

    if wit_source_int < 7:
        wit = get_movie_dialogue()

    elif wit_source_int < 9:
        # Get Joke
        wit = get_random_joke()

    elif wit_source_int < 10:
        # Get Advice
        wit = get_random_advice()

    elif wit_source_int < 11:
        # Get Advice
        wit = get_random_quote()

    return wit

# Related To Listening

def listen():

    try:
        global listening_status
        
        audio_recognizer = speech_recognition.Recognizer()
        
        with speech_recognition.Microphone() as source:
            listening_status = "Listening...."
            audio_recognizer.pause_threshold = 1
            audio = audio_recognizer.listen(source)
        
        try:
            listening_status = "Recognizing...."
            command = audio_recognizer.recognize_google(audio)
            commands_given.append(command)
        
        except Exception as error:
            print(error)
            listening_status = "Not Able To Recognize"
            return None
    
    except OSError:
        listening_status = "Proper Microphone Not Found"


def always_listening():

    global listening_status

    listening_status = ""

    while True:
        listen()

listening_thread = Thread(target=always_listening)

# Related To Command Processing

commands_given = []

def processing_commands_back_to_back():
    
    global rock_paper_scissor_going_on, rock_paper_scissor_options, rock_paper_scissors_my_choice, commands_given, things_to_be_said, skip_thing_to_be_said, slow_down_talking_speed, hold_thing_to_be_said, repeat_thing_to_be_said

    while True:
        
        if commands_given:
            
            for command in commands_given:
            
                try:

                    if rock_paper_scissor_going_on:
                        
                        for option in rock_paper_scissor_options:
                            if option in command:
                                rock_paper_scissors_my_choice = option
                        else:
                            wit = "Please Choose A Valid Option! Rock, Paper Or Scissor"

                    elif numbers_game_going_on:
                        
                        command_split = command.split(" ")
                        
                        for x in command_split:
                            try:
                                numbers_game_my_choice = int(x)

                            except TypeError:
                                pass

                            if not numbers_game_my_choice:
                                wit = "Please Choose A Valid Integer!"

                    elif "rock paper scissor" in command:

                        rock_paper_scissor_thread = Thread(target=rock_paper_scissor)
                        rock_paper_scissor_thread.start()

                        wit = "Starting Game!"

                    elif "numbers game" in command:
                        numbers_game_thread = Thread(target=numbers_game)
                        numbers_game_thread.start()
                        
                        wit = "Starting Game!"

                    elif "news" in command:
                        wit = "Narrating Today's News! Please Wait A Bit!"
                        news_thread = Thread(target=displaying_and_saying_news)
                        news_thread.start()

                    elif "scheduling day" in command:
                        if "for " in command:
                            scheduling_day = command.split("for ")
                            
                            with open("schedules.json", "r") as schedules_file:
                                schedule_json_record = json.load(schedules_file)
                            
                            schedule_json_record["scheduling day"] = scheduling_day

                            with open("schedules.json", "w") as schedules_file:
                                json.dump(schedule_json_record, schedules_file)
                        else:
                            wit = "Sir! Could You Please Define The Day Clearly Using 'For '"
                        
                    elif "add task " in command:

                        template_command = command.split("add task ")[1]

                        task, task_details, task_duration, task_time = "", "", "", ""

                        if template_command:
                            if ";" in template_command:
                                template_command = template_command.split(";")
                                task = template_command[0]
                                template_command = template_command[1]
                                if "for " in template_command: 
                                    template_command = template_command.split("for ")
                                    task_details = template_command[0]
                                    template_command = template_command[1]
                                    if "at " in template_command: 
                                        template_command = template_command.split("at ")
                                        task_duration = template_command[0]
                                        task_time = template_command[1]
                                        
                                        Thread(target=add_task_in_schedule, args=(task, task_details, task_time, task_duration))
                                        wit = "Task Added To Schedule Sir!"
                                    else:
                                        task_duration = template_command[1]
                                        wit = "Sir! Please Specify The Task Time"                                
                                else:
                                    task_details = template_command[1]
                                    wit = "Sir! Please Specify The Task Duration And Time"
                            else:
                                task = template_command
                                wit = "Sir! Please Specify The Task Details"
                        else:
                            wit = "Sir! Please Specify The Tasks And Its Details"

                    elif "show" in command and "schedule" in command:
                        wit = "Displaying Schedule!"
                        display_schedule_thread = Thread(target=display_schedule_inside)
                        display_schedule_thread.start()

                    elif "skip" in command:
                        skip_thing_to_be_said = True
                        wit = "Skipping Sir!"

                    elif "wait" in command or "mute" in command or "hold" in command:
                        hold_thing_to_be_said = True
                        wit = "Muted Sir!"

                    elif "start" in command or "unmute" in command or "unhold" in command:
                        hold_thing_to_be_said = False
                        wit = "UnMuted Sir!"

                    elif "repeat" in command or "again" in command:
                        repeat_thing_to_be_said = True
                        wit = "Repeating Sir!"

                    elif "slow" in command:
                        slow_down_talking_speed = True
                        wit = "Slowed Sir!"

                    elif "fast" in command:
                        slow_down_talking_speed = False
                        wit = "Fast Sir!"

                    elif "shut up" in command or "clear" in command:
                        things_to_be_said = []
                        wit = "Clear Sir!"

                    elif "log: " in command:
                        log = command.split("log: ")[1].title()
                        save_log(log)
                        wit = "Log Saved Sir!"

                    elif "log" in command:
                        display_log_thread = Thread(target=display_logs)
                        display_log_thread.start()
                        wit = "Displayed Log Sir!"

                    elif "play" in command and "music" in command:
                        webbrowser.open("https://www.youtube.com/watch?v=Mvvsa5HAJiI&list=RDMM&start_radio=1")
                        wit = "Music Played Sir!"
                    
                    elif "play " in command:
                        video_title = command.replace("play ", "")
                        playonyt(video_title) 
                        wit = "Played Sir!"

                    elif "sort" in command and "files" in command:
                        sort_files_by_category_thread.start()
                        wit = "File Sorting Has Started! For Progress Check Terminal!"

                    elif "open" in command:
                        site_to_open = command.split("open", maxsplit=1)[1]
                        open_site(site_to_open)
                        wit = "Opened Sir!"

                    elif "openr" in command:
                        site_to_open = command.split("openr", maxsplit=1)[1]
                        open_rootsite(site_to_open)
                        wit = "Opened Sir!"

                    else:
                        wit = get_witty_reply()

                    things_to_be_said.insert(0, wit)

                except Exception as error:
                    print(error)
                    things_to_be_said.insert(0, "An Error Occured!")

                del commands_given[commands_given.index(command)]

command_processing_thread = Thread(target=processing_commands_back_to_back)

# Related To Displaying Info Easily

gui_background_color = 25/255, 33/255, 43/255, 1
secondary_window_color = 21/255, 21/255, 23/255, 1
text_color = 245/255, 245/255, 255/255, 1

font = "Font\static\SpaceGrotesk.ttf"
font_thin = "Font\static\SpaceGrotesk-Light.ttf"
font_regular = "Font\static\SpaceGrotesk-Regular.ttf"
font_medium = "Font\static\SpaceGrotesk-Medium.ttf"
font_semibold = "Font\static\SpaceGrotesk-SemiBold.ttf"
font_bold = "Font\static\SpaceGrotesk-Bold.ttf"

items_to_display = []
items_displayed = []
items_to_remove = []
item_removed = True

class SecondaryWindow(BoxLayout):
    pass

class HeadingDisplay(BoxLayout):
    pass

class VerticalDivider(BoxLayout):
    pass

class HorizontalDivider(BoxLayout):
    pass

class WrappingText(Label):
    pass

# Logs Related Functionality

def load_logs():
    with open("logs.json", "r") as logs_json:
        logs = json.load(logs_json)
    return logs

def save_log(log):
    
    logs = load_logs()
    
    log_time = get_datetime()
    log_time = f"{log_time[0]}; {log_time[1]}"
    
    logs[log_time] = log

    with open("logs.json", "w") as logs_json:
        json.dump(logs, logs_json)

def display_logs():

    global items_to_display

    logs = load_logs()

    log_times = list(logs.keys())

    logs_structure = {"Logs":[]}
    
    for log_time in log_times:
        logs_structure["Logs"].append({"text":f"{log_time}; {logs[log_time]}"})

    items_to_display.append(logs_structure)

# News Related Tasks

topics_i_want_to_be_informed_on_globally = ["international", "elon musk", "technology", "programming", "engineering", "software engineering"]

def get_news(topic):
    response = requests.get(f"https://newsapi.org/v2/everything?q={topic}&apiKey=ad8ca14bf00848c8a64d11a83caba503").json()
    articles = response["articles"]
    news_headlines = [f' {article["title"]}: \n {article["description"]}' for article in articles]
    return news_headlines

def get_pakistani_news():
    response = requests.get("https://www.geo.tv/category/pakistan")
    html_soup = BeautifulSoup(response.text, "html.parser")
    unfinalized_news_titles = html_soup.find_all("div", class_="entry-title")
    news_headlines = [str(unfinalized_news_title.text).split("\n")[1] for unfinalized_news_title in unfinalized_news_titles]
    return news_headlines

def getting_all_news():
    
    all_news_storage_array = []

    fetched_news = get_pakistani_news()
    all_news_storage_array.append({"Pakistani News": fetched_news})

    for topic in topics_i_want_to_be_informed_on_globally:
        try:
            fetched_news = get_news(topic)
        except KeyError:
            things_to_be_said.append("Global News Cannot Be Fetched Right Now! Displaying Only Pakistani News!")
            break
        all_news_storage_array.append({topic: fetched_news})    

    return all_news_storage_array

def getting_sorted_news():
    
    finalized_news_storage_array = []
    
    categorized_news = getting_all_news()

    total_word_count = 1000

    with open("news.json", "r") as news_file:
        news_json = json.load(news_file)

    for news_category in categorized_news:

        while True:

            category_word_count = int(total_word_count/7)

            finalized_category_news_array = []

            category = str(list(news_category.keys())[0])
            news_in_category = list(news_category.values())[0]

            try:

                news_stored = news_json[category]

                for news in news_in_category:
                    if news not in news_stored:
                        if category_word_count > 0:
                            finalized_category_news_array.append(news)
                            word_count_in_news = int(str(news).count(" "))
                            category_word_count = category_word_count - word_count_in_news
                        else:
                            break

                news_json[category].extend(finalized_category_news_array)
                finalized_news_storage_array.append({category:finalized_category_news_array})

                break

            except KeyError:
                news_json[category] = []

    with open("news.json", "w") as news_file:
        json.dump(news_json, news_file)

    return finalized_news_storage_array

def displaying_and_saying_news():
      
    global items_to_display, items_displayed, items_to_remove, item_removed, things_to_be_said

    sorted_news = getting_sorted_news()

    structure_for_automatic_display = {"News":[]}

    for news_category in sorted_news:

        category = str(list(news_category.keys())[0])

        news_in_category = list(news_category.values())[0]
        
        structure_for_automatic_display["News"].append({"subheader":category.title()})

        for news in news_in_category:
            news = str(news).lower().replace("read more", "").title()
            structure_for_automatic_display["News"].append({"text":news})
            things_to_be_said.append(news)

    items_to_display.append(structure_for_automatic_display)

# Related To Time Management

def get_date_for_schedule():
    
    with open("schedules.json", "r") as schedules_file:
        schedule_json_record = json.load(schedules_file)
    
    current_datetime = datetime.datetime.now()
    
    scheduling_day = schedule_json_record["scheduling day"]

    if scheduling_day == "tommorow":
        current_datetime = current_datetime + datetime.timedelta(days=1)

    date = f"{current_datetime.strftime('%A')}, {current_datetime.strftime('%d')} {current_datetime.strftime('%B')} {current_datetime.strftime('%Y')}"
    time = f"{current_datetime.strftime('%H')}:{current_datetime.strftime('%M')}"

    return [date, time, scheduling_day]

def load_saved_schedule():
    
    date = get_date_for_schedule()[0]

    with open("schedules.json", "r") as schedules_file:
        schedule_json_record = json.load(schedules_file)

    if date not in list(schedule_json_record.keys()):
        
        schedule_json_record[date] = {"Tasks": {}, "Schedule":{}}

        time = "00:-05"

        for i in range(12 * 24):

            split_time = time.split(":")
            time_for_now = datetime.timedelta(hours=int(split_time[0]), minutes=int(split_time[1]))
            addition_of_duration = datetime.timedelta(minutes=int(5))
            added_time = time_for_now + addition_of_duration
            total_seconds = int(added_time.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, _ = divmod(remainder, 60)

            time = "{:02d}:{:02d}".format(hours, minutes)
            
            schedule_json_record[date]["Schedule"][time] = {"Task":"", "Task Details":""}     

    else:

        tasks = schedule_json_record[date]["Tasks"]

        task_time_seconds_array = [(int(tasks[task]["Task Time"].split(":")[0]) * 60 * 60) + (int(tasks[task]["Task Time"].split(":")[1]) * 60) for task in tasks]
        task_time_seconds_array.sort()

        tasks_array = list(tasks.keys())

        tasks_array = {}
        
        for task in tasks_array:

            task_detail = tasks[task]

            task_time_seconds = (int(task_detail["Task Time"].split(":")[0]) * 60 * 60) + (int(task_detail["Task Time"].split(":")[1]) * 60)

            for task_seconds in task_time_seconds_array:

                if task_time_seconds == task_seconds:
                    tasks_array[task] = {"Task Detail": task_detail['Task Detail'], "Task Duration": task_detail['Task Duration'], "Task Time": task_detail['Task Time']}  

    with open("schedules.json", "w") as schedules_file:
        json.dump(schedule_json_record, schedules_file)

    return schedule_json_record

def add_task_in_schedule(task, task_detail, task_time, task_duration):

    schedule = load_saved_schedule()

    date = get_date_for_schedule()[0]

    schedule[date]["Tasks"][task] = {"Task Detail": task_detail, "Task Duration": task_duration, "Task Time": task_time} 
    
    task_time_array = list(schedule[date]["Schedule"].keys())

    time_index = task_time_array.index(task_time)    

    task_blocks = int(task_duration)/5

    for i in range(int(task_blocks)):
        schedule[date]["Schedule"][task_time_array[time_index + i]]["Task"] = task 
        schedule[date]["Schedule"][task_time_array[time_index + i]]["Task Details"] = task_detail

    with open("schedules.json", "w") as schedules_file:
        json.dump(schedule, schedules_file)

def display_schedule_inside():
    
    date = get_date_for_schedule()[0]

    time = get_date_for_schedule()[1]

    minute = int(time.split(":")[1])

    rounded_minute = round_to_nearest_base(minute)

    rounded_minute = rounded_minute - 5 if rounded_minute > minute else rounded_minute 
    
    rounded_time = f"{time.split(':')[0]}:{rounded_minute}" 

    rounded_time_seconds = (int(rounded_time.split(':')[0]) * 60 * 60) + (int(rounded_time.split(":")[1]) * 60)
    
    schedule = load_saved_schedule()

    title = f"Planning For {date}".title()

    display_format = {title:[]}

    tasks = schedule[date]["Tasks"]

    display_format[title].append({"subheader":"Tasks:"})

    tasks_array = list(tasks.keys())

    for task in tasks_array:

        task_detail = tasks[task]

        task_time_seconds = (int(task_detail["Task Time"].split(":")[0]) * 60 * 60) + (int(task_detail["Task Time"].split(":")[1]) * 60)

        if task_time_seconds >= rounded_time_seconds or get_date_for_schedule()[2] == "tommorow":

            display_format[title].append({"text":f"- {task}: {task_detail['Task Detail']} for {task_detail['Task Duration']} mins at {task_detail['Task Time']}".title()})

    display_format[title].append({"subheader":"Schedule:"})

    scheduled = schedule[date]["Schedule"]

    scheduled_times = list(scheduled.keys())

    root_scheduled_time_task = " | "

    for scheduled_time in scheduled_times:

        scheduled_task = scheduled[scheduled_time]

        scheduled_time_seconds = (int(scheduled_time.split(":")[0]) * 60 * 60) + (int(scheduled_time.split(":")[1]) * 60)

        if scheduled_time_seconds >= rounded_time_seconds or get_date_for_schedule()[2] == "tommorow":

            scheduled_time_task = f"{scheduled_time} | {scheduled_task['Task']}: {scheduled_task['Task Details']}"

            if scheduled_time_task.split("|")[1] != root_scheduled_time_task.split("|")[1]:
                if scheduled_time_task.split("|")[1].split(" : ")[0] != "":
                    display_format[title].append({"text":scheduled_time_task.title()})
                    root_scheduled_time_task = scheduled_time_task
                else:
                    display_format[title].append({"text":scheduled_time_task.split("|")[0].title()})
            else: 
                display_format[title].append({"text":scheduled_time_task.split("|")[0].title()})

    items_to_display.append(display_format)

# Numbers Game

def numbers_game():
    
    to_guess_number = random.randint(1, 1000)
    attempts = 7

    global numbers_game_going_on, numbers_game_my_choice
    things_to_be_said.insert(0, "Starting Game Of Numbers! Number To Guess Is Less Than 1000 And You Have 7 Attempts")

    numbers_game_going_on = True

    while True:
        
        if numbers_game_my_choice:

            if numbers_game_my_choice < to_guess_number:
                comment = "Go Bigger!"

            elif numbers_game_my_choice > to_guess_number:
                comment = "Go Smaller!"

            elif numbers_game_my_choice == to_guess_number:
                comment = "You Won! Want To Play Again?"

            if attempts == 0:
                if comment != "You Won! Want To Play Again?":
                    comment = "You Have Lost As You Ran Out Of Attempts!"

            things_to_be_said.insert(0, comment)

            numbers_game_my_choice = 0
            attempts = attempts - 1
            

        else:
            time.sleep(1)

# Rock Paper Scissor 

def rock_paper_scissor():
    
    score_of_mine, score_of_jarvis = 0, 0

    combos = ["rock beats scissor", "paper beats rock", "scissor beat paper"]

    global rock_paper_scissors_my_choice, rock_paper_scissor_going_on, rock_paper_scissor_options
    rock_paper_scissors_my_choice = ""

    things_to_be_said.insert(0, "Starting Game Of Rock Paper Scissor!")

    rock_paper_scissor_going_on = True

    while True:
        
        if rock_paper_scissors_my_choice:

            choice_of_jarvis = random.choice(rock_paper_scissor_options)

            if rock_paper_scissors_my_choice == choice_of_jarvis:
                comment = f"Draw As Both Chose {rock_paper_scissors_my_choice}!"

            else:
                if f"{rock_paper_scissors_my_choice} beats {choice_of_jarvis}" in combos:
                    comment = f"You Won As I Chose {choice_of_jarvis}!"
                else:
                    comment = f"I Won As I Chose {choice_of_jarvis}!"

            score_innings = f"You - {score_of_mine} | Me - {score_of_jarvis}"
            comment = f"{comment} {score_innings}"

            things_to_be_said.insert(0, comment)

            if score_of_jarvis == 3:
                things_to_be_said.insert(0, "I Won")  
                rock_paper_scissor_going_on = False
                break

            if score_of_mine == 3:
                things_to_be_said.insert(0, "You Won")  
                rock_paper_scissor_going_on = False
                break

            rock_paper_scissors_my_choice = ""
        
        else:
            time.sleep(1)

# Main App

class JarvisApp(App):
    pass

class JarvisMainLayout(BoxLayout):
    pass

class AuraColumn(BoxLayout):
    
    time, date, seconds_left_in_the_day, witty_reply, aura_source, listening_status = StringProperty(""), StringProperty(""), StringProperty(""), StringProperty(""), StringProperty(""), StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.update_all_time_related_things, 1)

        Clock.schedule_interval(self.update_aura_source, 1)
        Clock.schedule_interval(self.update_witty_reply, 1)
        Clock.schedule_interval(self.update_listening_status, 1)

    def update_all_time_related_things(self, dt):
        current_datetime = datetime.datetime.now()
        self.time = f"{current_datetime.strftime('%H')}:{current_datetime.strftime('%M')}:{current_datetime.strftime('%S')}"
        self.date = f"{current_datetime.strftime('%A')}, {current_datetime.strftime('%d')} {current_datetime.strftime('%B')} {current_datetime.strftime('%Y')}"
        self.seconds_left_in_the_day = str( 84600 - (int(current_datetime.strftime('%H')) * 60 * 60) - (int(current_datetime.strftime('%M')) * 60) - int(current_datetime.strftime('%S')) ) + f" Seconds"
        
    def update_aura_source(self, dt):
        global aura_source 
        self.aura_source = aura_source

    def update_witty_reply(self, dt):
        global witty_reply 
        self.witty_reply = witty_reply[:190] + "...." if len(witty_reply) > 190 else witty_reply 


    def update_listening_status(self, dt):
        global listening_status 
        self.listening_status = listening_status

    def submit_command(self, widget):
        global commands_given
        command = str(widget.text).lower()
        commands_given.append(command)

class DumEColumn(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.handle_display, 3)

    def handle_display(self, dt):
        
        global items_to_display
        
        if items_to_display:
            for item_to_display in items_to_display:

                if type(item_to_display) == dict:
                    header_text = list(item_to_display.keys())[0]
                    window = SecondaryWindow()
                    window.orientation = "vertical"
                    window.spacing = dp(10)
                    window.padding = dp(10)

                    window.size_hint = (1, None)
                    window.height = dp(0)

                    header = Label(color=gui_background_color, font_name=font_bold, font_size=dp(23), size_hint=(1, None), height=dp(20))
                    header.text = header_text
                    window.height = window.height + dp(100)
                    
                    heading_display = HeadingDisplay()
                    heading_display.add_widget(header)
                    window.add_widget(heading_display)
                    
                    display_item_array = list(item_to_display.values())[0]

                    for item in display_item_array:
                        item_type = str(list(item.keys())[0])
                        item_text = str(list(item.values())[0])

                        if item_type == "subheader":
                            sub_header = Label(padding=(0, dp(20)), color=text_color, font_name=font_semibold, font_size=dp(20), size_hint=(1, None), height=dp(24))
                            sub_header.text = item_text

                            divider = HorizontalDivider()
                            divider2 = HorizontalDivider()
                            
                            window.add_widget(divider)
                            window.add_widget(sub_header)           
                            window.add_widget(divider2)
                            window.height = window.height + dp(100)

                        if item_type == "text":
                            
                            normal_text = WrappingText()
                            normal_text.text = item_text 
                            window.add_widget(normal_text)
                            for i in range(int(len(item_text)/window.
                                               width)+ 1):
                                window.height = window.height + dp(30)

                    window.add_widget(BoxLayout())

                    self.add_widget(window)

            items_displayed.append(item_to_display)
            del items_to_display[items_to_display.index(item_to_display)]
        
        if items_to_display:
            for item_to_display in items_to_display:

                if type(item_to_display) == dict:
                    header_text = list(item_to_display.keys())[0]
                    window = SecondaryWindow()
                    window.orientation = "vertical"
                    window.spacing = dp(10)
                    window.padding = dp(10)

                    window.size_hint = (1, None)
                    window.height = dp(0)

                    header = Label(color=gui_background_color, font_name=font_bold, font_size=dp(23), size_hint=(1, None), height=dp(20))
                    header.text = header_text
                    window.height = window.height + dp(100)
                    
                    heading_display = HeadingDisplay()
                    heading_display.add_widget(header)
                    window.add_widget(heading_display)
                    
                    display_item_array = list(item_to_display.values())[0]

                    for item in display_item_array:
                        item_type = str(list(item.keys())[0])
                        item_text = str(list(item.values())[0])

                        if item_type == "subheader":
                            sub_header = Label(padding=(0, dp(20)), color=text_color, font_name=font_semibold, font_size=dp(20), size_hint=(1, None), height=dp(24))
                            sub_header.text = item_text

                            divider = HorizontalDivider()
                            divider2 = HorizontalDivider()
                            
                            window.add_widget(divider)
                            window.add_widget(sub_header)           
                            window.add_widget(divider2)
                            window.height = window.height + dp(100)

                        if item_type == "text":
                            
                            normal_text = WrappingText()
                            normal_text.text = item_text 
                            window.add_widget(normal_text)
                            for i in range(int(len(item_text)/window.
                                               width)+ 1):
                                window.height = window.height + dp(30)

                    window.add_widget(BoxLayout())

                    self.add_widget(window)

            items_displayed.append(item_to_display)
            del items_to_display[items_to_display.index(item_to_display)]

if __name__ == "__main__":

    # Starting The Threads
    saying_thread.start()
    listening_thread.start()

    command_processing_thread.start()

    # Starting The App
    JarvisApp().run()