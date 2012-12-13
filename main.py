## Starts the benchmark suite.

import getopt, sys, time, subprocess

OPTIONS = ""
LONG_OPTIONS = [ "help", "fib" ]

JS_RUN = "node"

FIBS_DIR = "fibs-recursive-memo/"

RUN_CMDS = { "js" : JS_RUN }
TEST_CMDS = {
    "fibs" : {
        "js" : FIBS_DIR + "js/fibs.js"
        }
    }

class Timer:
    """Class to time running calculations."""
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start

def run(test, language, iterations):
    """Runs TEST using LANGUAGE, times the result, and returns the time
    used in such a calculation."""
    with Timer() as t:
        subprocess.check_call([ RUN_CMDS[language],
                                TEST_CMDS[test][language],
                                str(iterations) ])
    print "time: %f" % t.interval

def usage():
    """Prints the usage info for this benchmark suite."""
    print >>sys.stderr, """\
Usage: python main.py [--test ...] [language ...]
    where test is a test and language is a language.
"""
    sys.exit(2)

def main():
    """Starts the benchmark suite."""
    run("fibs", "js", 1000)
    sys.exit(0)
    try:
        opts, args = getopt.getopt(sys.argv[1:], OPTIONS, LONG_OPTIONS)
    except getopt.GetoptError as err:
        print >>sys.stderr, str(err)
        usage()
    if "help" in opts:
        usage()
    for test in opts:
        for language in args:
            # run test on language
            pass

if __name__ == "__main__":
    main()
