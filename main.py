#!/usr/bin/python
## Starts the benchmark suite.

import getopt, sys, time, subprocess

OPTIONS = ""
LONG_OPTIONS = [ "help", "fibs" ]
WARMUP_ROUNDS = 2
TEST_ROUNDS = 10

JS_RUN = "node"
HS_RUN = "runhaskell"
BIN_RUN = "./execbin.sh"
PYTHON_RUN = "python"

FIBS_DIR = "fibs/"

FIBS_ITER = 35

RUN_CMDS = {
    "js" : JS_RUN,
    "hs" : HS_RUN,
    "hsc" : BIN_RUN,
    "py" : PYTHON_RUN
    }
TEST_CMDS = {
    "fibs" : {
        "js" : FIBS_DIR + "js/fibs.js",
        "hs" : FIBS_DIR + "hs/fibs.hs",
        "hsc" : FIBS_DIR + "hs/fibs",
        "py" : FIBS_DIR + "py/fibs.py"
        }
    }
ITERATIONS = {
    "fibs" : str(FIBS_ITER)
    }

class Timer:
    """Class to time running calculations."""
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start

def run(test, language):
    """Runs TEST using LANGUAGE, times the result, and returns the time
    used in such a calculation."""
    # TODO : check for languages/tests not supported
    for r in range(WARMUP_ROUNDS):
        subprocess.check_call([ RUN_CMDS[language],
                                TEST_CMDS[test][language],
                                ITERATIONS[test] ],
                              stdout = subprocess.PIPE)
    for r in range(TEST_ROUNDS):
        with Timer() as t:
            subprocess.check_call([ RUN_CMDS[language],
                                    TEST_CMDS[test][language],
                                    ITERATIONS[test] ],
                                  stdout = subprocess.PIPE)
        print "Running '%s' with %s - time taken: %.4f seconds" % \
            (test, language, t.interval)

def usage():
    """Prints the usage info for this benchmark suite."""
    print >>sys.stderr, """\
Usage: python main.py [--test ...] [language ...]
    where test is a test and language is a language.
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
            run(test[0][2:], language)

if __name__ == "__main__":
    main()
