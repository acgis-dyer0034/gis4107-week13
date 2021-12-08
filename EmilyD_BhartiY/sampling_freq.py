import water_stn_converter as wsc
import csv

def create_sampling_report(in_json_filename, out_csv_filename):
    #this will open the out_csv_filename for writing authorization
    with open(in_json_filename, 'w') as infile:
        writer = csv.writer(infile)
        #this will writ ethe list of seaonal and yearly counts
        header = infile.readline()
        writer.writerow(header)

    with open(out_csv_filename) as outfile:
                outfile.write(wsc.get_sampling_frequencies())

# with open(in_json_filename) as infile
#Hi Emily  since we are opening the json file here, should we be using csv.writer?
#
# 
# with open(out_csv_filename,'w') as outfile:
#      outfile.write(wsc.get_sampling_frequencies())            





