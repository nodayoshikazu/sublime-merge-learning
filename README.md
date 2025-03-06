# sublime-merge-learning
Learning how to use Sublime merge

For the next push, please take a look at the attched screen. See that example (it was just a local branch so you understand the expectations)? I gathered all your content, rebased it (resolving all conflicts against origin/develop), linted everything properly, and addressed test crashes. When tests fail, you can use @unittest.skip (it works on both methods and classes). Also, make sure there are no print statements at runtime. Instead, use logger_manager to instantiate logger objects. Then you can set individual file logging levels per file within if __name__ == "__main__" for debugging purposes without affecting the other file's logger levels, take a look to logger_manager singleton.



Please get into the habit of using logger objects instead of print. You can add as many logger.debug calls as needed, but at runtime (for the final distributable or pipeline level), the logging level will be set to INFO. That way, debug statements won’t create unnecessary noise.

Additionally, I'm making sure all class methods within sections (public, private, overrides, ...) are sorted alphabetically. In general, I generally sort any file that can be sorted because it significantly reduces Git diffs and makes solving merge bugs & merge conflicts a piece of cake. For this sorting I use a custom Sublime Text plugin for this, but if you're on Emacs, it wouldn’t work. Also, the idea of "commented sections" per class is because when folding methods at certain levels it gives an overall view of the whole thing without focusing on low-level implementation

### Key Guidelines:
- Always keep your feature branch **squashed and rebased** against origin/develop. Make sure just lint and just test return an exit code 0—this is the first sign that the branch is **releaseable and reviewable**.
- **Favor logger.debug over print**. I usually instruct LLMs with something like: _"Add logger.debug calls in the necessary spots to identify X, Y, Z..."_
- **Stress tests are useful**, but unit test suites (`just test`) should run in milliseconds or a few seconds. If we want to add stress tests, they should be **kept out** of the just test recipe to avoid slowing down the pipeline.
- **Fix the ongoing issue** as pointed out in your previous message.



Regarding communication, sure, no problem we can talk on Discord and getting markdown formatting for free, no problem, though I connect at specific times (outside work). However, it'd be even better we get into the rhythm of **Pull Request (PR) reviews**. GitHub has a powerful reviewing system, and I insist on always creating **releasable and reviewable** feature branches. That way, reviewers can focus on design, code, and performance rather than just ensuring releaseability.



PRs also integrate with **CI/CD and automation**. I’m not sure if I added a pipeline to this repo, but in others, I’ve enabled **pipeline triggers** to check PR statuses automatically. This way, I know if a PR is good before even reviewing it. If no pipeline in this repo, I'll add it eventually after your work makes it into origin/develop and becomes versioned



One last thing—I’m a CLI freak and automate almost everything (including git workflows), but when it comes to prepare manual or feature branches and releases on idividual repos like this one, **Sublime Merge is unbeatable**. It has a command palette, customizable UI, and allows keyboard-only navigation to move across repos, you can open diffs on your favourite editors, all git operations are extremely easy and you can check which exact git operation you're spawning every time. Even as a hardcore CLI user who has contributed to Git’s codebase, I always found **Sublime Merge made me 10x faster** (no joking). Many Git power users I’ve worked with were initially reluctant to adopt it, but once they did, their efficiency **improved significantly** in comparison to raw git cli interaction.

Hello Riverpool
