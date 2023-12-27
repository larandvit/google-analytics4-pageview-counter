# Google Analytics 4 Page Views Counter

## Description

The repository is a sample on how to implement Google Analytics 4 in static web site. Google Analytics 4 reduces options to do it 
comparing with Google Universal Analytics. 

The main idea is to generate a report with page views in Python Google Analytics library on schedule and store it in a javascript file as a variable.   

The sample content is.

1. show_pageviews.html - shows pageviews counter.

2. pageviews.js - retrieve stored Google Analytics 4 report from a javascript file.

3. blog_metrics.js - Google Analytics 4 report data.

4. generate_page_views_analytics4.py - a tool to generate Google Analytics 4 report data on schedule.

5. [key file].json - service account key JSON file .

## Generate Google Analytics token usage

```
usage: generate_page_views_analytics4.py [-h] -p PROPERTY_ID -o OUTPUT_PATH

Generate Google Analytics 4 page view report file v. 1.0.0

optional arguments:
  -h, --help            show this help message and exit
  -p PROPERTY_ID, --propertyid PROPERTY_ID
                        Google Analytics 4 property_id
  -o OUTPUT_PATH, --outputpath OUTPUT_PATH
                        Google Analytics 4 page views report file output path
``` 

Sample of usage in Alpine Linux where the tool and service account file located in `/opt/generate_page_views_analytics4` folder and web site in `/var/www/sample.com` folder.


```console
export GOOGLE_APPLICATION_CREDENTIALS="/opt/generate_page_views_analytics4/tech-jogging-blog-58s414ae632b.json"
python3 /opt/generate_page_views_analytics4/generate_page_views_analytics4.py -p 123456789 -o /var/www/sample.com/blog_metrics.js
``` 

## Prerequisites

1. Set up Google Analytics for using Google Analytics 4 Data API.

2. Install Python library

   ````console
   pip install google-analytics-data
   ```

## How to run it in sample mode

1. Publish files to a web server.
   * show_pageviews.html
   * pageviews.js
   * blog_metrics.js
2. Open show_pageviews.html page. 

## How to run it in production mode

1. Make changes to your Web site pages as per samples in files.
   * pageviews.js
   * show_pageviews.html

2. Publish files to a Web server folder.
   * Modified pageviews.js
   * Your updated Web pages.
   
3. Copy files to your Linux machine.
   * [key file].json
   * generate_page_views_analytics4.py
   
4. Run `generate_page_views_analytics4.py` file to generate `blog_metrics.js` page views report file.

5. Copy `blog_metrics.js` file to Web server folder.

6. Open your web site pages.

## Set up to renew page views file on schedule with cron job scheduler 

1. Switch to root account if needed.

   ```console
   sudo su
   ```

2. Open `crontab` editor.

   ```console
   crontab -e
   ```

3. Add the command item.

   It runs cron job once an hour. Based on my experience, Google Analytics 4 database is updated daily.  

   ```
   0 * * * * python3 /opt/generate_page_views_analytics4/launcher.sh
   ```

   `launcher.sh` is located in `/opt/generate_page_views_analytics4` folder and encapsulate the logic to run the process.

   ```console
   export GOOGLE_APPLICATION_CREDENTIALS="/opt/generate_page_views_analytics4/[key file].json"
   python3 /opt/generate_page_views_analytics4/generate_page_views_analytics4.py -p [property_id] -o /var/www/sample.com/blog_metrics.js
   ```

4. Validate your setup.

   ```console
   crontab -l
   ```

## Documentation

[API Quickstart](https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries)
 