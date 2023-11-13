## Company: AI Camp/ Rakugo Media
## Authors: Elian Ahmar, Lucas, Cash, Nikhil

## This file contains all of the testing we are going to do to validate our code

import os
from datetime import datetime
import unittest
import main
import argparse

class Test_TestCodebase(unittest.TestCase):
    # Lucas, Cash, Nikhil
    @staticmethod
    def test_main(folder_path):
        file_paths = [] #

        for _, _, file_names in os.walk(folder_path):
            for file_name in file_names:
                if file_name.lower().endswith(".pdf") or file_name.lower().endswith(".docx"):
                    file_paths.append(file_name)

        output_file = open("output.txt", "a", encoding="utf-8") # use "a" to append, "w" to write

        output_file.write(str(datetime.now())) # will vary timezone btw

        print("# of file_paths:", len(file_paths))
        print(file_paths)
        for file_path in file_paths:
            print("file path:", file_path)
            output_file.write("\n\n\n\n" + file_path)
            rel_file_path = os.path.join(folder_path, file_path)
            output_file.write("\n\n" + main.main(rel_file_path))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('test_files_dir', type=str)
    args = parser.parse_args()
    Test_TestCodebase.test_main(args.test_files_dir)
