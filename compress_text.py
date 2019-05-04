import huffman as huf
import pickle


def main():
    fname = 'Data/Text_data.txt'
    output_fname = 'Data/compressed_text_data.pkl'
    dict_fname = 'Data/compression_dictionary.pkl'
    with open(fname) as f:
        data = f.read().lower()
    data = huf.remove_punctuation(data)

    v = huf.count_unique_values(data)
    coding_tree = huf.create_huffman_code(v)
    d = huf.tree_to_bin_dict(coding_tree)

    # occurrences dictionary sorted by the occurrences of values in data
    size_noncoded = 8*len(data)
    size_coded = sum([v[ch]*len(d[ch]) for ch in v])

    compression_level = size_coded/size_noncoded*100
    print('Data is compressed to {0:.2f}% of its initial size.'.format(compression_level))
    with open(output_fname, 'wb+') as f:
        pickle.dump([d[ch] for ch in data], f)

    with open(dict_fname, 'wb+') as f:
        pickle.dump(d, f)


if __name__ == '__main__':
    main()
