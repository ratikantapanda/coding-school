def is_valid_sub_sequence(arr,seq):
    arr_idx=0
    seq_idx=0
    
    while arr_idx < len(arr) and seq_idx < len(seq):
        if arr[arr_idx] == seq[seq_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(seq) -1