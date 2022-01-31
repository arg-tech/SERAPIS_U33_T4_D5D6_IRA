import pickle
import numpy as np
import pandas as pd
import transformers as ppb
import torch

class Pproc:
    def run(self, d):
        with open(f'lr_0.76_BERT_15-03-21.pkl', 'rb') as f:
            trained_model = pickle.load(f)

        BERT_model_class, BERT_tokenizer_class, BERT_pretrained_weights = (ppb.BertModel, ppb.BertTokenizer, 'bert-base-uncased')
        BERT_tokenizer = BERT_tokenizer_class.from_pretrained(BERT_pretrained_weights)
        BERT_model = BERT_model_class.from_pretrained(BERT_pretrained_weights)

        distilBERT_model_class, distilBERT_tokenizer_class, distilBERT_pretrained_weights = (ppb.DistilBertModel, ppb.DistilBertTokenizer, 'distilbert-base-uncased')
        distilBERT_tokenizer = distilBERT_tokenizer_class.from_pretrained(distilBERT_pretrained_weights)
        distilBERT_model = distilBERT_model_class.from_pretrained(distilBERT_pretrained_weights)

        previous_results = []

        text = d
        BERT_type = 'DistilBERT'

        reset_results = 'y'

        if BERT_type == 'DistilBERT':
            model = distilBERT_model
            tokenizer = distilBERT_tokenizer
        elif BERT_type == 'BERT':
            model = BERT_model
            tokenizer = BERT_tokenizer

        untokenized_input = pd.DataFrame([text], dtype="string")
        tokenized = untokenized_input[0].apply((lambda x: tokenizer.encode(x, add_special_tokens=True)))
        max_len = 0
        for i in tokenized.values:
            padded = np.array([i + [0]*(max_len-len(i)) for i in tokenized.values])           
        attention_mask = np.where(padded != 0, 1, 0)

        attention_mask = torch.tensor(attention_mask)
        try:
            input_ids = torch.tensor(padded)
            with torch.no_grad():
                last_hidden_states = model(input_ids, attention_mask=attention_mask)
        except:
            input_ids = torch.LongTensor(padded)
            with torch.no_grad():
                last_hidden_states = model(input_ids, attention_mask=attention_mask)


        features = last_hidden_states[0][:,0,:].numpy()

        prediction = trained_model.predict_proba(features)
        true_prediction = trained_model.predict(features)

        fact_chance = prediction[0][0]
        value_chance = prediction[0][2]
        policy_chance = prediction[0][1]

        return([fact_chance, value_chance, policy_chance])
