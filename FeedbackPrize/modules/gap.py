# gap_length, gap_endlengthを計算する。
# train_txtは train_txt = glob('../input/feedback-prize-2021/train/*.txt')で多分取れる。
def get_gap_length(train, train_txt): 
    len_dict = {}
    word_dict = {}
    for t in tqdm(train_txt):
        with open(t, "r") as txt_file:
            myid = t.split("/")[-1].replace(".txt", "")
            data = txt_file.read()
            mylen = len(data.strip())
            myword = len(data.split())
            len_dict[myid] = mylen
            word_dict[myid] = myword
    train["essay_len"] = train["id"].map(len_dict)
    train["essay_words"] = train["id"].map(word_dict)
    #initialize column
    train['gap_length'] = np.nan

    #set the first one
    train.loc[0, 'gap_length'] = 7 #discourse start - 1 (previous end is always -1)

    #loop over rest
    for i in tqdm(range(1, len(train))):
        #gap if difference is not 1 within an essay
        if ((train.loc[i, "id"] == train.loc[i-1, "id"])\
            and (train.loc[i, "discourse_start"] - train.loc[i-1, "discourse_end"] > 1)):
            train.loc[i, 'gap_length'] = train.loc[i, "discourse_start"] - train.loc[i-1, "discourse_end"] - 2
            #minus 2 as the previous end is always -1 and the previous start always +1
        #gap if the first discourse of an new essay does not start at 0
        elif ((train.loc[i, "id"] != train.loc[i-1, "id"])\
            and (train.loc[i, "discourse_start"] != 0)):
            train.loc[i, 'gap_length'] = train.loc[i, "discourse_start"] -1


    #is there any text after the last discourse of an essay?
    last_ones = train.drop_duplicates(subset="id", keep='last')
    last_ones['gap_end_length'] = np.where((last_ones.discourse_end < last_ones.essay_len),\
                                        (last_ones.essay_len - last_ones.discourse_end),\
                                        np.nan)

    cols_to_merge = ['id', 'discourse_id', 'gap_end_length']
    train = train.merge(last_ones[cols_to_merge], on = ["id", "discourse_id"], how = "left")

    return train


# エッセイに含まれるgapを、discource_tyoe=Notingとして追加する関数。
# 先にget_gap_lengthを実行してね。
def add_gap_rows(essay, train):
    cols_to_keep = ['discourse_start', 'discourse_end', 'discourse_type', 'gap_length', 'gap_end_length']
    df_essay = train.query('id == @essay')[cols_to_keep].reset_index(drop = True)

    #index new row
    insert_row = len(df_essay)
   
    for i in range(1, len(df_essay)):          
        if df_essay.loc[i,"gap_length"] >0:
            if i == 0:
                start = 0 #as there is no i-1 for first row
                end = df_essay.loc[0, 'discourse_start'] -1
                disc_type = "Nothing"
                gap_end = np.nan
                gap = np.nan
                df_essay.loc[insert_row] = [start, end, disc_type, gap, gap_end]
                insert_row += 1
            else:
                start = df_essay.loc[i-1, "discourse_end"] + 1
                end = df_essay.loc[i, 'discourse_start'] -1
                disc_type = "Nothing"
                gap_end = np.nan
                gap = np.nan
                df_essay.loc[insert_row] = [start, end, disc_type, gap, gap_end]
                insert_row += 1

    df_essay = df_essay.sort_values(by = "discourse_start").reset_index(drop=True)

    #add gap at end
    if df_essay.loc[(len(df_essay)-1),'gap_end_length'] > 0:
        start = df_essay.loc[(len(df_essay)-1), "discourse_end"] + 1
        end = start + df_essay.loc[(len(df_essay)-1), 'gap_end_length']
        disc_type = "Nothing"
        gap_end = np.nan
        gap = np.nan
        df_essay.loc[insert_row] = [start, end, disc_type, gap, gap_end]
        
    return(df_essay)