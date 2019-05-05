# Huffman coding for data compression
This is an implementation of the Huffman coding algorithm. 
This project has been created to present the algorithm and the resulting compression efficiency.  

## Instalation
First you need to clone the repository. You will need git for that:
```bash
git clone https://github.com/OskarDuda/huffman-coding.git
cd huffman-coding
```

Secondly you might want to create a new virtual environment for Python and activate it, to install the 
requirements:
```bash
virtualenv venv -p python3
source venv/bin/activate
```

Finally install the requirements as follows:
```bash
pip3 install -r requirements.txt
```

## How to use
First a sample data needs to be created in 'Data' folder. This data can be either a text and saved as
'text_data.txt' or a vector of numbers and saved as 'signal_data.txt'.

To run the compression of the text data execute:  
```bash
source venv/bin/activate
python3 compress_text.py
```

To run the compression of time series data execute:  
```bash
source venv/bin/activate
python3 compress_signal.py
```
'compressed_text_data.pkl' and 'compression_dictionary.pkl' files are being created either
way, which contain pickled variables with compressed text and a dictionary to translate it
into readable values.
