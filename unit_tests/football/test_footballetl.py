import numpy
import pytest
from football.footballetl import FootballETL


@pytest.fixture()
def df():
    obj = FootballETL("output.csv")
    df = obj.extract()
    return df

def dtype_int(df, column):
    return df[column].dtype == int or df[column].dtype == numpy.dtype("int64")

def dtype_str(df, column):
    return df[column].dtype == str or  df[column].dtype == numpy.dtype("O")

def dtype_bool(df, column):
    return df[column].dtype == bool or df[column].dtype ==numpy.dtype("bool")

def test_player_id_exists(df):
    column = "player_id"
    assert column in df.columns

def test_player_id_dtype(df):
    column = "player_id"
    assert dtype_int(df, column)

def test_player_name_exists(df):
    column = "player_name"
    assert column in df.columns

def test_player_name_dtype(df):
    column = "player_name"
    assert dtype_str(df, column)

def test_match_id_exists(df):
    column = "match_id"
    assert column in df.columns

def test_match_id_dtype(df):
    column = "match_id"
    assert dtype_int(df, column)

def test_match_name_exists(df):
    column = "match_name"
    assert column in df.columns

def test_match_name_dtype(df):
    column = "match_name"
    assert dtype_str(df, column)

def test_goals_scored_exists(df):
    column = "goals_scored"
    assert column in df.columns

def test_match_id_dtype(df):
    column = "goals_scored"
    assert dtype_int(df, column)

def test_minutes_played_exists(df):
    column = "minutes_played"
    assert column in df.columns

def test_minutes_played_dtype(df):
    column = "minutes_played"
    assert dtype_int(df, column)

def test_team_id_exists(df):
    column = "team_id"
    assert column in df.columns

def test_team_id_dtype(df):
    column = "team_id"
    assert dtype_int(df, column)

def test_team_name_exists(df):
    column = "team_name"
    assert column in df.columns

def test_team_name_dtype(df):
    column = "team_name"
    assert dtype_str(df, column)

def test_is_home_exists(df):
    column = "is_home"
    assert column in df.columns

def test_is_home_dtype(df):
    column = "is_home"
    assert dtype_bool(df, column)

def test_null_check(df):
    for column in df.columns:
        assert df[column].notnull().all()

def test_minutes_played_range(df):
    assert df["minutes_played"].between(0, 90).any()