# THE BELOW WORK IS NOT MINE

# import re
# import sys
# import random
# from collections import defaultdict
#
# def tokenize(string):
#   return re.findall(r"\d+|[\w'’]+|\S", string)
#
# def markov(tokens, connections, length):
#   tokens.append("END$")
#   context = ["^START"]
#   connections["^START"].append(tokens[0])
#   for i in range(len(tokens) - 1):
#     context.append(tokens[i])
#     context = context[-length:]
#     connections["".join(context)].append(tokens[i+1])
#   return connections
#
# def generate(connections, length):
#   context = ["^START"]
#   tokens = []
#   while True:
#     token = random.choice(connections["".join(context)])
#     if token == "END$": break
#     tokens.append(token)
#     context.append(token)
#     context = context[-length:]
#   return tokens
#
# paragraphs = ["Hi my name is menglan, I am a comp sci major at UC Berkeley. I am"]
# paragraph = []
# for line in sys.stdin:
#   if line.strip() != "":
#     paragraph += tokenize(line)
#   elif len(paragraph):
#     paragraphs.append(paragraph)
#     paragraph = []
#
# def untokenize(tokens):
#   string = tokens[0]
#   for t in tokens[1:]:
#     no_space_before = re.search(r"[,\.!)\]:?;]", t)
#     no_space_after = string[-1] in ["(", "["]
#     if not (no_space_before or no_space_after): string += " "
#     string += t
#   return string
#
# connections = defaultdict(list)
# for p in paragraphs:
#   markov(p, connections, 2)
# for _ in range(10):
#   print(untokenize(generate(connections, 2)))