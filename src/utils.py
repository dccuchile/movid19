import csv
import re
import numpy as np
import sys
from gensim.models.keyedvectors import KeyedVectors
from numpy.linalg import norm
from gensim.models.wrappers import FastText
import torch
from torch.nn.utils.rnn import pad_sequence

def date_to_int(date_text):
    date_text = re.sub('(-|/)','',date_text)
    date = date_text.split()[0]
    return int(date)

def read_movid_file(infile_name, text_field,
              should_ignore=['NA'], 
              after=None,
              id_field = 'pob_id', 
              date_field = 'fecha_obs'):
    
    text_dict = {}
    with open(infile_name) as infile:
        reader = csv.DictReader(infile)
        c = 0
        for row in reader:
            k = row[id_field]
            d = date_to_int(row[date_field])
            if after and d <= after:
                continue
            text = row[text_field]
            if text not in should_ignore:
                if (k,d) in text_dict:
                    k = k + f'_{c}'
                    c += 1
                text_dict[(k,d)] = text
    return text_dict


letters = set('aáeéoóíúiuüàèìòùbcdfghjklmnñopqrstvwxyz')
numbers = set('1234567890')

def clean_text(text):
    char_tokens = []
    text = text.lower().strip()
    for char in text:
        if char in (letters | numbers):
            to_append = char
        else:
            to_append = ' '
        char_tokens.append(to_append)
    text = re.sub(' +',' ',''.join(char_tokens)).strip()
    return text

def tokenize(text):
    text = clean_text(text)
    return text.split()

def delete_ignored_tokens(tokens, ignore_tokens=[]):
    new_tokens = [token for token in tokens if token not in ignore_tokens]
    return new_tokens

def load_we(wordvectors_file, mode, limit=100000):
    if mode == 'bin':
        wordvectors = FastText.load_fasttext_format(wordvectors_file)
    elif mode == 'vec':
        wordvectors = KeyedVectors.load_word2vec_format(wordvectors_file + '.vec', limit=limit)
    else:
        print('mode debe ser vec o bin')
    return wordvectors

def to_vector(text, we, verbose=True):
    tokens = tokenize(text)
    tokens = delete_ignored_tokens(tokens)
    vec = np.zeros(300)
    n = 0
    for word in tokens:
        # si la palabra está la acumulamos
        if word in we:
            vec += we[word]
            n += 1
    if norm(vec) == 0 or n == 0:
        if verbose:
            print('not possible to create vector for:', tokens)
        return vec
    else:
        vec = vec / n
        return vec / norm(vec)
    
def generate_emb_dict(text_dict, wordvectors, verbose=True):
    emb_dict = {}
    for id_t in text_dict:
        emb_dict[id_t] = to_vector(text_dict[id_t], wordvectors, verbose)
    return emb_dict
    
def to_vector_bert_model(text, tokenizer, model, verbose=True):
    text = clean_text(text)
    text = '[CLS] ' + text + ' [SEP]'
    tokens = tokenizer.tokenize(text)
    indexed_tokens = tokenizer.convert_tokens_to_ids(tokens)
    tokens_tensor = torch.tensor([indexed_tokens]) # Batch size 1
    outputs = model(tokens_tensor)
    hidden_size = outputs[0].size()[-1]
    vectors = outputs[0].view(-1,768)
    vec = torch.mean(vectors, dim=0)
    return vec / torch.norm(vec)

def prepare_text_for_bert(text):
    text = clean_text(text)
    text = '[CLS] ' + text + ' [SEP]'
    return text

def to_vector_batch(list_of_texts, tokenizer, model, batch_size=None, device='cpu', verbose=True):
    if device:
        model = model.to(device)
    N = len(list_of_texts)
    if not batch_size:
        batch_size = N
    b, i = 0, 0
    embs_list = []
    while i < N:
        j = i + batch_size
        if j > N:
            j = N
        if verbose:
            info = f'\rbatch:{b}, examples:{j}/{N}'
            sys.stdout.write(info)
            #print(info)
            b += 1
        current_list = list_of_texts[i:j]
        token_ids = tokenizer.batch_encode_plus(current_list, pad_to_max_length=True)['input_ids']
        tensor_token_ids = [torch.tensor(x) for x in token_ids]
        model_input = pad_sequence(tensor_token_ids, batch_first=True, padding_value=1)
        if device:
            model_input = model_input.to(device)
        output_embs = model(model_input)[0].data
        embeddings = output_embs.mean(dim=1)
        embeddings = embeddings.to('cpu')
        embs_list.append(embeddings)
        ### TENGO QUE ENTENDER POR QUÉ ESTÁ LIKEANDO MEMORIA
        ### POR AHORA EL del LO SOLUCIONA
        del output_embs
        del model_input
        i = j # next batch
    embs = torch.cat(embs_list)
    if verbose:
        print('\ndone')
    return embs

def generate_bert_emb_dict(text_dict, tokenizer, model, batch_size=50, device='cpu'
                             verbose=True, debug=False, debug_N=200):
    list_of_keys = list(text_dict.keys())
    list_of_text = [prepare_text_for_bert(text_dict[k]) for k in list_of_keys]
    if debug:
        list_of_keys = list_of_keys[:debug_N]
        list_of_text = list_of_text[:debug_N]
    embs = to_vector_batch(list_of_text, tokenizer, model, batch_size=batch_size, device=device)
    emb_dict = {}
    for emb, id_t in zip(embs, list_of_keys):
        emb_dict[id_t] = emb
    return emb_dict

def out_emb_line(emb):
    if type(emb) == torch.Tensor:
        line = [str(n.item()) for n in emb]
    else:
        line = [str(n) for n in emb]
    line = '\t'.join(line) + '\n'
    return line

def out_text_line(text):
    line = text
    if text.strip() == '':
        line += 'NONE'
    line += '\n'
    return line

def save_emb_and_meta(text_dict, emb_dict, outfilename_we, outfilename_metadata):
    with open(outfilename_we,'w') as outfile_we, open(outfilename_metadata,'w') as outfile_metadata:
        for id_t in emb_dict:
            text = text_dict[id_t]
            text_line = out_text_line(text)
            outfile_metadata.write(text_line)

            emb = emb_dict[id_t]
            emb_line = out_emb_line(emb)
            outfile_we.write(emb_line)