def complement_codon(input_codon):
    answer = is_codon_correct(input_codon)
    if answer is True:
       print('Things working nicely')
    else:
        print('Codon has bad characters')
        return None
        
    base_complements = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C',
            '?': '?',
    }

    first_base = input_codon[0]
    second_base = input_codon[1]
    third_base = input_codon[2]
        
    first_complemented_base = base_complements[first_base]
    second_complemented_base = base_complements[second_base]
    third_complemented_base = base_complements[third_base]

    complemented_codon = first_complemented_base + second_complemented_base + third_complemented_base

    return complemented_codon

def is_codon_correct(input_codon):    
    allowed_characters = ['A','T','C','G','?','N','_']
    
    for base in input_codon:
       if base.upper() in allowed_characters:
           continue
       else:
          print('Your codon is bad')
          return False
    return True
 