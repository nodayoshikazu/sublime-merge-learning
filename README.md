# sublime-merge-learning
Learning how to use Sublime merge

For the next push, please take a look at the attched screen. See that example (it was just a local branch so you understand the expectations)? I gathered all your content, rebased it (resolving all conflicts against origin/develop), linted everything properly, and addressed test crashes. When tests fail, you can use @unittest.skip (it works on both methods and classes). Also, make sure there are no print statements at runtime. Instead, use logger_manager to instantiate logger objects. Then you can set individual file logging levels per file within if __name__ == "__main__" for debugging purposes without affecting the other file's logger levels, take a look to logger_manager singleton.



Please get into the habit of using logger objects instead of print. You can add as many logger.debug calls as needed, but at runtime (for the final distributable or pipeline level), the logging level will be set to INFO. That way, debug statements won’t create unnecessary noise.
