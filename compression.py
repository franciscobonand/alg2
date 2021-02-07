from io import StringIO
import ctrie

# standard int size
INTSIZE = 3
# standard char size
CHARSIZE = 1

def compress(input_file_name, output_file_name):
    inpt_file = open(input_file_name, "r")
    text = inpt_file.read()
    inpt_file.close()

    out_file = open(output_file_name, 'wb')

    trie = ctrie.CTrie('', numeric_value=0)
    wrd_chain = ''
    index = 1
    for char in text:
        value = trie.contains(wrd_chain + char)
        if value != -1:
            wrd_chain += char
        else:
            wrd_chain_index = trie.contains(wrd_chain)
            trie.add(wrd_chain + char, index)
            out_file.write(wrd_chain_index.to_bytes(INTSIZE, "big"))
            out_file.write(ord(char).to_bytes(CHARSIZE, "big"))
            index += 1
            wrd_chain = ''

    out_file.write((trie.contains(wrd_chain)).to_bytes(INTSIZE, "big"))

    out_file.close()

def decompress(input_file_name):
    trie_elem = ['']
    decoded = ''
    inpt_file = open(input_file_name, 'rb')

    while True :
        index = inpt_file.read(INTSIZE)
        char = inpt_file.read(CHARSIZE)

        if index == b'': # runs until EOF
            break
        index = int.from_bytes(index, "big")
        if char == b'':
            char = ''
        else:
            char = chr(int.from_bytes(char, "big"))
        
        wrd_chain = trie_elem[index]
        decoded += wrd_chain + char
        trie_elem += [wrd_chain + char]
    
    inpt_file.close()
    return decoded


def create_compressed_file(file_cfg, bfile):
    if len(file_cfg) == 5 :
            z78_file = open(file_cfg[4]+".z78", "wb")
    else :
        f_name = file_cfg[2].split(".")[0]
        z78_file = open(f_name+".z78", "wb")

    z78_file.write(bfile)
    z78_file.close()

def create_txt_file(file_name, content):
    txt_file = open(file_name, "w")
    txt_file.write(content)
    txt_file.close()