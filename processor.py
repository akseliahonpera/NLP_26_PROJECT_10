import json
import os 

def get_filenames_in_workdir():
    """Get filenames of files in the current folder and retuirn as list"""
    file_list = []
    for file in os.listdir():
        if file.endswith(".json"):
            file_list.append(file)
            
    print("found following input files from the workdir")
    for file in file_list:
        print(file)
        
    return file_list
       
def processor(filenames,target_path="trimmed_file.txt"):
    """Takes filenamelist and processed it to actually readdable and handleable(smaller) format"""
    for file in filenames:
        thread_object = {} 
        with open(file, "r",errors="replace",encoding = 'UTF-8') as f:
            with open(target_path, "a",errors="replace",encoding = 'UTF-8') as f2:##not smart but i dont care enough to change
                for line in f:
                    line = json.loads(line)
                    for index in line:
                        thread_object = {}
                        thread_object["date"]                   = index['text']['date']
                        thread_object["comment_id"]             = index['text']['comment_id']
                        thread_object["parent_comment_id"]      = index['text']['parent_comment_id']
                        thread_object["quoted_comment_id"]      = index['text']['quoted_comment_id']
                        thread_object["thread_id"]              = index['text']['thread_id']
                        thread_object["title"]                  = index['text']['title']
                        thread_object["msg_type"]               = index['text']['msg_type']
                        thread_object["topic_names"]            = index['text']['topic_names']
                        thread_object["thread_start_datetime"]  = index['text']['thread_start_datetime']

                        thread_object["orig_msg"]               = []
                        thread_object["orig_msg_lemmatized"]    = []
                        orig_msg_data_whole                     = index['data'][0]['data'][0]['data']
                        for word_data in orig_msg_data_whole:
                            thread_object["orig_msg"].append(word_data['word'])
                            thread_object["orig_msg_lemmatized"].append(word_data['lemma'])
                        thread_object["comments"]               = []
                        
                        f2.write(json.dumps(thread_object)+"\n")
                        
                    print(f'Currently processing file: {file}')
                
                
        
def concatenate_threads_root(temp_file_list, final_file):
    """Doing this in a lazy and wasteful way, 1 pass for thread starts, 2nd pass for related comments."""
    final_f = open(final_file, "a", errors="replace", encoding="utf-8")
    for file in temp_file_list:
        with open(file, "r", errors="replace", encoding="utf-8") as f:
            for row in f:
                record = json.loads(row)
                if record["msg_type"]=="thread_start":
                    final_f.write(json.dumps(record)+"\n")
    final_f.close()
    
def concatenate_threads_comments(temp_file_list, root_file,target_file):
    """Doing this in a lazy and wasteful way, 1 pass for thread starts, 2nd pass for related comments."""
    #final_f = open(final_file, "a", errors="replace", encoding="utf-8")
    root_f = open(root_file, "r", errors="replace", encoding="utf-8")
    
    for record in root_f:
        json_row = json.loads(record)
        root_t_id = json_row["thread_id"]
        
        for file in temp_file_list:
            with open(file, "r", errors="replace", encoding="utf-8") as f:
                for row in f:
                    json_row2 = json.loads(row)
                    if root_t_id == json_row2["thread_id"] and json_row2["msg_type"]=="comment":
                        json_row["comments"].append(json_row2)
                        
        with open(target_file, "a", errors="replace", encoding="utf-8") as t_file:
            t_file.write(json.dumps(json_row)+"\n")
    
    
    root_f.close()   


def concat_in_memory(root_file, trimmed_files, result_file,  bastard_file):
    """Root file contains all thread starts, trimmed files contain all files, result file is the target for all"""
    root_file_memory = {}
    bastard_json_memory = []
    skipped = 0
    ##load root_file to memoryview
    root_f = open(root_file, "r", errors="replace", encoding="utf-8")
    print("loading root to memory")
    for record in root_f:
        thread = json.loads(record)
        root_file_memory[thread["thread_id"]] = thread
        
    root_f.close()    
    print("root loaded in memory")
    ##Ugly af matcher
    print("shitty search starting")
    for file in trimmed_files:
        with open(file, "r", errors="replace", encoding="utf-8") as f:
            for record in f:
                json_object = json.loads(record)
                if json_object["msg_type"]=="comment":
                    try:
                        if root_file_memory[json_object["thread_id"]]:
                            root_file_memory[json_object["thread_id"]]["comments"].append(json_object)
                    except KeyError:
                        
                        skipped+=1
                        bastard_json_memory.append(json_object)
                    ###If no matching thread is found the comment is dropped. Why you may ask... 67!
   
    print(f'Total number skipped {skipped}')
    with open(result_file,"a", errors="replace", encoding="utf-8") as f2:
        print("writing to result file:")
        for thread in root_file_memory.values():
            f2.write(json.dumps(thread)+"\n")
        print("writing to result file complete")
        
    with open(bastard_file,"a", errors="replace", encoding="utf-8") as f3:
        print("writing to bastard file:")
        for thread in bastard_json_memory:
            f3.write(json.dumps(thread)+"\n")
        print("writing to bastard file complete") 
 
def main():
    file_list = get_filenames_in_workdir()
    temp_file = "mixed_threads_n_comments.txt"
    root_file = "root_file.txt"
    conc_file = "threads_with_comments.txt"
    bastard_file = "bastards.txt"
    
    #processor(file_list,temp_file)
    #concatenate_threads_root([temp_file],root_file)
    concat_in_memory(root_file,[temp_file], conc_file, bastard_file)
    print("exiting")



if __name__ == '__main__':
    main()
