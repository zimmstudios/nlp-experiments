import nltk
from nltk.book import *

# Print separator line
def print_separator_line():
  print("="*80)

# Search for given word in given text, with context
def print_concordance(text, keyword):
  print_separator_line()
  print("Searching {} for '{}'".format(text, keyword))
  text.concordance(keyword)
  print_separator_line()

# Print words that are similar to the given word in the given text
def print_similar(text, keyword):
  print_separator_line()
  print("Searching {} for words similar to '{}'".format(text, keyword))
  text.similar(keyword)
  print_separator_line()

# Print words that have a common context between the given words in the given text
def print_common_contexts(text, keywords):
  print_separator_line()
  print("Searching {} for common contexts of '{}'".format(text, keywords))
  text.common_contexts(keywords)
  print_separator_line()
  
  
# ==============================================================================

# Print some examples of concordance
print_concordance(text1, "monstrous")
print_concordance(text2, "affection")
print_concordance(text3, "lived")
print_concordance(text4, "citizen")
print_concordance(text5, "lol")
print_concordance(text6, "grail")
print_concordance(text7, "market")
print_concordance(text8, "seeking")
print_concordance(text9, "thursday")

# ==============================================================================

# Look for similar words
print_similar(text1, "monstrous")
print_similar(text2, "monstrous")
print_similar(text4, "nation")

# ==============================================================================

# Examine contexts shared by multiple words
print_common_contexts(text1, ["monstrous", "mean"])
print_common_contexts(text2, ["monstrous", "very"])
print_common_contexts(text4, ["nation", "republic"])


# **** Note ****
# I could not get dispersion_plot() to work because I had a problem installing matplotlib.
# I'll try again next time it comes up in the book.
# **************

# ==============================================================================
# 1.4 Counting Vocabulary
# ==============================================================================

print_separator_line()

print("Length of {}: {}".format(text1, len(text1)))
print("Size of vobaluary in {}: {}".format(text1, len(set(text1))))

# Determine the lexical diversity of the text.
# (i.e. what percentage of the text is unique words)
def lexical_diversity(text):
  return len(set(text)) / len(text)

# Get a percentage value for the given count and total
def percentage(count, total):
  return 100 * count / total

print("Lexical diversity of {}: {}".format(text1, lexical_diversity(text1)))
print("Number of times the word 'lol' appears in {}: {}".format(text5, text5.count("lol")))
print("Percentage of {} that is the word 'lol': {}".format(text5, percentage(text5.count("the"), len(text5))))

print_separator_line()

# ==============================================================================
# 2 Lists
# ==============================================================================

print_separator_line()

print("Sentence 1: {}".format(sent1))
print("Sentence 4 + 5: {}".format(sent4 + sent5))
print("Sentence 9 sorted: {}".format(sorted(sent9)))

print_separator_line()

my_sentence = ['Python', 'lists', 'are', 'easy', '!']
print("my_sentence: {}".format(my_sentence))
print("my_sentence length: {}".format(len(my_sentence)))
print("my_sentence sorted: {}".format(sorted(my_sentence)))
print("my_sentence lexical diversity: {}".format(lexical_diversity(my_sentence)))
print("my_sentence[3]: {}".format(my_sentence[3]))
print("my_sentence[:2]: {}".format(my_sentence[:2]))


# **** Note ****
# I'm skipping the rest of section 2. There's no reason for me to keep writing all these
# list and string operations I already know how to do.
# **************

print_separator_line()

# ==============================================================================
# 3 Simple Statistics
# ==============================================================================

# ==============================================================================
# 3.1 Frequency Distributions
# ==============================================================================

print_separator_line()

fdist1 = FreqDist(text1)
print("Frequency distribution of {}".format(text1))
print(fdist1)
print("Most common 50 tokens in {}".format(text1))
print(fdist1.most_common(50))

# This won't work until I can get matplotlib to work
# fdist1.plot(50, cumulative=True)

print ("Hapaxes in {} (i.e. tokens that occur only once.".format(text1))
print(fdist1.hapaxes())

print_separator_line()

# ==============================================================================
# 3.2 Fine-grained selection of words
# ==============================================================================

print_separator_line()

# Print all tokens in the given text that are longer than the given length
def print_words_over_length(text, length):
  print("Tokens over length {} in {}".format(length, text))
  long_words = [word for word in set(text) if len(word) > length]
  print(sorted(long_words))

print_words_over_length(text1, 15)
print_words_over_length(text4, 15)
print_words_over_length(text5, 15)

# Print all tokens in the given text that are longer than the given length
#   and occur more often than the given frequency
def print_words_over_length_and_frequency(text, length, frequency):
  print("Tokens over length {} in {} that occur more than {} times.".format(length, text, frequency))
  fdist = FreqDist(text)
  long_words = [word for word in set(text) if len(word) > length and fdist[word] > frequency]
  print(sorted(long_words))

print_words_over_length_and_frequency(text4, 10, 10)
print_words_over_length_and_frequency(text5, 7, 7)

print_separator_line()

# ==============================================================================
# 3.3 Collocations and Bigrams
# ==============================================================================

print_separator_line()

# Bigrams = word pairs
print(list(bigrams(['more', 'is', 'said', 'than', 'done'])))

# Collocations = words that occur together unusually often
def print_collocations(text):
  print("Collocations in {}".format(text))
  print(text.collocations())

print_collocations(text4)
print_collocations(text5)
print_collocations(text8)

print_separator_line()

# ==============================================================================
# 3.4 Counting other things
# ==============================================================================

print_separator_line()

word_lengths = [len(word) for word in text1]
print(word_lengths[:50])
fdist = FreqDist(word_lengths)
print("Frequency distribution of word lengths:")
print(fdist1)

print("Most common word lengths:")
print(fdist.most_common())

print("Most common word length:")
most_common_word_length = fdist.max()
print(most_common_word_length)

print("Number of words of length {}:".format(most_common_word_length))
print(fdist[most_common_word_length])

print("Frequency of words of length {}:".format(most_common_word_length))
print(fdist.freq(most_common_word_length))



