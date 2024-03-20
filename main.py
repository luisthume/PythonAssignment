from football.footballetl import FootballETL


if __name__ == "__main__":
    obj = FootballETL("output.csv")
    obj.run()