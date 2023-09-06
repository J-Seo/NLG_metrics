from bert_score.score import score
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--gts_file', default="../test/commongen_test_eval_hypothesis_multi.txt", type=str)
parser.add_argument('--res_file', default="../test/commongen_test_eval_reference_multi.txt", type=str)
parser.add_argument('--dataset_name', default="", type=str)
args = parser.parse_args()

def BERTScore_multi(gts,res):
    with open(res) as f:
        cands = [line.strip() for line in f]

    with open(gts) as f:
        refs = [line.strip() for line in f]

    (P, R, F), hashname = score(cands, refs, lang="en", return_hash=True)
    print(
        f"{hashname}: P={P.mean().item():.6f} R={R.mean().item():.6f} F={F.mean().item():.6f}"
    )

if __name__=='__main__':
    gts_file = args.gts_file
    res_file = args.res_file
    BERTScore_multi(gts_file,res_file)






# with multi for GLUCOSE

# hyps = []
# refs = []
# #
# #
# from tqdm import tqdm
# import json
# import numpy as np
# line_score_container = []
# with open('../../../../../../GLUCOSE/new_parsing/GLUCOSE_merged3.json') as f:
#     lines = f.readlines()
#
#     for line in tqdm(lines):
#         hyp = json.loads(line)['hypothesis']
#         rfs = json.loads(line)['reference']
#
#         try:
#             rfs.remove(hyp)
#         except:
#             print('머임')
#         hyps.append(hyp)
#         refs.append(rfs)
#
#         # multi = []
#         #cands.append(hyp)
#         #refs.append(rfs)
#         #for r in rfs:
#
#
#
#
#     (P, R, F), hashname = score(hyps, refs, lang="en", return_hash=True)
#     #multi.append(F)
#     print(F)
#     #last_one = np.mean(multi)
#     #print(last_one)
#     #line_score_container.append(last_one)
# #
# #
# with open('../../bert_score_results_114.txt', 'w', encoding='utf-8') as f:
#     for line in F:
#         f.write(str(line.item()))
#         f.write('\n')
