import re 
import pandas as pd

def remove_symbols(reviews):
    replace_with_space = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)|(\n*\n)|(\r*\n)|(#&)")
    reviews = [replace_with_space.sub(" ", i.lower()) for i in reviews]
    
    return reviews

def remove_punctuation(reviews):
    remove = re.compile("[.;:!\'?,\"()\[\]]")
    reviews = [remove.sub("", i.lower() ) for i in reviews]
    
    return reviews

def clean_text(df, text_columns):
    """Makes all words lowercase and removes punctuation but will replace set of symbols with a space so we don't join two separate words together. """
    
    for text_column in text_columns:
        df[text_column] = remove_symbols(df[text_column])
        df[text_column] = remove_punctuation(df[text_column])
    
    return df

def swap_columns(df, c1, c2):
    df['temp'] = df[c1]
    df[c1] = df[c2]
    df[c2] = df['temp']
    df.drop(columns=['temp'], inplace=True)
    df.rename(columns={c1:c2,c2:c1},inplace=True)
    return df


def reassign_dates(dataframe, column_name, original_value, new_value, yearfirst):
    """ Used to locate and re-assign specific row values for datetime objects.
    Yearfirst should be a 0 (no) or 1 (yes) integer value"""
        
    df=dataframe    
    
    # Convert to string 
    df[column_name] = df[column_name].astype('str')

    # Re-assign date
    df.loc[df[column_name]==original_value, column_name] = new_value

    # Convert back to datetime object and check value_counts
    if yearfirst==0:
        df[column_name] = pd.to_datetime(df[column_name],yearfirst=False)
        return df
        
    elif yearfirst==1:
        df[column_name] = pd.to_datetime(df[column_name],yearfirst=True)
        return df
    
    else:
        return("yearfirst must be 0 or 1 integer value.")  
    
