def to_rna(dna_strand):
    dna_strand = dna_strand.upper()
    rna_strand=""
    for i in dna_strand:
        if i=="G":
          rna_strand = rna_strand + "C"
        elif i=="C":
          rna_strand = rna_strand + "G"
        elif i=="T": 
          rna_strand = rna_strand + "A"
        elif i=="A":   
          rna_strand = rna_strand + "U"
        else:
          try:  
            break  
          except ValueError: 
             print 'Invalid DNA strand.'
    print rna_strand      
    return rna_strand     

to_rna(raw_input('Enter dna_strand:'))
    
