# BLEU, METEOR, ROUGE, CiDEr, SPICE
python similarity.py --key_file ./test/commongen_test_eval_concepts_multi.txt \
--gts_file ./test/commongen_test_eval_reference_multi.txt \
--res_file ./test/commongen_test_eval_hypothesis_multi.txt \
--dataset_name CommonGen

# BERTScore
python BERTScore/eval_bert.py --gts_file ./test/commongen_test_eval_reference_multi.txt \
--res_file ./test/commongen_test_eval_hypothesis_multi.txt

# BARTScore
python BARTScore/eval_bart.py --gts_file ./test/commongen_test_eval_reference_multi.txt \
--res_file ./test/commongen_test_eval_hypothesis_multi.txt