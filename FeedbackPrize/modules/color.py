# エッセイを色塗りする関数
# 先にgapをNothingで埋めたほうがいいかも。
# KaggleNotebookでの動作を前提。
def print_colored_essay(essay):
    df_essay = add_gap_rows(essay)
    #code from https://www.kaggle.com/odins0n/feedback-prize-eda, but adjusted to df_essay
    essay_file = "../input/feedback-prize-2021/train/" + essay + ".txt"

    ents = []
    for i, row in df_essay.iterrows():
        ents.append({
                        'start': int(row['discourse_start']), 
                         'end': int(row['discourse_end']), 
                         'label': row['discourse_type']
                    })

    with open(essay_file, 'r') as file: data = file.read()

    doc2 = {
        "text": data,
        "ents": ents,
    }

    colors = {'Lead': '#EE11D0','Position': '#AB4DE1','Claim': '#1EDE71','Evidence': '#33FAFA','Counterclaim': '#4253C1','Concluding Statement': 'yellow','Rebuttal': 'red'}
    options = {"ents": df_essay.discourse_type.unique().tolist(), "colors": colors}
    spacy.displacy.render(doc2, style="ent", options=options, manual=True, jupyter=True);