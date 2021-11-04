def convertToNAN(row, columns, delim, value):
    """
        returns a new row
        Replaces all values referenced by `delim` to values referenced by `value`
        
        
        -columns: list-like, 
                  DataFrame columns to iterate through
                  
        -row:     Dictionary/pd.Series,
                  key:(column in DataFrame.columns) pairs of data
                  
        -delim:   str,
                  what to change
                  
        -value:   Change to
        
        
        example:
        df.apply(lambda row: convertToX(row, df.columns, "?", numpy.NaN), axis="columns")
        
    """
    for column in columns:
        #Replace all entries with ? as np.NaN
        try:#If delim is an iterable iterate through and remove match with values in delim
            for deli in delim:
                if (row[column] == deli):
                    row[column] = value;
        except:#else
            if (row[column] == delim):
                row[column] = value;
    return row;