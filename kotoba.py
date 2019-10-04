#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from jamdict import Jamdict
import random
import copy
from puchikarui import puchikarui
import logging
puchikarui.getLogger().setLevel(logging.ERROR)

def flatten(nested):
    output = []
    get = nested[:]
    return recur(get, output)

def recur(nested, output):
    nested = queue_ify(nested)
    while nested:
        cur = nested.pop()
        if isinstance(cur, (list, tuple)):
            recur(cur, output)
        else:
            output.append(cur)

    return output

def queue_ify(input_stack):
    output = []
    while input_stack:
        output.append(input_stack.pop())
    return output

def shuffle(arr):
    for i in range(len(arr)-1):
        a = random.randint(0, len(arr)-1)
        temp = arr[i]
        arr[i] = arr[a]
        arr[a] = temp

class Kotoba():
    def __init__(self):
        self.jmd = Jamdict() 
        self.moras = ['あ','い','う','え','お',
                'か','き','く','け','こ',
                'さ','し','す','せ','そ',
                'た','ち','つ','て','と',
                'な','に','ぬ','ね','の',
                'は','ひ','ふ','へ','ほ',
                'ま','み','む','め','も',
                'ら','り','る','れ','ろ',
                'や','ゆ','よ','わ','ん']
        
        self.special_cases = {'か':['が'], 'き':['ぎ'], 'け':['げ'], 'こ':['ご'], 
                'さ':['ざ'],'し':['じ'],'す':['ず'],'せ':['ぜ'],'そ':['ぞ'],
                'た':['だ'],'ち':['ぢ'],'つ':['づ','っ'],'て':['で'],'と':['ど'],
                'は':['ば','ぱ'],'ひ':['び','ぴ'],'ふ':['ぶ','ぷ'],'へ':['べ','ぺ'],'ほ':['ぼ','ぽ'],
                'や':['ゃ'],'ゆ':['ゅ'],'よ':['ょ'],
                }

    def find_kotoba(self, word, hidden):
        temp = set()
        hidden_set = set()
        for m in word:
            temp.add(m)
        for m in hidden:
            hidden_set.add(m)
        if not temp.issubset(hidden):
            return None
        test = self.jmd.lookup(word)
        return test.entries

    def generate_moras(self):
        current_set = []
        all_set = []
        hidden = []

        all_set.append([self.moras[2]])
        current_set.append(self.moras[2])
        current_set.append(self.moras[17])
        tsu = [self.moras[17]]
        for mora in self.special_cases[self.moras[17]]:
            tsu.append(mora)
        all_set.append(tsu)

        while len(current_set) < 9:
            cur = self.moras[random.randint(0, len(self.moras)-1)]
            if cur not in current_set:
                current_set.append(cur)
                hidden.append(cur)
                if cur in self.special_cases:
                    temp = [cur]
                    for char in self.special_cases[cur]:
                        temp.append(char)
                        hidden.append(char)
                    all_set.append(temp)
                else:
                    all_set.append([cur])
        dup = copy.deepcopy(all_set)
        str_display = ''.join(flatten(dup))
        shuffle(all_set)

        return (str_display, current_set, all_set, hidden)

    def display_result(self, word, entry, max_score):
        print("Correct!")
        print("Current Score: " + str(max_score))
        print(entry.entries)

    def start_session(self):
        session_started = True
        mora_list = self.generate_moras()
        guesses = set()
        lives_left = 3
        cur_score = 0
        max_score = 0

        while session_started:
            print('The letters are: ' + mora_list[0])
            cmd = input('Create a word: ')
            if cmd not in guesses:
                check = self.jmd.lookup(cmd)
                if check != "Found nothing":
                    cur_score += 1
                    max_score += 1
                    self.display_result(cmd, check, max_score)
                else:
                    lives_left -= 1
            else:
                print("You have already used " + cmd)
            #reset for a new mora list
            if cur_score >= 5:
                cmd = input('Generate a new list?')
                if cmd == 'y':
                    cur_score = 0
                    mora_list = self.generate_moras()

    def start_game(self):
        print('Hello from start')
        self.start_session()

