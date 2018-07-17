import pandas as pd
import json

def prepare_df(df):
    df.rename(columns={"Source":"source","Destination":"target"}, inplace=True)

    grouped_df = df.groupby(["source","target"]).size().reset_index()

    unique_nodes = pd.Index(grouped_df['source']
                      .append(grouped_df['target'])
                      .reset_index(drop=True).unique())

    temp_links_list = list(df.apply(lambda row: {"source": row['source'], "target": row['target'], "value": row['value']}, axis=1))


    links_list = []
    for link in temp_links_list:
        record = {"value":link['value'], "source":unique_nodes.get_loc(link['source']),
        "target": unique_nodes.get_loc(link['target'])}
        links_list.append(record)

    nodes_list = []

    for node in unique_nodes:
        nodes_list.append({"name":node, "group": 1})
    
    json_prep = {"nodes":nodes_list, "links":links_list}

  
    

    json_dump = json.dumps(json_prep, indent=1, sort_keys=True)

    filename_out = 'pcap_export.json'
    json_out = open(filename_out,'w')
    json_out.write(json_dump)
    json_out.close()
