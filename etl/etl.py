from abc import ABC, abstractmethod
import logging
import pandas
import time
import os

class ETL(ABC):

    _root_data_dir = "data/"
    _output = {}

    @property
    @abstractmethod
    def input_file_name(self):
        pass

    def input_data_path(self) -> str:
        return os.path.join(
        self._root_data_dir,
        "input",
        self.input_file_name,
    )

    def output_data_path(self, output_file_name: str) -> str:
        return os.path.join(
        self._root_data_dir,
        "output",
        output_file_name,
    )

    def extract(self) -> pandas.DataFrame:
        self._df = pandas.read_csv(self.input_data_path())
        return self._df

    @abstractmethod
    def transform(self):
        pass

    def load(self) -> bool:
        sucefull = True
        try:
            for output_file_name, output_df in self._output.items():
                logging.debug(f"Saving {output_df} as {output_file_name}...")
                output_df.to_csv(self.output_data_path(output_file_name))
        except Exception as e:
            sucefull = False
            logging.error(e)
        return sucefull

    def run(self):
        timer = time.time()
        self.extract()
        logging.info(f"Extract time: {time.time() - timer}")
        timer = time.time()
        self.transform()
        logging.info(f"Transform time: {time.time() - timer}")
        timer = time.time()
        self.load()
        logging.info(f"Load time: {time.time() - timer}")