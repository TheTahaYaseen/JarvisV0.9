
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

