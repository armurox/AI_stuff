# Analysis

## Layer 4, Head 5

The relationship identified here is that the model pays attention to the fact that verbs are modifying a noun. I.e., in the attention head, in the noun row, a similar amount of attention is given to all the verbs in the sentence. For example, in the first sentence (indicated below), in the row for "man", the same amount of attention appeared to be given to "ran" and "is". Similarly in the second sentence, in the row for "boy", both "ran" and "jumped" received a similar amount of attention.

Example Sentences:
- That man ran quickly but unfortunately is now [MASK].
- The boy ran and jumped [MASK].

## Layer 5, Head 2

Here, the model identifies the relationship between a determiner and a noun, paying a similar amount of attention to all the determiners in the word with respect to the noun. Eg: In my first setence, both "the"'s received a similar amount of attention in the fox row. In the second sentence both "a"'s received a similar amount of attention.

Example Sentences:
- The quick brown fox jumped over the [MASK].
- It is amazing that a human and a [MASK] can get along so swimmingly.

