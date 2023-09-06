from bart_score import BARTScorer
import numpy as np

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--gts_file', default="../test/commongen_test_eval_hypothesis_multi.txt", type=str)
parser.add_argument('--res_file', default="../test/commongen_test_eval_reference_multi.txt", type=str)
parser.add_argument('--dataset_name', default="", type=str)
args = parser.parse_args()

def BARTScore_multi(gts,res):
    bart_score = BARTScorer(device='cuda:0', checkpoint='facebook/bart-large-cnn')

    with open(res) as f:
    ## with open("/home/jaehyung/PycharmProjects/ACL2023/GLUCOSE/reference_based/ratings_train_agreement_hypothesis.txt") as f:
        cands = [line.strip() for line in f]

    with open(gts) as f:
    ## with open("/home/jaehyung/PycharmProjects/ACL2023/GLUCOSE/reference_based/ratings_train_agreement_references.txt") as f:
        refs = [line.strip() for line in f]

    # cands = ['I like you', 'I like you', 'I like you', 'I like you']
    # refs = ['I love you', 'I really like you', 'I really hate you', 'This is my phone']

    out = bart_score.score(cands, refs, batch_size=4)
    print("낮을 수록 멀다. 클수록 점수가 높은 것")
    print("결과", np.mean(out))

if __name__=='__main__':
    gts_file = args.gts_file
    res_file = args.res_file
    BARTScore_multi(gts_file,res_file)



## multi for GLUCOSE
# from tqdm import tqdm
# import json
#
# line_score_container = []
# with open('../../../../../../GLUCOSE/new_parsing/GLUCOSE_merged3.json') as f:
#     lines = f.readlines()
#
#     for line in tqdm(lines):
#         hyp = json.loads(line)['hypothesis']
#         rfs = json.loads(line)['reference']
#         multi = []
#         #cands.append(hyp)
#         #refs.append(rfs)
#         for r in rfs:
#
#             if r == hyp:
#                 continue
#
#             score = bart_score.score(hyp, r, batch_size=4)
#             multi.append(score)
#
#         last_one = np.mean(multi)
#         print(type(last_one))
#         line_score_container.append(last_one)
#
#
# with open('../../bart_score_results_114.txt', 'w', encoding='utf-8') as f:
#     for line in line_score_container:
#         f.write(str(line))
#         f.write('\n')



#print(len(line_score_container))

# # 낮을 수록 멀다.
#print("결과", np.mean(out))