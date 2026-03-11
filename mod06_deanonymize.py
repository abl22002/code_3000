import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    merged = pd.merge(
        anon_df,
        aux_df,
        on=['age', 'gender', 'zipcode'],
        how='inner',
        suffixes=('_anon', '_aux')
    )
    match_counts = merged.groupby('anon_id').size()
    unique_ids = match_counts[match_counts == 1].index
    result = merged[merged['anon_id'].isin(unique_ids)][['anon_id', 'name']]
    result = result.rename(columns={'name': 'matched_name'})
    return result

def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    raise NotImplementedError


#  write functions in "deanonymize" script to (1) link the records in the two datasets and (2) calculate the rate at which you are successful doing so. 