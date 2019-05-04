import huffman as huf
import numpy as np
import pickle


def main():
    fname = 'signal_data.txt'
    output_fname = 'Data/compressed_text_data.pkl'
    dict_fname = 'Data/compression_dictionary.pkl'
    with open(fname) as f:
        data = f.readlines()
    data = [x.replace('\n','') for x in data]

    # In time domain
    v = huf.count_unique_values(data)
    coding_tree = huf.create_huffman_code(v)
    d = huf.tree_to_bin_dict(coding_tree)

    # occurrences dictionary sorted by the occurrences of values in data
    a = [[ch, v[ch]] for ch in v]
    a = sorted(a, key=lambda x: x[1], reverse=True)

    tmp = [int(ch) for ch in data]
    size_uncoded = (max(tmp)-min(tmp)).bit_length()*len(data)
    size_coded = sum([v[ch]*len(d[ch]) for ch in v])

    compression_level = size_coded/size_uncoded*100
    print('(TIME DOMAIN) Data is compressed to {0:.2f}% of its initial size.'.format(compression_level))

    # In frequency domain
    data_fft = list(np.abs(np.fft.fft([int(x) for x in data])))
    data_fft = [str(ch) for ch in data_fft[:int(len(data_fft)/2)]]
    v = huf.count_unique_values(data_fft)
    coding_tree = huf.create_huffman_code(v)
    d = huf.tree_to_bin_dict(coding_tree)

    # occurrences dictionary sorted by the occurrences of values in data_fft
    a = [[ch, v[ch]] for ch in v]
    a = sorted(a, key=lambda x: x[0], reverse=True)

    tmp = [int(float(ch)) for ch in data_fft]
    size_uncoded = (max(tmp)-min(tmp)).bit_length()*len(data_fft)
    size_coded = sum([v[ch]*len(d[ch]) for ch in v])

    compression_level = size_coded/size_uncoded*100
    print('(FREQUENCY DOMAIN) Data is compressed to {0:.2f}% of its initial size.'.format(compression_level))
    with open(output_fname, 'w+') as f:
        f.write()

    # In time/frequency domain
    data_spektr = list(np.abs(np.fft.fft([int(x) for x in data])))
    data_fft = [str(ch) for ch in data_fft]
    v = huf.count_unique_values(data_fft)
    coding_tree = huf.create_huffman_code(v)
    d = huf.tree_to_bin_dict(coding_tree)

    # ocurrences dictionary sorted by the occurrences of values in data_fft
    a = [[ch, v[ch]] for ch in v]
    a = sorted(a, key=lambda x: x[0], reverse=True)

    tmp = [int(float(ch)) for ch in data_fft]
    size_uncoded = (max(tmp)-min(tmp)).bit_length()*len(data_fft)
    size_coded = sum([v[ch]*len(d[ch]) for ch in v])

    compression_level = size_coded/size_uncoded*100
    print('(TIME/FREQUENCY DOMAIN) Data is compressed to {0:.2f}% of its initial size.'.format(compression_level))
    with open(output_fname, 'wb+') as f:
        pickle.dump([d[ch] for ch in data], f)

    with open(dict_fname, 'wb+') as f:
        pickle.dump(d, f)


if __name__=='__main__':
    main()
