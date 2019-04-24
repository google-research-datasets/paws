## Raw Sentences and Mappings for PAWS-Wiki

Here we provide raw source sentences for `PAWS-Wiki` before any human
judgements, and their mappings to final released pairs.

*   [`PAWS-Wiki Raw and Mappings`](https://storage.googleapis.com/paws/english/wiki_raw_and_mapping.tar.gz)

This package has the following files:

*   `input_swap_wiki_50k.tsv`: The 50,000 sentence pairs generated from the swap
    method. Each row has three values.
    *   `id`: A unique ID for each pair, e.g. `swap_00001`
    *   `sentence1`: Source sentences from Wikipedia
    *   `sentence2`: Sentences generated from word swapping without any human
        corrections
*   `input_backtransl_wiki_with_swap_id.tsv`: The 26,893 pairs generated from
    the back translation method. Each row has four values.
    *   `id`: A unique ID for each pair, e.g. `backtransl_set1_14693`
    *   `sentence1`: Source sentences for back translation
    *   `sentence2`: Back-translated results from `sentence1`
    *   `swap_id`: Mappings from `sentence1` to sentences from the swap method,
        in the format of `swap_id_[1|2]`. E.g. `swap_00258_1` indicates that the
        sentence is picked from the first sentence of the pair with ID
        `swap_00258` in the file `input_swap_wiki_50k.tsv`.
*   `labeled_final_mapping/[train|dev|test].tsv`: Mappings between inputs above
    and final released pairs in
    [`PAWS-Wiki Labeled (Final)`](https://storage.googleapis.com/paws/english/paws_wiki_labeled_final.tar.gz).
    Each row has three values.
    *   `id`: A unique id for each final released pair
    *   `mapping1`: Mappings for the first sentence in final pairs, in the
        format of `swap_id_[1|2]` or `backtransl_id_2`, meaning the sentence is
        sourced from swap inputs (the first or the second sentence) or back
        translation inputs (always the second sentence).
    *   `mapping2`: Mappings for the second sentnece, in the same format as
        above.
*   `labeled_swap_mapping/train.tsv`: Mappings between swap inputs and released
    pairs in
    [`PAWS-Wiki Labeled (Swap-only)`](https://storage.googleapis.com/paws/english/paws_wiki_labeled_swap.tar.gz).
    It has the same format as mappings above, but all sentences are sourced only
    from swap inputs.
