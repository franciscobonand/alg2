CHARLIMIT = 256

def compress(bytearr):
    inpt_chars = tuple(bytearr)
    outp_chars = (inpt_chars[0], )
    key_arr_dict = {tuple(): (0, ), (inpt_chars[0], ): (1, )}
    base_ptr = 1
    limit_ptr = 1
    key_counter = [2]
    while limit_ptr < len(inpt_chars):
        # Se novo elemento não se encontra no dicionário
        if not inpt_chars[base_ptr:limit_ptr + 1] in key_arr_dict:
            prepend = key_arr_dict[inpt_chars[base_ptr:limit_ptr]]
            if sum(key_counter) == 1:
                prepend += tuple([0 for i in range(len(key_counter) - len(prepend) - 1)])
            else:
                prepend += tuple([0 for i in range(len(key_counter) - len(prepend))])
            outp_chars += prepend + (inpt_chars[limit_ptr], )
            key_arr_dict[inpt_chars[base_ptr:limit_ptr + 1]] = tuple(key_counter)

            for i in range(len(key_counter)):
                key_counter[i] += 1
                if key_counter[i] != CHARLIMIT:
                    break
                else:
                    key_counter[i] = 0
                    if i == len(key_counter) - 1:
                        key_counter.append(1)
            base_ptr = limit_ptr + 1
        limit_ptr += 1
    if inpt_chars[base_ptr:limit_ptr] in key_arr_dict and base_ptr != limit_ptr:
        prepend = tuple(key_arr_dict[inpt_chars[base_ptr:limit_ptr]])
        outp_chars += prepend + tuple([0 for i in range(len(key_counter) - len(prepend))])
    return bytes(outp_chars)

def create_compressed_file(file_cfg, bfile):
    if len(file_cfg) == 5 :
            z78_file = open(file_cfg[4]+".z78", "wb")
    else :
        f_name = file_cfg[2].split(".")[0]
        z78_file = open(f_name+".z78", "wb")

    z78_file.write(bfile)
    z78_file.close()

def uncompress(bytearr):
    inpt_chars = tuple(bytearr)
    outp_chars = (inpt_chars[0], )
    array = [tuple(), (inpt_chars[0], )]
    readPointer = 1
    numIndexBytes = 1
    nextLimit = CHARLIMIT
    isChar = False
    i = 0
    while readPointer < len(inpt_chars):
        if isChar:
            outp_chars += (inpt_chars[readPointer], )
            array.append(array[i] + (inpt_chars[readPointer], ))
            isChar = False
            readPointer += 1
            if len(array) == nextLimit + 1:
                numIndexBytes += 1
                nextLimit *= CHARLIMIT
        else:
            i = 0
            multiplier = 1
            for j in range(numIndexBytes):
                i += inpt_chars[readPointer + j] * multiplier
                multiplier *= CHARLIMIT
            if i >= len(array):
                print(i, len(array))
                print(bytes(outp_chars))
            outp_chars += array[i]
            readPointer += numIndexBytes
            isChar = True
    return bytes(outp_chars)

def create_txt_file(file_cfg, bfile):
    if len(file_cfg) == 5 :
            txt_file = open(file_cfg[4]+".txt", "wb")
    else :
        f_name = file_cfg[2].split(".")[0]
        txt_file = open(f_name+".txt", "wb")

    txt_file.write(bfile)
    txt_file.close()