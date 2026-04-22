
from collections import defaultdict
from itertools import product


rna_codon_table = {
    'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


dna_codon_table = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def readFASTA(content):
    sequences = {}
    seq_id = ''
    
    for line in content:
        if line.startswith('>'):
            seq_id = line[1:]
            sequences[seq_id] = ''
        else:
            sequences[seq_id] += line.strip()
    
    return sequences

codon_count = {
    'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2,
    'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
    'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6,
    'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2,
    'Stop': 3
}


aa_mass = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}


def rev_comp(s):
    """返回 DNA 序列的反向互补链"""
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(comp[c] for c in reversed(s))


kmers = [''.join(p) for p in product('ACGT', repeat=4)]

def parse_newick(s):
    stack = []
    graph = defaultdict(list)
    node_id = 0
    name_to_id = {}

    i = 0
    while i < len(s):
        if s[i] == '(':
            stack.append('(')
            i += 1

        elif s[i] == ',':
            i += 1

        elif s[i] == ')':
            children = []
            while stack and stack[-1] != '(':
                children.append(stack.pop())
            if stack:
                stack.pop()  # remove '('

            # 创建一个内部节点
            current = node_id
            node_id += 1

            # 连边（无向）
            for child in children:
                graph[current].append(child)
                graph[child].append(current)

            stack.append(current)
            i += 1

            # 处理 ) 后面的名字（可能存在）
            name = ''
            while i < len(s) and (s[i].isalnum() or s[i] == '_'):
                name += s[i]
                i += 1
            if name:
                name_to_id[name] = current
            
            # 跳过冒号和数字（分支长度）
            if i < len(s) and s[i] == ':':
                i += 1
                while i < len(s) and (s[i].isdigit() or s[i] == '.'):
                    i += 1

        elif s[i] == ';':
            i += 1

        elif s[i] in ' \t\n':
            i += 1

        else:
            # 读取名字
            name = ''
            while i < len(s) and (s[i].isalnum() or s[i] == '_'):
                name += s[i]
                i += 1

            if name:
                current = node_id
                node_id += 1

                name_to_id[name] = current
                stack.append(current)
            
            # 跳过冒号和数字（分支长度）
            if i < len(s) and s[i] == ':':
                i += 1
                while i < len(s) and (s[i].isdigit() or s[i] == '.'):
                    i += 1

    return graph, name_to_id