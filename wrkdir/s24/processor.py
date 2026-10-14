import json
import os 

def get_filenames_in_workdir():
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
                
                
        
def concatenate_threads(temp_file_list, final_file):
    """Doing this in a lazy and wasteful way,"""
    
    for file in temp_file_list:
        with open(final_file, "a", errors="replace", encoding="utf-8") as f:
        
        


def main():
    file_list = get_filenames_in_workdir()
    
    processor(file_list)
    print("exiting")



if __name__ == '__main__':
    main()
