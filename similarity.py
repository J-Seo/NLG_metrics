import sys
sys.path.append('./BLEU')
sys.path.append('./METEOR')
sys.path.append('./ROUGE')
sys.path.append('./CIDEr')
sys.path.append('./SPICE')

print(sys)
from bleu import Bleu
from meteor import Meteor
from rouge import Rouge
from cider import Cider
from spice import Spice
import spacy
import sys
import codecs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--key_file', default="", type=str)
parser.add_argument('--gts_file', default="", type=str)
parser.add_argument('--res_file', default="", type=str)
parser.add_argument('--dataset_name', default="", type=str)

args = parser.parse_args()

nlp = spacy.load("en_core_web_sm")
nlp.select_pipes(disable=['tok2vec', 'parser', 'attribute_ruler', 'lemmatizer', 'ner'])

#nlp.pipeline = [('tagger', nlp.tagger)]
#nlp.pipeline = [('tagger', spacy.pipeline.tagger)]

def tokenize(dict):
    for key in dict:
        new_sentence_list = []
        for sentence in dict[key]:
            a = ''
            for token in nlp(str(sentence)):
                a += token.text
                a += ' '
            new_sentence_list.append(a.rstrip())
        dict[key] = new_sentence_list

    return dict


def evaluator(gts, res):
    eval = {}
    # =================================================
    # Set up scorers
    # =================================================
    print('tokenization...')
    # Todo: use Spacy for tokenization
    gts = tokenize(gts)
    res = tokenize(res)

    print(gts)
    print(res)

    # =================================================
    # Set up scorers
    # =================================================
    print('setting up scorers...')
    scorers = [
        (Bleu(4), ["Bleu_1", "Bleu_2", "Bleu_3", "Bleu_4"]),
        (Meteor(), "METEOR"),
        (Rouge(), "ROUGE_L"),
        (Cider(), "CIDEr"),
        (Spice(), "SPICE")
    ]

    # =================================================
    # Compute scores
    # =================================================
    for scorer, method in scorers:
        print('computing %s score...' % (scorer.method()))
        score, scores = scorer.compute_score(gts, res)

        if scorer.method() == 'Bleu':
            for i, s_b in enumerate(scores):
                with open('result/bleu_score_{}.txt'.format(dataset_name,i+1), 'w', encoding='utf-8') as f:
                    for s in s_b:
                        f.write(str(s) + '\n')

        if scorer.method() == 'METEOR':
            with open('result/meteor_score.txt'.format(dataset_name), 'w', encoding='utf-8') as f:
                for s in scores:
                    f.write(str(s) + '\n')

        if scorer.method() == 'Rouge':
            with open('result/rouge_score.txt'.format(dataset_name), 'w', encoding='utf-8') as f:
                for s in scores:
                    f.write(str(s) + '\n')

        if scorer.method() == 'CIDEr':
            with open('result/cider_score.txt'.format(dataset_name), 'w', encoding='utf-8') as f:
                for s in scores:
                    f.write(str(s) + '\n')

        if scorer.method() == 'SPICE':
            with open('result/spice_score.txt'.format(dataset_name), 'w', encoding='utf-8') as f:
                for s in scores:
                    f.write(str(s['All']['f']) + '\n')


        if type(method) == list:
            for sc, scs, m in zip(score, scores, method):
                eval[m] = sc
                print("%s: %0.3f" % (m, sc))
        else:
            eval[method] = score
            print("%s: %0.3f" % (method, score))

if __name__=='__main__':

    key_file = args.key_file
    gts_file = args.gts_file
    res_file = args.res_file
    dataset_name = args.dataset_name

    gts = {}
    res = {}

    with codecs.open(key_file, encoding='utf-8') as f:
        key_lines = f.readlines()
        # key_lines = [line.decode('utf-8') for line in f.readlines()]
    with codecs.open(gts_file, encoding='utf-8') as f:
        gts_lines = f.readlines()
        # gts_lines = [line.decode('utf-8') for line in f.readlines()]
    with codecs.open(res_file, encoding='utf-8') as f:
        res_lines = f.readlines()
        # res_lines = [line.decode('utf-8') for line in f.readlines()]

    for key_line, gts_line, res_line in zip(key_lines, gts_lines, res_lines):
        key = '#'.join(key_line.rstrip('\n').split(' '))
        if key not in gts:
            gts[key] = []
            gts[key].append(gts_line.rstrip('\n'))
            res[key] = []
            res[key].append(res_line.rstrip('\n'))
        else:
            gts[key].append(gts_line.rstrip('\n'))

    evaluator(gts, res)

    # gts = {"cat#dog#boy": ["The dog is the boy's cat.", "The dog eats the cat of the boy."],
    #        "apple#tree#boy": ["A boy is picking apples from trees."]}
    # res = {"cat#dog#boy": ["The dog is the boy's cat."],
    #        "apple#tree#boy": ["A boy is picking apples from trees and put them into bags."]}
    # evaluator(gts, res)
    #
    # gts = {"cat#dog#boy": ["The dog is the boy's cat.", "The dog eats the cat of the boy."],
    #        "apple#tree#boy": ["A boy is picking apples from trees."]}
    # res = {"cat#dog#boy": ["The dog is the boy's cat."],
    #        "apple#tree#boy": ["A boy is picking apples trees and put them into bags"]}
    # evaluator(gts, res)
