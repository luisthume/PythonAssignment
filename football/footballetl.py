import pandas
from etl.etl import ETL
from football.utils import team_df, players_df, statistic_df, match_df
import logging

class FootballETL(ETL):

    def __init__(self, input_file_name):
        self._input_file_name = input_file_name
        logging.basicConfig(
            filename= "FootballETL.log",
            level=logging.INFO,
            format= "%(asctime)s.%(msecs)03d %(levelname)s - %(funcName)s: %(message)s",
            datefmt= "%Y-%m-%d %H:%M:%S",
        )

    @property
    def input_file_name(self):
        return self._input_file_name

    def transform(self) -> pandas.DataFrame:
        df = self._df.rename({
            "player_id": "Player Id",
            "player_name": "Player Name",
            "match_id": "Match Id",
            "goals_scored": "Goals Scored",
            "minutes_played": "Minutes Played",
            "team_id": "Team Id",
            "team_name": "Team Name"
        }, axis=1)
        self._output["team.csv"] = team_df(df)
        self._output["players.csv"] = players_df(df)
        self._output["statistic.csv"] = statistic_df(df)
        self._output["match.csv"] = match_df(df)
        del self._df
        return self._output