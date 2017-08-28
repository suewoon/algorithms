#!/usr/bin/env python3
# pytest for ocr.py

from ocr import Reader

class Test_Class(object):
    def test_read_input(self):
        reader = Reader(['I','am','a','boy','buy'])
        reader.read_input('1.0 0.0 0.0 0.0 0.0', 'first_pos_probs')
        for _list in '0.1 0.6 0.1 0.1 0.1\n0.1 0.1 0.6 0.1 0.1\n0.1 0.1 0.1 0.6 0.1\n0.2 0.2 0.2 0.2 0.2\n0.2 0.2 0.2 0.2 0.2'.split('\n'):
            reader.read_input(_list, 'cond_probs')
        for _list in '0.8 0.1 0.0 0.1 0.0\n0.1 0.7 0.0 0.2 0.0\n0.0 0.1 0.8 0.0 0.1\n0.0 0.0 0.0 0.5 0.5\n0.0 0.0 0.0 0.5 0.5'.split('\n'):
            reader.read_input(_list, 'classified_probs')
        print(reader.first_pos_probs)
        print(reader.cond_probs)
        print(reader.classified_probs)
        print(reader.words)
    
        assert 0

    def test_read_words(self):
        reader = Reader(['I','am','a','boy','buy'])
        reader.read_input('1.0 0.0 0.0 0.0 0.0', 'first_pos_probs')
        for _list in '0.1 0.6 0.1 0.1 0.1\n0.1 0.1 0.6 0.1 0.1\n0.1 0.1 0.1 0.6 0.1\n0.2 0.2 0.2 0.2 0.2\n0.2 0.2 0.2 0.2 0.2'.split('\n'):
            reader.read_input(_list, 'cond_probs')
        for _list in '0.8 0.1 0.0 0.1 0.0\n0.1 0.7 0.0 0.2 0.0\n0.0 0.1 0.8 0.0 0.1\n0.0 0.0 0.0 0.5 0.5\n0.0 0.0 0.0 0.5 0.5'.split('\n'):
            reader.read_input(_list, 'classified_probs')
       
        assert reader.read_words('4 I am a buy') == 'I am a boy'
        #assert reader.read_words('4 I I a boy') == 'I am a boy'
        assert reader.read_words('4 I am am boy') == 'I am a boy'

