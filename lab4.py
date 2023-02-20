import pandas as pd
from log_analysis import get_log_file_path_from_cmd_line,filter_log_by_regex
def main():
    log_file = get_log_file_path_from_cmd_line(param_num=True)
    dpt_tally = tally_port_traffic(log_file)
    #records = filter_log_by_regex(log_file,'SRC=(.*?) DSR=(.*?) LEN=(.*?)',print_summary=True,print_records=True)
    for dpt, count in dpt_tally.items():
      if count>100:
            generate_port_traffic_report(log_file,dpt)
    pass
    generate_invalid_user_report(log_file)

#Step 8
def tally_port_traffic(log_file):
    dest_port_logs = filter_log_by_regex(log_file,'DPT=(.+?)')[1]
    
    dpt_tally={}
    for dpt_tuple in dest_port_logs:
        dpt_num=dpt_tuple[0]
        dpt_tally[dpt_num] = dpt_tally.get(dpt_num,0)+1
    
    return dpt_tally

#Step 9
def generate_port_traffic_report(log_file, port_number):
    regex =r"^(.{6}) (.{8}).*SRC=(.+?) .*SPT=(.+?)" + f"DPT=({port_number})"
    captured_data=filter_log_by_regex(log_file,regex)[1]
    
    report_df = pd.DataFrame(captured_data)
    report_header =  ('Date','Time','Source IP Address','Destination IP Address','Destination port')
    report_df.to_csv(f'destination_port{port_number}_report.csv', index=False, header=report_header)

# TODO: Step 11
def generate_invalid_user_report(log_file):
    invalid_report=filter_log_by_regex(log_file)
    report_df= pd.DataFrame(invalid_report)
    header = ('Date','Time','Username','IP Address')
    report_df.to_csv(f'invalid_user.csv',index=False,header=header)
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    source_ip= filter_log_by_regex(log_file)
    report= pd.DataFrame(source_ip)
    
    return

if __name__ == '__main__':
    main()