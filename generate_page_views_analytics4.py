from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

import traceback
import argparse
import sys

__author__ = "Vitaly Saversky"
__date__ = "2023-12-24"
__credits__ = ["Vitaly Saversky"]
__version__ = "1.0.0"
__maintainer__ = "Vitaly Saversky"
__email__ = "larandvit@hotmail.com"
__status__ = "Production"

class ExitCode():
    SUCCESS = 0
    ERROR_MISSING_GOOGLE_APPLICATION_CREDENTIALS_VARIABLE = 1
    ERROR_RUNTIME = 255

def run_report(property_id, output_path):
    
    # Using a default constructor instructs the client to use the credentials
    # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = BetaAnalyticsDataClient()

    request = RunReportRequest(
        property=f'properties/{property_id}',
        dimensions=[Dimension(name='pagePath')],
        metrics=[Metric(name='screenPageViews')],
        date_ranges=[DateRange(start_date='2020-03-31', end_date='today')],
    )
    response = client.run_report(request)

    with open(output_path, 'w') as f_out:
        f_out.write('const blog_views = new Map([\n')
        
        comma = ''
        for row in response.rows:
            page_name = row.dimension_values[0].value
            page_views = row.metric_values[0].value
            
            f_out.write(f'{comma}["{page_name}", {page_views}]\n')
            comma = ','
            
        f_out.write(']);')
        
    print('Google Analytics 4 page views report file has been created succesfully')
    sys.exit(ExitCode.SUCCESS)
        
if __name__ == "__main__":
    try:
        
        parser = argparse.ArgumentParser(description="Generate Google Analytics 4 page view report file v. {}".format(__version__))
        
        parser.add_argument('-p', 
                            '--propertyid', 
                            dest='property_id',
                            required=True,
                            help='Google Analytics 4 property_id')
        
        parser.add_argument('-o', 
                            '--outputpath', 
                            dest='output_path',
                            required=True,
                            help='Google Analytics 4 page views report file output path')
        
        args = parser.parse_args()
        property_id = args.property_id
        output_path = args.output_path
        
        run_report(property_id, output_path)
        
    except SystemExit:
        pass
    
    except:
        error_message = traceback.format_exc()
        
        print('Google Analytics 4 page views report file creation has been failed')
        
        if error_message.find('google.auth.exceptions.DefaultCredentialsError: Your default credentials were not found. To set up Application Default Credentials')>0:
            print('Missing credentials json file. Set it up with the command below.')
            print(r'export GOOGLE_APPLICATION_CREDENTIALS="Path to credentials json file"')
            sys.exit(ExitCode.ERROR_MISSING_GOOGLE_APPLICATION_CREDENTIALS_VARIABLE)
        else:
            print(error_message)
            sys.exit(ExitCode.ERROR_RUNTIME)
        
        
        
        