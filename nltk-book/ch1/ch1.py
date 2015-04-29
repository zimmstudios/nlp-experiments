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


# ****Note to self****
# I left off here at dispersion_plot(). I had a problem installing matplotlib.
# ********************


