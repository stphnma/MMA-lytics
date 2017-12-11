import urllib2
from urllib2 import HTTPError
from bs4 import BeautifulSoup
from datetime import datetime


def get_totals_data(data):
    tds = data.findAll("td")
    if len(tds) != 10:
        print "something wrong"
        return None
    else:
        f1 = {}
        f2 = {}
        f1['name'] = tds[0].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['name'] = tds[0].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['kd'] = tds[1].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['kd'] = tds[1].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['sig_str'] = tds[2].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['sig_str'] = tds[2].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['sig_str_perc'] = tds[3].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['sig_str_perc'] = tds[3].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['total_strikes'] = tds[4].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['total_strikes'] = tds[4].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['td'] = tds[5].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['td'] = tds[5].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['sub_att'] = tds[7].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['sub_att'] = tds[7].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['pass'] = tds[8].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['pass'] = tds[8].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['rev'] = tds[9].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['rev'] = tds[9].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()
        return [f1, f2]


def get_sigstrike_data(data):
    tds = data.findAll("td")
    if len(tds) != 9:
        print "something wrong"
        return None
    else:
        f1 = {}
        f2 = {}
        
        f1['name'] = tds[0].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['name'] = tds[0].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['sig_str'] = tds[1].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['sig_str'] = tds[1].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['sig_str_perc'] = tds[2].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['sig_str_perc'] = tds[2].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()
        
        f1['head'] = tds[3].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['head'] = tds[3].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['body'] = tds[4].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['body'] = tds[4].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['leg'] = tds[5].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['leg'] = tds[5].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['distance'] = tds[6].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['distance'] = tds[6].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['clinch'] = tds[7].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['clinch'] = tds[7].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        f1['ground'] = tds[8].find_all("p", {'class': 'b-fight-details__table-text'})[0].text.encode('utf-8').strip()
        f2['ground'] = tds[8].find_all("p", {'class': 'b-fight-details__table-text'})[1].text.encode('utf-8').strip()

        return [f1, f2]

def get_fight_results(fight_results):
    results = []
    for fight in fight_results:
        f = {}
        f['name'] = fight.find("h3").text.encode('utf-8').strip()
        f['result'] = fight.find('i',{'class': 'b-fight-details__person-status'}).text.encode('utf-8').strip()
        results.append(f)
    return results


def get_Fight_Title(soup):
    return soup.findAll('h2', {'class' : 'b-content__title'})[0].text.encode('utf-8').strip()


def get_fight_details(fight_details):
    
    data = {}
    data['bout'] = fight_details.find("i","b-fight-details__fight-title").text.encode('utf-8').strip()
    data['method'] = fight_details.findAll('p')[0].find('i',{'style':"font-style: normal"}).text.encode('utf-8').strip()
    data['round'] = fight_details.findAll('p')[0].findAll('i','b-fight-details__text-item')[0].text.encode('utf-8').replace(" ","").replace("\n","")
    data['time'] = fight_details.findAll('p')[0].findAll('i','b-fight-details__text-item')[1].text.encode('utf-8').replace(" ","").replace("\n","")
    data['time_format'] = fight_details.findAll('p')[0].findAll('i','b-fight-details__text-item')[2].text.encode('utf-8').replace(" ","").replace("\n","")
    data['referee'] = fight_details.findAll('p')[0].findAll('i','b-fight-details__text-item')[3].text.encode('utf-8').replace(" ","").replace("\n","")
    data['details'] = fight_details.findAll('p')[0].findAll('i','b-fight-details__text-item_first')[0].text.encode('utf-8').replace(" ","").replace("\n","")           
    return data


def get_all(url):
    soup = BeautifulSoup(urllib2.urlopen(url))

    fight_title = get_Fight_Title(soup)

    fight_details = soup.find("div","b-fight-details__fight")
    fight_details = get_fight_details(fight_details)

    table = soup.find_all('table')

    totals_data = []
    totals_soup = table[1].findAll({'th' : "Round", 'tr' : True})
    totals_round_indices = [i for i in range(len(totals_soup)) if "Round" in str(totals_soup[i])]
    for k in totals_round_indices:
        totals = get_totals_data(totals_soup[k+1])
        for t in totals:
            t['round'] = totals_soup[k].text.encode('utf-8').strip()
        totals_data.extend( totals)

    sig_strikes_data = []
    sig_strike_soup = table[3].findAll({'th' : "Round", 'tr' : True})
    sig_strike_round_indices = [i for i in range(len(sig_strike_soup)) if "Round" in str(sig_strike_soup[i])]
    for k in sig_strike_round_indices:
        sigs = get_sigstrike_data(sig_strike_soup[k+1])
        for s in sigs:
            s['round'] = sig_strike_soup[k].text.encode('utf-8').strip()
        sig_strikes_data.extend(sigs)

    fight_results = get_fight_results(soup.findAll('div', {'class': 'b-fight-details__person'}))

    data = {
        'url': url,
        'fight_title' : fight_title,
        'fight_details' : fight_details,
        'fight_results' : fight_results,
        'totals': totals_data,
        'sig_strikes': sig_strikes_data,
    }
    
    return data


def get_main_events(main_url):
    ''' Returns list of urls of main events from FightMetrics
    ''' 
    soup = BeautifulSoup(urllib2.urlopen(main_url))
    event_urls = []
    trs = soup.find_all('tr')
    for tr in trs:
        for link in tr.find_all('a'):
            event_urls.append(link.get('href'))
    return event_urls

def get_event_detail_links(url):
    soup = BeautifulSoup(urllib2.urlopen(url))
    
    main = {}
    main['main_url'] = url
    
    date_tag = soup.findAll('li', {'class' : 'b-list__box-list-item'})[0]
    main['date'] = date_tag.contents[len(date_tag.contents) - 1].encode('utf-8').strip()
    
    main['fight_title'] = soup.findAll('h2', {'class' : 'b-content__title'})[0].text.encode('utf-8').strip()
    
    main['links'] = []
    tds = soup.find_all('td')
    for td in tds:
        for link in td.find_all('a'):
            url = link.get('href')
            main['links'].append(url)
    return main


MAIN_URL = "http://www.fightmetric.com/statistics/events/completed?page=all"

SLEEP_INTERVAL = 15

if __name__ == '__main__':
    
    import json
    import os
    import time
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default="0", help="start index")
    args = vars(ap.parse_args())
    s = args["start"]

    if not os.path.exists("raw"):
        os.makedirs("raw")

    events = get_main_events(MAIN_URL)
    print "%d events on main page" %len(events)

    for k in range(s, len(events)):

        if k % SLEEP_INTERVAL == 0 and k > 0:
            print "sleeping 60 seconds"
            time.sleep(60)

        e = events[k]
        e_details = get_event_detail_links(e)
        print k, e_details['fight_title']
        
        if datetime.strptime(e_details['date'], "%B %d, %Y") < datetime.today():

            e_data = []
            
            for url in e_details['links']:
                if "fight-details" in url:
                    data = get_all(url)
                    data['date'] = e_details['date']
                    e_data.append(data)
            to_file = os.getcwd() +"/raw/%s.json"%e_details['fight_title'].replace(" ", "_")

            with open(to_file, 'w') as fp:
                json.dump(e_data, fp)

        # except Exception as error:
        #     print e_details['fight_title'], error






