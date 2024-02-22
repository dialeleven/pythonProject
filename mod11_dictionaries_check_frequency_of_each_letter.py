name = 'Jimmy Johnson'

letter_freq_dict = {}

for i in name:
    if i not in letter_freq_dict:
        letter_freq_dict[i] = 1
    else:
        letter_freq_dict[i] += 1
    print(i, end=' ')

print('\n', letter_freq_dict)