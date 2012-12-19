#!/usr/bin/python
## Starts the benchmark suite.

import getopt, sys, time, subprocess

OPTIONS = ""
LONG_OPTIONS = [ "help", "fibs=", "quicksort=" ]
WARMUP_ROUNDS = 2
TEST_ROUNDS = 10

JS_RUN = "node"
HS_RUN = "runhaskell"
BIN_RUN = "./execbin.sh"
PYTHON_RUN = "python"
JAVA_RUN = "java"
JAVA_OPT = "-cp"
RUBY_RUN = "ruby"
BASH_RUN = "bash"

FIBS_DIR = "fibs/"
QUICKSORT_DIR = "quicksort/"

FIBS_ITER = 35
QUICKSORT_FILE = "data/rand1000000.data"

RUN_CMDS = {
    "js" : [ JS_RUN ],
    "hs" : [ HS_RUN ],
    "hsc" : [ BIN_RUN ],
    "py" : [ PYTHON_RUN ],
    "cy" : [ PYTHON_RUN ],
    "java" : [ JAVA_RUN, JAVA_OPT ],
    "rb" : [ RUBY_RUN ],
    "bash" : [ BASH_RUN ],
    "c" : [ BIN_RUN ]
    }
RUN_LOCATIONS = {
    "fibs" : {
        "js" : [ FIBS_DIR + "js/fibs.js" ],
        "hs" : [ FIBS_DIR + "hs/fibs.hs" ],
        "hsc" : [ FIBS_DIR + "hs/fibs" ],
        "py" : [ FIBS_DIR + "py/fibs.py" ],
        "cy" : [ FIBS_DIR + "cy/run.py" ],
        "java" : [ FIBS_DIR + "java", "Fibs" ],
        "rb" : [ FIBS_DIR + "rb/fibs.rb" ],
        "bash" : [ FIBS_DIR + "bash/fibs.sh" ],
        "c" : [ FIBS_DIR + "c/fibs.out" ]
        },
    "quicksort" : {
        "py" : [ QUICKSORT_DIR + "py/quicksort.py" ]
        }
    }
RUN_OPTIONS = {
    "fibs" : str(FIBS_ITER),
    "quicksort" : QUICKSORT_FILE
    }

class Timer:
    """Class to time running calculations."""
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start

def run(test, language, options):
    """Runs TEST using LANGUAGE, times the result, and returns the time
    used in such a calculation."""
    # TODO : check for languages/tests not supported
    run_cmd = RUN_CMDS[language]
    run_location = RUN_LOCATIONS[test][language]
    if options:
        run_option = options
    else:
        run_option = RUN_OPTIONS[test]
    for r in range(WARMUP_ROUNDS):
        subprocess.check_call(run_cmd +
                              run_location +
                              [ run_option ],
                              stdout = subprocess.PIPE)
    for r in range(TEST_ROUNDS):
        with Timer() as t:
            subprocess.check_call(run_cmd +
                                  run_location +
                                 [ run_option ],
                                  stdout = subprocess.PIPE)
        print "Running '%s' with %s - time taken: %.4f seconds" % \
            (test, language, t.interval)

def usage():
    """Prints the usage info for this benchmark suite."""
    print >>sys.stderr, """\
Usage: python main.py [--test options] [language ...]
    where test is a test and language is a language, and options is...
    wait for it... the options to run for a given test. Options could be the
    number of iterations to run for or the file to sort, or whatever the test
    requires.
"""
    sys.exit(2)

def main():
    """Starts the benchmark suite."""
    try:
        opts, args = getopt.getopt(sys.argv[1:], OPTIONS, LONG_OPTIONS)
    except getopt.GetoptError as err:
        print >>sys.stderr, str(err)
        usage()
    if "help" in opts:
        usage()
    for test in opts:
        for language in args:
            run(test[0][2:], language, test[1])

if __name__ == "__main__":
    main()
