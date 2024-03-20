import pandas

def remove_duplicates(df: pandas.DataFrame) -> pandas.DataFrame:
    return df[~df.index.duplicated()]

def statistic_df(df: pandas.DataFrame) -> pandas.DataFrame:
    total_goals = df["Match Id"].map(df.groupby("Match Id")["Goals Scored"].sum())
    df["Fraction of total minutes played"] = df["Minutes Played"] / 90
    df["Fraction of total goals scored"] = df["Goals Scored"] / total_goals
    df = df[["Player Id", "Match Id", "Goals Scored", "Minutes Played", "Fraction of total minutes played", "Fraction of total goals scored"]]
    df.index.names = ["Stat Id"] 
    return df

def team_df(df: pandas.DataFrame) -> pandas.DataFrame:
    return remove_duplicates(df.set_index("Team Id")["Team Name"])

def players_df(df: pandas.DataFrame) -> pandas.DataFrame:
    return remove_duplicates(df.set_index("Player Id")[["Player Name", "Team Id"]])

def match_df(df: pandas.DataFrame) -> pandas.DataFrame:
    is_home_df = df[df["is_home"] == True].groupby(["Team Id", "Match Id"], as_index=False)["Goals Scored"].sum()
    is_home_df.columns = ["Home Team Id", "Match Id", "Home Goals"]
    is_not_home_df = df[df["is_home"] == False].groupby(["Team Id", "Match Id"], as_index=False)["Goals Scored"].sum()
    is_not_home_df.columns = ["Away Team Id", "Match Id", "Away Goals"]
    is_home_df = is_home_df.set_index("Match Id").join(is_not_home_df.set_index("Match Id"))
    is_home_df.index.names = ["Match Id"] 
    return is_home_df